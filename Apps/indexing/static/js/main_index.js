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
    let option = '<option value="">Seleccione una carpeta</option>'

    //Evento para cargar las carpetas.
    $.ajax({
        url: window.location.pathname,
        method: "POST",
        data: {
            'action': 'search_directory'
        }
    }).done(function (request) {
        carpetas = request.carpetas;
        $.each(carpetas, function (key, value) {
            option += '<option value="' + value.name + '">' + value.name + '</option>';
        });
    }).fail(function (jqXHR, textStatus, errorThrown) {
    }).always(function (request) {
        select.html(option);
    });


    // Seccion para buscar la seccion oculta de los documentos
    var select_seccion = $('input[name="seccion"]');

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

        let canvas = $(`<canvas id=${id} class="page-preview" style="box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);"></canvas>`);
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
            pdf.getPage(i).then(function (page) {
                let id = i - 1;
                let canvas = renderPage(page, id);
                let inputs = `<div id="${i - 1}" class="confirm-checkbox">
            <input type="checkbox" name="page" value="${i - 1}">
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
    let loader = document.getElementById('preloader_container');
    const openFIle = async (filename) => {

        loader.style.display = 'flex';
        let folder = $('#directoryes').val();
        let url = `/media/indexation/${folder}/${filename}`;
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
                message_info_top({'success': 'Documentos indexados correctamente'})
                $('#menu').addClass('oculto')
                $('input[type=checkbox]').prop('checked', false);
            }
        })
    });

    //Evento para cambiar de PDF
    function onNextDoc() {
        const data = new FormData();
        data.append('doc_name', $('#docname').val());
        data.append('carpeta', $('#directoryes').val());
        data.append('action', 'next');

        submit_with_ajax(window.location.pathname, 'Siguiente Documento', '¿Seguro de viasualizar el siguiente documento? Se eliminara el actual', data, function () {
            // if (fileNum >= archivos.length - 1) {
            //     crearCanvas();
            // }
            openFIle(archivos[fileNum + 1]);
            no_render = []
            const fileInfo = $('#files').val();
            files.value = fileInfo - 1;
            setTimeout(function () {
                decoration()
            }, 2000);
        })
    }

//Evento para seleccionar y mostras las carpetas disponibles
    $('#directoryes').on('change', function () {
        const _this = $(this);

        if (_this.val() === '') {
            crearCanvas();
            document.getElementById('files').value = ''
            $('#next_doc').addClass('disabled');
            $('#btn_doc_delete').addClass('disabled');
            $('#btn_indexing').addClass('disabled');

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
                    console.log(archivos.length)
                    document.getElementById('files').value = request.files;
                    if (archivos.length > 0) {
                        openFIle(archivos[0]);
                        $('#next_doc').removeClass('disabled');
                        $('#btn_doc_delete').removeClass('disabled');
                        $('#btn_indexing').removeClass('disabled');
                        setTimeout(function () {
                            decoration()
                        }, 2000);
                    } else {
                        crearCanvas();
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
                    $('#insert_file').val(null);
                    $('#block_insert').toggle();
                    message_info2(response)
                }
            })
        }
    });

    //Boton para eliminar el documento subido
    $('#btn_doc_delete').on('click', function () {
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
                $('#btn_doc_delete').addClass('disabled');
                $('#btn_indexing').addClass('disabled');
                return;
            }
            openFIle(archivos[fileNum + 1]);
            const fileInfo = $('#files').val();
            files.value = fileInfo - 1
        });
    });

    //Evento para ocultar y mostrar formulario de indexing
    let scrollAnterior = window.pageYOffset;
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

    // PART TO UPDATE

    function decoration() {
        console.log('ready')
        loader.style.display = 'none';
        let page = $('canvas.page-preview');

        // part of the function for colored the border
        page.on('click', function (e) {
            let id = e.currentTarget.id;
            let inputId = $(`input[value="${id}"]`);
            if (inputId.prop('checked') === true) {
                inputId.prop('checked', false);
            } else if (inputId.prop('checked') === false) {
                inputId.prop('checked', true);
                $(`canvas#${id}`).addClass('colored-border');
            }
            // console.log(inputId[0].checked)
            // console.log(e.currentTarget.id);
        }).on('mouseover', function (e) {
            let id = e.currentTarget.id;
            $(`canvas#${id}`).addClass('colored-border');
        }).on('mouseleave', (e) => {
            let id = e.currentTarget.id;
            let inputId = $(`input[value="${id}"]`);
            if (inputId.prop('checked') === true) {
                return;
            } else {
                $(`canvas#${id}`).removeClass('colored-border');
            }
        });

    }

    //END UPDATE


// document.getElementById('prev_doc').addEventListener('click', onPrevDoc);
    document.getElementById('next_doc').addEventListener('click', onNextDoc);
// document.getElementById('clean_page').addEventListener('click', deletePage);


})
;

