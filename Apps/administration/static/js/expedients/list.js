// Funcion para mostrar el model informativo de la tabla consulta expediente

let id;
$(function () {

    $('#btn-query-listview').on('click', function (e) {

        let expedient = $('#id_expedients').val();
        if (expedient === '') {
            message_error({'info': 'Por favor, Seleccione un expediente'})
        } else {

            let config = [
                {
                    targets: [0, 1, 2, 3, 4, 5, 6],
                    class: 'text-center',
                    //orderable: false,
                },
                {
                    targets: [7],
                    class: 'text-center',
                    //orderable: false,
                    render: function (data, type, row) {
                        var buttons = '<a title="Editar registro" rel="edit" type="button" class="btn btn-warning"><i class="fas fa-edit"></i></a>';
                        buttons += '<a title="Eliminar registro" rel="delete" type="button" class="btn btn-danger" style="margin: 0 5px 0 5px"><i class="fas fa-trash"></i></a>';
                        if (row[8] === 1) {
                            buttons += '<a title="Informacion Peronsal" rel="personal_info" type="button" class="btn btn-danger" style="color: white"><i class="fas fa-eye"></i></a>';
                        }
                        // buttons += '<a title="Historial de modificaciones" rel="history" type="button" class="btn bg-olive" style="color: white;"><i class="fas fa-history"></i></a>';
                        return buttons;
                    },
                },
            ]

            let data = {
                'action': {
                    'action': 'search_data',
                    'id': expedient
                },
                'inserInto': 'rowTable',
                'th': ['id', 'Departamento', 'Nro Serie', 'Documento', 'Resguardo', 'Codigo Archivo', 'Codigo Cliente', 'Opciones'],
                'table': 'tableData',
                'config': config,
                'modal': false
            };
            drawTables(data);

            // $('#card-query-result').show();


        }


    })


    $('.table tbody').on('click', 'a[rel="edit"]', function () {
        let tr = tableData.cell($(this).closest('td, li')).index();
        let data = tableData.row(tr.row).data();
        location = '/administracion/expedientes/edit/' + data[0] + '/';
    }).on('click', 'a[rel="delete"]', function () {
        let tr = tableData.cell($(this).closest('td, li')).index();
        let data = tableData.row(tr.row).data();
        location = '/administracion/expedientes/delete/' + data[0] + '/';
    }).on('click', 'a[rel="personal_info"]', function (e) {
        let tr = tableData.cell($(this).closest('td, li')).index();
        let id = tableData.row(tr.row).data();

        // console.log(tr)
        // console.log(id)

        let data = {
            'action': {
                'action': 'search_personal_info',
                'id': id[0]
            },
            'inserInto': 'rowModal',
            'th': ['id', 'Expediente', 'Nombres', 'Apellidos', 'Cedula', 'Telefono', 'Direccion'],
            'table': 'tableInfoIndexado',
            'config': [
                {
                    targets: ['_all'],
                    class: 'text-center',
                },
            ],
            'modal': true,
            'complete': true,
        };
        drawTables(data);
    })


})