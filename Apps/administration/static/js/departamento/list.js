// Funcion para mostrar el model informativo de la tabla consulta expediente
$(function () {

    $('#btn-query-listview').on('click', function (e) {
        let expedient = $('#id_departaments').val();
        if (expedient === '') {
            message_error({'info': 'Por favor, Seleccione un expediente'})
        } else {
            let config = [
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
                        var buttons = '<a title="Editar registro" rel="edit" type="button" class="btn btn-primary" style="color: white;"><i class="fas fa-edit"></i></a>';
                        buttons += '<a title="Eliminar registro" rel="delete" type="button" class="btn btn-danger" style="margin: 0 5px 0 5px; color: white"><i class="fas fa-trash"></i></a>';
                        // buttons += '<a title="Historial de modificaciones" rel="history" type="button" class="btn bg-olive" style="color: white;"><i class="fas fa-history"></i></a>';
                        return buttons;
                    },
                },
            ]

            let data = {
                'action': {
                    'action': 'search_data',
                    'id': expedient,
                },
                'inserInto': 'rowTable',
                'th': ['id', 'Departamento', 'Responsable', 'Email', 'Telefono', 'Opciones'],
                'table': 'tableData',
                'config': config,
                'modal': false
            };
            drawTables(data);
            $('#card-query-result').show();
        }
    })

    $('.table tbody').on('click', 'a[rel="edit"]', function () {
        var tr = tableData.cell($(this).closest('td, li')).index();
        var data = tableData.row(tr.row).data();
        location = '/administracion/departamentos/edit/' + data[0] + '/';
    }).on('click', 'a[rel="delete"]', function () {
        var tr = tableData.cell($(this).closest('td, li')).index();
        var data = tableData.row(tr.row).data();
        location = '/administracion/departamentos/delete/' + data[0] + '/';
    })


});