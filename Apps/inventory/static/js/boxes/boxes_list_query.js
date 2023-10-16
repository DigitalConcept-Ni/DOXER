$(function () {

    $('#btn-search-box').on('click', function () {
        let inputBoxNumber = document.getElementById('box-number').value
        let inputBoxDate = document.getElementById('box-date').value
        let infoSearch = {};


        if (inputBoxNumber === '' && inputBoxDate === '') {
            message_error({'error de seleccion': 'Favor seleccione una de las 2 opciones: Numero de caja o Fecha'});
        } else if (inputBoxNumber !== '' && inputBoxDate !== '') {
            message_error({'error de seleccion': 'Favor seleccione una de las 2 opciones'});
        } else {
            if (inputBoxNumber === '' && inputBoxDate !== '') {
                infoSearch.boxDate = inputBoxDate
            } else if (inputBoxDate === '' && inputBoxNumber !== '') {
                infoSearch.boxNumber = inputBoxNumber
            }
            let config = [
                {
                    targets: [0],
                    class: 'text-center',
                    visible: false,
                },
                {
                    targets: [4],
                    class: 'text-center',
                    render: function (data, type, row) {
                        if (data === '0') {
                            let card = '<a class="btn-sm btn-danger active">PENDIENTE</a>'
                            return card;
                        } else if (data === '1') {
                            let card = '<a class="btn-sm btn-secondary active">REVISION</a>'
                            return card;
                        } else if (data === '2') {
                            let card = '<a class="btn-sm btn-success active">COMPLETA</a>'
                            return card;
                        }
                    },
                },
                {
                    targets: [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    class: 'text-center',
                    //orderable: false,
                },
                {
                    targets: [9],
                    class: 'text-center',
                    //orderable: false,
                    render: function (data, type, row) {
                        var buttons = '<a title="Detalle de lista" rel="detList" type="button" class="btn" style="color: white; background: #009900;"><i class="fas fa-sitemap"></i></a>';
                        buttons += '<a title="Historial de modificaciones" rel="history" type="button" class="btn" style="color: white !important; background: #008f39; margin-left: 5px"><i class="fas fa-history"></i></a>';
                        if (row.is_superuser === true) {
                            buttons += '<a title="Editar registro" href="/panel/listado/edit/' + row.id + '/" type="button" style="margin: 0 5px 0 5px;" class="btn btn-secondary superUserEdit"><i class="fas fa-edit"></i></a>';
                            buttons += '<a title="Eliminar registro"  rel="delete"  type="button" class="btn btn-danger" style="color: white"><i class="fas fa-trash"></i></a>';
                        } else {
                            if (row.is_staff === true) {
                                return buttons;
                            } else {
                                if (row.status === 2 || row.status === '2') {
                                    return buttons;
                                } else {
                                    buttons += '<a title="Editar registro" href="/panel/listado/edit/' + row.id + '/" type="button" style="margin: 0 5px 0 5px;" class="btn btn-secondary superUserEdit"><i class="fas fa-edit"></i></a>';
                                }
                            }
                        }
                        return buttons;
                    },
                },
            ];

            let data = {
                // 'url': location.pathname,
                'data': {'action': 'search_data', 'data': JSON.stringify(infoSearch)},
                'inserInto': 'rowTable',
                'th': ['id', 'Sucursal', 'Documento', 'Codigo', 'Estado', 'Usuario', 'Fecha Registro', 'Fecha Inicio', 'Fecha Fin', 'Opciones'],
                'table': 'tableData',
                'config': config,
                'modal': false,
                // 'buttons': {}
            }

            drawTables(data);
        }

    });

    $('#tableData tbody').on('click', 'a[rel="detList"]', function () {
        var tr = tableData.cell($(this).closest('td, li')).index();
        var data = tableData.row(tr.row).data();

        let config = [
            {
                targets: [0],
                class: 'text-center',
                visible: false,
            },

        ]

        let buttons = {
            dom: {
                button: {
                    className: 'btn'
                }
            },
            buttons: [
                {
                    extend: "excel",
                    text: 'Exportar a Excel',
                    className: 'btn btn-outline-success'
                }
            ]
        }

        let dat = {
            // 'url': location.pathname,
            'data': {'action': 'search_expedients', 'boxNumber': data[0]},
            'inserInto': 'rowModal',
            'th': ['id', 'item', 'Codigo caja', 'Nombres', 'Apellidos', 'Cedula', 'Telefono', 'Direccion', 'Existencica', 'Agregado', 'Opciones'],
            'table': 'tableModal',
            'config': config,
            'modal': true,
            'buttons': buttons,
        }

        drawTables(dat)
    });


})

