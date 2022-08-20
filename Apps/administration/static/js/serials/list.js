// Funcion para mostrar el model informativo de la tabla consulta expediente
var tbSerials;
$(function () {
    tbSerials = $('.table').DataTable({
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
            {"data": "name"},
            {"data": "name"},
        ],
        columnDefs: [
            {
                targets: [0, 1],
                class: 'text-center',
                //orderable: false,
            },
            {
                targets: [2],
                class: 'text-center',
                //orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a title="Editar registro" href="/administration/serials/edit/' + row.id + '/" type="button" class="btn btn-warning"><i class="fas fa-edit"></i></a>';
                    buttons += '<a title="Eliminar registro" href="/administration/serials/delete/' + row.id + '/" type="button" class="btn btn-danger" style="margin: 0 5px 0 5px"><i class="fas fa-trash"></i></a>';
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