// Funcion para mostrar datos de la tabla branches
var tbListas;

$(function () {
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
                targets: [1, 2, 3, 4, 5, 6],
                class: 'text-center',
                //orderable: false,
            },
            {
                targets: [7],
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

    let data ={
        'action': 'search_data',
        'inserInto': 'rowTable',
        'th': ['id', 'Sucursal', 'Documento', 'Personal', 'Codigo', 'Estado', 'Usuario', 'Fecha Registro', 'Fecha Inicio', 'Fecha Fin', 'Opciones'],
        'table': 'tableData',
        'config': config,
        'modal': false
    }

    // drawTables(data)

    $('.table tbody').on('click', 'a[rel="detList"]', function () {
        var tr = tbListas.cell($(this).closest('td, li')).index();
        var data = tbListas.row(tr.row).data();
        // console.log(data);
        $('#tableInfoIndexado').DataTable({
            dom: 'Bfrtip',
            buttons: {
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
            },
            deferRender: true,
            responsive: true,
            autoWidth: false,
            destroy: true,
            ajax: {
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_expedients',
                    'id': data.id
                },
                dataSrc: ""
            },
            columns: [
                {"data": "id"},
                {"data": "item"},
                {"data": "branch_name"},
                {"data": "branch_code"},
                {"data": "client"},
                {"data": "credit"},
                {"data": "canceled_date"},
                {"data": "year"},
                {"data": "exists"},
                {"data": "joined"},
            ],
            columnDefs: [
                {
                    targets: [0, 2, 3],
                    // class: 'text-center',
                    visible: false,
                },
                {
                    targets: [1, 4, 5, 6, 7],
                    class: 'text-center',
                    //orderable: false,
                },
                {
                    targets: [8],
                    class: 'text-center',
                    render: function (data, type, row) {
                        if (data === 0 || data === '0') {
                            return '<input type="checkbox" disabled/>';
                        } else if (data === 1 || data === '1') {
                            return '<input type="checkbox" checked disabled/>';
                        }
                    },
                },
                {
                    targets: [9],
                    class: 'text-center',
                    render: function (data, type, row) {
                        if (data === 0 || data === '0') {
                            return '<input type="checkbox" disabled/>';
                        } else if (data === 1 || data === '1') {
                            return '<input type="checkbox" checked disabled/>';
                        }
                    },
                }
            ],
            initComplete: function (settings, json) {
            }
        })
        $('#modalInfo').modal('show');
    }).on('click', 'a[rel="delete"]', function () {
        var tr = tbListas.cell($(this).closest('td, li')).index();
        var data = tbListas.row(tr.row).data();
        var id = data.id

        submit_with_ajax('/panel/listado/delete/' + id + '/', 'Eliminar Registro', '¿Estas seguro de eliminar este registro?', {}, evt => {
            window.location.reload();
        });
    }).on('click', 'a[rel=history]', function () {
        var tr = tbListas.cell($(this).closest('td, li')).index();
        var data = tbListas.row(tr.row).data();
        var id = data.id

        $('#tableInfoIndexado2').DataTable({
            dom: 'frtip',
            deferRender: true,
            responsive: true,
            autoWidth: false,
            destroy: true,
            buttons: {
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
            },
            ajax: {
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_history',
                    'id': id,
                },
                dataSrc: ""
            },
            columns: [
                {"data": "id"},
                {"data": "id"},
                {"data": "id"},
                {"data": "id"},
                {"data": "id"},
                {"data": "id"},
                {"data": "user"},
                {"data": "date"},
                {"data": "comment"},
            ],
            columnDefs: [
                {
                    targets: [0, 1, 2, 3, 4, 5],
                    class: 'text-center',
                    visible: false,
                },
                {
                    targets: [6, 7, 8],
                    class: 'text-center',
                },
            ],
            initComplete: function (settings, json) {
            }
        })

        $('#modalInfo2').modal('show')
    });


})