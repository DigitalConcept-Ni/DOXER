$(function () {
    let config = [{
        targets: [0, 1, 2, 3, 4, 5, 6, 7],
        class: 'text-center'
    },
        {
            targets: [7],
            render: function (data, type, row) {
                var buttons = '<a title="Editar registro" rel="edit" type="button" class="btn btn-secondary"><i class="fas fa-edit"></i></a>';
                buttons += '<a title="Eliminar registro" rel="delete"  type="button" class="btn btn-danger" style="margin: 0 5px 0 5px"><i class="fas fa-trash"></i></a>';
                // buttons += '<a title="Historial de modificaciones" rel="history" type="button" class="btn bg-olive" style="color: white;"><i class="fas fa-history"></i></a>';
                return buttons;
            },
        }

    ]
    let data = {
        'action': 'search_supplier',
        'inserInto': 'rowTable',
        'th': ['id', 'Nombre', 'Vendedor', 'Direccion', 'Correo', 'Telefono', 'Opciones'],
        'table': 'tableData',
        'config': [],
        'modal': false
    };
    drawTables(data);

    $('.table tbody').on('click', 'a[rel="edit"]', function () {
        var tr = tableData.cell($(this).closest('td, li')).index();
        var data = tableData.row(tr.row).data();
        location = '/inventario/category/update/' + data[0] + '/';
    }).on('click', 'a[rel="delete"]', function () {
        var tr = tableData.cell($(this).closest('td, li')).index();
        var data = tableData.row(tr.row).data();
        location = '/inventario/category/delete/' + data[0] + '/';
    })

    // $('#modalInfo').modal('show');
})