// Funcion para mostrar el model informativo de la tabla consulta expediente
var tbPlantillas;
$(function () {
    tbPlantillas = $('.table').DataTable({
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
            {"data": "template_name"},
            {"data": "departament.name"},
            {"data": "nombre"},
        ],
        columnDefs: [
            {
                targets: [-2, -3, -4],
                class: 'text-center',
                //orderable: false,
            },
            {
                targets: [-1],
                class: 'text-center',
                //orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a title="Editar registro" href="/administration/plantillas/edit/' + row.id + '/"  type="button" class="btn btn-warning"><i class="fas fa-edit"></i></a>';
                    buttons += '<a title="Eliminar registro" href="/administration/plantillas/delete/' + row.id + '/" type="button" class="btn btn-danger" style="margin: 0 5px 0 5px"><i class="fas fa-trash"></i></a>';
                    buttons += '<a title="Campos en esta plantilla" rel="detalle" type="button" class="btn bg-olive" style="color: white;"><i class="fas fa-stream"></i></a>';
                    return buttons;
                },
            },
        ],
        initComplete: function (settings, json) {
        }
    });
    // href="/plantillas/edit/' + row.id + '/"

    $('.table tbody').on('click', 'a[rel="detalle"]', function () {
        var tr = tbPlantillas.cell($(this).closest('td, li')).index();
        var data = tbPlantillas.row(tr.row).data();
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
                {"data": "id"},
                {"data": "field_name"},
                {"data": "data_type"},
                {"data": "data_type"},
            ],
            columnDefs: [
                {
                    targets: [0, 1, 2],
                    class: 'text-center',
                    //orderable: false,
                },
                {
                    targets: [3],
                    // class: 'text-center',
                    //orderable: false,
                    visible: false
                },
            ],
            initComplete: function (settings, json) {
            }
        });
        $('#modalInfo').modal('show');
    })

});