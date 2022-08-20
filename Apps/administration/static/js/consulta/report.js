var date_range = null;
var date_now = new moment().format('YYYY-MM-DD');

var tbQuery;

function modal(id) {
    $('#tbTemplate').DataTable({
        // dom: 'Bfrtip',
        dom: 't',
        deferRender: true,
        responsive: true,
        autoWidth: false,
        destroy: true,
        order: false,
        ordering: false,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'search_modal',
                'id': id,
            },
            dataSrc: ""
        },
        columnDefs: [
            {
                targets: [0, 1],
                class: 'text-center',
                //orderable: false,
            },
        ],
        initComplete: function (settings, json) {
        }
    });
}

function generate_report(parameters) {

    if (date_range !== null) {
        parameters['start_date'] = date_range.startDate.format('YYYY-MM-DD');
        parameters['end_date'] = date_range.endDate.format('YYYY-MM-DD');
    }

    tbQuery = $('#data').DataTable({
        // dom: 'Bfrtip',
        responsive: true,
        autoWidth: true,
        destroy: true,
        deferRender: true,
        order: false,
        // paging: false,
        ordering: false,
        // info: false,
        // searching: false,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: parameters,
            dataSrc: ""
        },
        // buttons: [
        //     {
        //         extend: 'excelHtml5',
        //         text: 'Descargar Excel <i class="fas fa-file-excel"></i>',
        //         titleAttr: 'Excel',
        //         className: 'btn btn-success btn-flat btn-xs'
        //     },
        //     {
        //         extend: 'pdfHtml5',
        //         text: 'Descargar Pdf <i class="fas fa-file-pdf"></i>',
        //         titleAttr: 'PDF',
        //         className: 'btn btn-danger btn-flat btn-xs',
        //         download: 'open',
        //         orientation: 'landscape',
        //         pageSize: 'LEGAL',
        //         customize: function (doc) {
        //             doc.styles = {
        //                 header: {
        //                     fontSize: 18,
        //                     bold: true,
        //                     alignment: 'center'
        //                 },
        //                 subheader: {
        //                     fontSize: 13,
        //                     bold: true
        //                 },
        //                 quote: {
        //                     italics: true
        //                 },
        //                 small: {
        //                     fontSize: 8
        //                 },
        //                 tableHeader: {
        //                     bold: true,
        //                     fontSize: 11,
        //                     color: 'white',
        //                     fillColor: '#2d4154',
        //                     alignment: 'center'
        //                 }
        //             };
        //             doc.content[1].table.widths = ['10%', '20%', '20%', '10%', '10%', '10%', '10%', '10%'];
        //             doc.content[1].margin = [0, 35, 0, 0];
        //             doc.content[1].layout = {};
        //             doc['footer'] = (function (page, pages) {
        //                 return {
        //                     columns: [
        //                         {
        //                             alignment: 'left',
        //                             text: ['Fecha de creación: ', {text: date_now}]
        //                         },
        //                         {
        //                             alignment: 'right',
        //                             text: ['página ', {text: page.toString()}, ' de ', {text: pages.toString()}]
        //                         }
        //                     ],
        //                     margin: 20
        //                 }
        //             });
        //
        //         }
        //     }
        // ],
        // columns: [
        //     {"data": "id"},
        //     {"data": "name"},
        //     {"data": "desc"},
        //     {"data": "desc"},
        // ],
        columnDefs: [
            {
                targets: [0],
                class: 'text-center',
                visible: false,
            },
            {
                targets: [8],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    if (data === '') {
                        var button = '<a href="#" type="button" class="btn btn-danger disabled"><i class="far fa-file-pdf"></i></a>'
                        return button
                    } else {
                        var button = '<a href="/media/' + data + '" target="_blank" type="button" class="btn btn-danger" ><i class="fas fa-file-pdf"></i></a>';
                        return button;
                    }
                },
            },
            {
                targets: [9],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    buttons = '<a title="Documentos en expediente" rel="documents" type="button" class="btn bg-secondary" style="margin-right:2px;color: white !important;"><i class="fas fa-file-alt"></i></a>';
                    buttons += '<a title="Informacion Periodica" rel="history" type="button" class="btn bg-orange" style="color: white !important;"><i class="fas fa-info"></i></a>';
                    return buttons;
                }
            }
        ],
        initComplete: function (settings, json) {

        }
    });

    $('.table tbody').on('click', 'a[rel="history"]', function () {
        var tr = tbQuery.cell($(this).closest('td, li')).index();
        var data = tbQuery.row(tr.row).data();
        // console.log(data[0]);

        $('#tableInfoIndexado').DataTable({
            // dom: 'Bfrtip',
            dom: 't',
            deferRender: true,
            responsive: true,
            autoWidth: false,
            destroy: true,
            order: false,
            ordering: false,
            ajax: {
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_dates',
                    'id': data[0]
                },
                dataSrc: ""
            },
            columnDefs: [
                {
                    targets: [0],
                    class: 'text-center',
                    visible: false,
                },
                {
                    targets: [0, 1, 2, 3, 4, 5],
                    class: 'text-center',
                    //orderable: false,
                },
            ],
            initComplete: function (settings, json) {
                const id = json[0][0]
                modal(id);
            }
        });
        $('#modalInfo').modal('show');
    });

    $('.table tbody').on('click', 'a[rel="documents"]', function () {
        var tr = tbQuery.cell($(this).closest('td, li')).index();
        var data = tbQuery.row(tr.row).data();
        // console.log(data[0]);
        // $('#modalInfo2').modal('show')

        $('#tableInfoDocument').DataTable({
            dom: 'Bfrtip',
            // dom: 't',
            deferRender: true,
            responsive: true,
            autoWidth: false,
            destroy: true,
            order: false,
            ordering: false,
            ajax: {
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_document_in',
                    'id': data[0]
                },
                dataSrc: ""
            },
            columnDefs: [
                {
                    targets: [0],
                    class: 'text-center',
                    visible: false,
                },
                {
                    targets: [0, 1, 2, 3, 4, 5, 6, 7, 8],
                    class: 'text-center',
                    //orderable: false,
                },

                {
                    targets: [9],
                    class: 'text-center',
                    //orderable: false,
                    render: function (data, type, row) {
                        if (data === '') {
                            var button = '<a href="#" type="button" class="btn btn-danger disabled"><i class="far fa-file-pdf"></i></a>'
                            return button
                        } else {
                            var button = '<a href="/media/' + data + '" target="_blank" type="button" class="btn btn-danger" ><i class="fas fa-file-pdf"></i></a>';
                            return button;
                        }
                    },
                },
            ],
            initComplete: function (settings, json) {
            }
        });
        $('#modalInfo2').modal('show');
    });

}

$(function () {

    $('input[name="date_range"]').daterangepicker({
        locale: {
            format: 'YYYY-MM-DD',
            applyLabel: '<i class="fas fa-chart-pie"></i> Aplicar',
            cancelLabel: '<i class="fas fa-times"></i> Cancelar',
        }
    }).on('apply.daterangepicker', function (ev, picker) {
        date_range = picker;
        var parameters = {
            'action': 'search_report',
            'start_date': date_now,
            'end_date': date_now,
        };
        generate_report(parameters);
        $('#data').css('display', 'initial')
    }).on('cancel.daterangepicker', function (ev, picker) {
        $(this).data('daterangepicker').setStartDate(date_now);
        $(this).data('daterangepicker').setEndDate(date_now);
        // date_range = picker;
        // generate_report();
    });

    $('#btn_query').on('click', function () {
        const departamento = $('#id_departamentos')
        const documento = $('#id_documentos')

        if (departamento.val() !== '' && documento.val() !== '') {
            message_error({'error': 'Selecciones una de las 2 opciones'})
        } else if (departamento.val() > 0) {
            var parameters = {
                'action': 'search_departament',
                'id_departament': departamento.val(),
            };
            generate_report(parameters);
            $('#data').css('display', 'initial')
            departamento.val('')
        } else if (documento.val() > 0) {
            var parameters = {
                'action': 'search_document',
                'id_departament': documento.val(),
            };
            generate_report(parameters);
            $('#data').css('display', 'initial')
            documento.val('')
        }
    })
    // generate_report();
});