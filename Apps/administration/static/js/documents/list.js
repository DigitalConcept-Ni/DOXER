// Funcion para mostrar el model informativo de la tabla consulta expediente
var tbDocu;
$(function () {
    tbDocu = $('.table').DataTable({
        deferRender: true,
        responsive: true,
        autoWidth: false,
        destroy: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'search_data'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {"data": "file_code"},
            {"data": "client_code"},
            {"data": "document_type"},
            {"data": "date"},
            {"data": "file"},
            {"data": "file"},
        ],
        columnDefs: [
            {
                targets: [0, 1, 2, 3, 4],
                class: 'text-center',
                //orderable: false,
            },
            {
                targets: [5],
                class: 'text-center',
                //orderable: false,
                render: function (data, type, row) {
                    if (data === 'No insertado') {
                        var button = '<a href="#" type="button" class="btn btn-danger disabled"><i class="far fa-file-pdf"></i></a>'
                        return button
                    } else {
                        var button = '<a href="/media/' + data + '" target="_blank" type="button" class="btn btn-danger" ><i class="fas fa-file-pdf"></i></a>';
                        return button;
                    }
                },
            },
            {
                targets: [6],
                class: 'text-center',
                //orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a title="Editar registro" href="/administracion/documentos/edit/' + row.id + '/" type="button" class="btn btn-warning"><i class="fas fa-edit"></i></a>';
                    buttons += '<a title="Eliminar registro" href="/administracion/documentos/delete/' + row.id + '/" type="button" class="btn btn-danger" style="margin: 0 5px 0 5px"><i class="fas fa-trash"></i></a>';
                    // buttons += '<a title="Historial de modificaciones" rel="history" type="button" class="btn bg-olive" style="color: white;"><i class="fas fa-history"></i></a>';
                    return buttons;
                },
            },
        ],
        initComplete: function (settings, json) {
        }
    });

    $('.table tbody').on('click', 'a[rel="history"]', function () {
        var tr = tbDoc.cell($(this).closest('td, li')).index();
        var data = tbDoc.row(tr.row).data();
        // console.log(data);
        $('#tableInfoIndexado').DataTable({
            // dom: 'Bfrtip',
            dom: 't',
            deferRender: true,
            responsive: true,
            autoWidth: false,
            destroy: true,
            ajax: {
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_history',
                    'id': data.id
                },
                dataSrc: ""
            },
            columns: [
                {"data": "date_creation"},
                {"data": "user_creation"},
                {"data": "date_update"},
                {"data": "user_update"},
            ],
            columnDefs: [
                {
                    targets: [-1, -2, -3, -4],
                    class: 'text-center',
                    //orderable: false,
                },
            ],
            initComplete: function (settings, json) {
            }
        });
        $('#modalInfo').modal('show');
    });

});