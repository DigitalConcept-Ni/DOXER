/*Escript realizado para el modulo de indexing, ultima version estable
segun requerimientos y necesidades del mismo modulo*/
$(function () {

    //Variables globales para utilizacion y comunicacion entre las funciones
    let pdf = null;
    let fileNum = null;
    let fileName = null;
    let archivos;
    let no_render = [];
    let index_file;


    let select = $('select[name="directory"]');
    let option = '<option value="">Selecciones una carpeta</option>'

    //Evento para cargar las carpetas.
    $.ajax({
        url: window.location.pathname,
        method: "POST",
        data: {
            'action': 'search_directory'
        }
    }).done(function (request) {
        carpetas = request.carpetas;
        $('#next_doc').addClass('disabled');

        $.each(carpetas, function (key, value) {
            option += '<option value="' + value.name + '">' + value.name + '</option>';
        });
    }).fail(function (jqXHR, textStatus, errorThrown) {
    }).always(function (request) {
        select.html(option);
    });

    var select_seccion = $('input[name="seccion"]');

    $('.select2').select2({
        data: data,
        theme: "bootstrap4",
        language: 'es'
    });

    $('select[name="documento"]').on('change', function () {
        var id = $(this).val();
        // if (id === '') {
        //     select_documento.html(options);
        //     return false;
        // }
        $.ajax({
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'search_section_id',
                'id': id
            },
            dataType: 'json',
        }).done(function (data) {
            if (!data.hasOwnProperty('error')) {
                select_seccion.attr('value', data.id);
                return false;
            }
            message_error(data.error);
        }).fail(function (jqXHR, textStatus, errorThrown) {
            alert(textStatus + ': ' + errorThrown);
        }).always(function (data) {
            // select_products.html(options);
        });
    });

    //Renderizacin de las hojas del PDF
    function renderPage(page, id) {
        let scale = 1;
        let viewport = page.getViewport({scale: scale});

        let canvas = $('<canvas class="page-preview" style="box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);"></canvas>');
        let ctx = canvas[0].getContext('2d');
        canvas[0].width = viewport.width;
        canvas[0].height = viewport.height;

        let renderContext = {
            canvasContext: ctx,
            viewport: viewport
        };
        page.render(renderContext);
        return canvas;
    }

    //Funcion para cargar las hojas del pdf
    function loadMiniatures(pdf) {
        const miniatures = $('.miniatures').empty();
        for (let i = 1; i <= pdf.numPages; i++) {
            pdf.getPage(i).then(function (page, id) {
                let canvas = renderPage(page);
                let inputs = `<div id="${i - 1}">
            <input type="checkbox" name="page" value="${i - 1}" style="height: 30px; width:30px">
            <input type="hidden" name="action" value="">
                                                </div>`;
                let pageContainer = $(`<div class="page" style="order: ${i}" ></div>`)
                    .append(canvas)
                    .append(inputs);
                miniatures.append(pageContainer);
            })
        }
    }

    //Funcion para crear y preparar lienzo para renderizas cada hoja del pdf
    function crearCanvas() {
        $('.miniatures').empty();
        document.getElementById('docname').value = '';
    }

    //Evento para abrir archvio pdf seleccionado desde la lista (archivos) al principio del scrip;
    const openFIle = async (filename) => {
        let folder = $('#directoryes').val();
        let url = `/media/migration/${folder}/${filename}`;
        // let url = '/media/migration/' + filename;
        const loadingTask = pdfjsLib.getDocument(url);
        loadingTask.promise.then(pdf => {
            // The document is loaded here...
            // console.log(pdf._pdfInfo.numPages)
            fileNum = archivos.findIndex(element => element === filename);
            fileName = filename;
            loadMiniatures(pdf);
            document.getElementById('numfile').value = fileNum;
            $('#numfile').attr('value', fileNum);
        });
        document.getElementById('docname').value = filename;
        $('#docname').attr('value', filename);
    }

    // let url = '/media/' + 'migration/test.pdf';
    // const loadingTask = pdfjsLib.getDocument(url);
    // loadingTask.promise.then(pdf => {
    //     // The document is loaded here...
    //     console.log(pdf._pdfInfo.numPages)
    //     loadMiniatures(pdf)
    // });

    function onPrevDoc() {
        if (fileNum <= 0) {
            return;
        }
        openFIle(archivos[fileNum - 1]);
    }

//Evento para eliminar las paginas o ocultar las paginas indexadas
    const deletePage = function () {
        if (no_render.length === 0) {
            // console.log("No Hay paginas que limpiar")
        } else {
            $.each(no_render, function (e, value) {
                $.each(value, function (i, v) {
                    const input = document.getElementById(v).parentNode;
                    $(input).css({
                        display: 'none'
                    });
                });
            })
        }
    };
//Evento para enviar los datos de las paginas y donde se guardaran
    $('#indexing').on('submit', function (e) {
        e.preventDefault();
        const data = new FormData(this);
        data.append('action', 'indexar');
        $.ajax(".", {
            url: window.location.pathname,
            method: "POST",
            data: data,
            processData: false,
            contentType: false,
            success: function (response) {
                no_render.push(response.no_render);
                index_file = response.openFile
                // openFIle(archivos[index_file]);
                deletePage();
                Swal.fire({
                    position: 'top-end',
                    icon: 'info',
                    title: 'Documentos indexados correctamente',
                    showConfirmButton: false,
                    timer: 1200
                });
                $('#menu').addClass('oculto')
                $('input[type=checkbox]').prop('checked', false);
                // $('#last-document')
                //     .data('document', response.document)
                //     .removeAttr('disabled');
                //
                // $('.miniatures').empty();
                // $('#docname').val('');
                // $('.autocomplete-document').val('');
                // onNextDoc();
            }
        })
    });

    //Evento para cambiar de PDF
    function onNextDoc() {
        const data = new FormData();
        data.append('doc_name', $('#docname').val());
        data.append('carpeta', $('#directoryes').val());
        data.append('action', 'next');

        submit_with_ajax(window.location.pathname, 'Siguiente Documento', '¿Seguro de viasualizar el siguiente documento?', data, function () {
            if (fileNum >= archivos.length - 1) {
                return;
            }
            openFIle(archivos[fileNum + 1]);
            no_render = []
            const fileInfo = $('#files').val();
            files.value = fileInfo - 1;
        })
    }

//Evento para seleccionar y mostras las carpetas disponibles
    $('#directoryes').on('change', function () {
        const _this = $(this);

        if (_this.val() === '') {
            // console.log('vacio')
            crearCanvas();
            document.getElementById('files').value = ''
            $('#next_doc').addClass('disabled');
        } else {
            $.ajax('.', {
                url: window.location.pathname,
                method: "POST",
                data: {
                    'action': 'refresh',
                    'carpeta': _this.val()
                },
                success: function (request) {
                    archivos = request.archivos;
                    document.getElementById('files').value = request.files;
                    if (archivos.length > 0) {
                        openFIle(archivos[0]);
                    } else {
                        crearCanvas();
                    }
                    $('#next_doc').removeClass('disabled');
                    if (_this.val() === 'ACTUALIZACION') {
                        if ($('#files').val() >= 1) {
                            $('#btn_doc_upgrade').toggle();
                        }
                    } else {
                        if ($('#btn_doc_upgrade').is(':visible')) {
                            $('#btn_doc_upgrade').hide();
                        }
                    }
                }
            })
        }
    });

    $('#btn_insert_document').on('click', function () {
        $('#block_insert').toggle();
    });

    // boton para insertar los archivos nuevos
    $('#btn_insert_file').on('click', function () {

        if ($('#insert_file').val() === '') {
            message_error({'error': 'Selecciones un documento para poder insertarlo'})
        } else {
            const data = new FormData();
            data.append('file', $('#insert_file')[0].files[0]);
            data.append('action', 'insert_file');

            $.ajax('.', {
                method: "POST",
                data: data,
                contentType: false,
                processData: false,
                success: function (response) {
                    // console.log(response);
                    // archivos = [...response.archivos];
                    // openPdf(response.filename);
                    $('#insert_file').val(null);
                    $('#block_insert').toggle();
                    message_info(response)
                    setTimeout(function () {
                        location.reload();
                    }, 1450)
                }
            })
        }
    });

    //Boton para eliminar el documento subido
    $('#btn_doc_upgrade').on('click', function () {
        const data = new FormData();
        data.append('docname', $('#docname').val());
        data.append('directory', $('#directoryes').val());
        data.append('action', 'delete_file');

        submit_with_ajax(window.location.pathname, 'Eliminar Documento', 'Seguro de Eliminar el documento actual', data, function (data) {
            message_info(data);
            if (fileNum >= archivos.length - 1) {
                crearCanvas();
                document.getElementById('files').value = 0;
                $('#next_doc').addClass('disabled');
                $('#btn_doc_upgrade').toggle();
                return;
            }
            openFIle(archivos[fileNum + 1]);
            const fileInfo = $('#files').val();
            files.value = fileInfo - 1
        });
    });

    //Evento para ocultar y mostrar formulario de indexing
    window.addEventListener("scroll", function (e) {
        var scroll = window.pageYOffset;

        if (scrollAnterior > scroll) {
            if ($('input[type=checkbox]').is(':checked')) {
                // alert('seleccionado');
                document.querySelector('#menu').classList.remove('oculto');
            } else {
                if (scroll <= 180) {
                    document.querySelector('#menu').classList.remove('oculto');
                }
            }
        } else {
            document.querySelector('#menu').classList.add('oculto');
        }
        scrollAnterior = scroll;
    })


// document.getElementById('prev_doc').addEventListener('click', onPrevDoc);
    document.getElementById('next_doc').addEventListener('click', onNextDoc);
// document.getElementById('clean_page').addEventListener('click', deletePage);


})
;

