// Funcion para mostrar el model informativo de la tabla consulta expediente
var tbDepart;
$(function () {
    tbDepart = $('.table').DataTable({
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
            {"data": "responsable"},
            {"data": "responsable"},
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
                    var buttons = '<a title="Editar registro" href="/administracion/departamentos/edit/' + row.id + '/" type="button" class="btn btn-warning"><i class="fas fa-edit"></i></a>';
                    buttons += '<a title="Eliminar registro" href="/administracion/departamentos/delete/' + row.id + '/" type="button" class="btn btn-danger" style="margin: 0 5px 0 5px"><i class="fas fa-trash"></i></a>';
                    // buttons += '<a title="Historial de modificaciones" rel="history" type="button" class="btn bg-olive" style="color: white;"><i class="fas fa-history"></i></a>';
                    return buttons;
                },
            },
        ],
        initComplete: function (settings, json) {
        }
    });

});