// Funcion para mostrar el model informativo de la tabla consulta expediente
var tbDocuments;
$(function () {
    let config = [
        {
            targets: [0, 1, 2],
            class: 'text-center',
        },
        {
            targets: [2],
            class: 'text-center',
            //orderable: false,
            render: function (data, type, row) {
                var buttons = '<a title="Editar registro" href="/administracion/document-type/edit/' + data + '/" type="button" class="btn btn-warning"><i class="fas fa-edit"></i></a>';
                buttons += '<a title="Eliminar registro" href="/administracion/document-type/delete/' + data + '/" type="button" class="btn btn-danger" style="margin: 0 5px 0 5px"><i class="fas fa-trash"></i></a>';
                // buttons += '<a title="Historial de modificaciones" rel="history" type="button" class="btn bg-olive" style="color: white;"><i class="fas fa-history"></i></a>';
                return buttons;
            },
        },
    ];
    let data = {
        'action': 'search_data',
        'inserInto': 'rowTable',
        'th': ['id', 'Nombre del Documento', 'Opciones'],
        'table': 'tableData',
        'config': config,
        'modal': false
    }

    drawTables(data)

    // $('.table tbody').on('click', 'a[rel="history"]', function () {
    //     var tr = tbDoc.cell($(this).closest('td, li')).index();
    //     var data = tbDoc.row(tr.row).data();
    //     // console.log(data);
    //     $('#tableInfoIndexado').DataTable({
    //         // dom: 'Bfrtip',
    //         dom: 't',
    //         deferRender: true,
    //         responsive: true,
    //         autoWidth: false,
    //         destroy: true,
    //         ajax: {
    //             url: window.location.pathname,
    //             type: 'POST',
    //             data: {
    //                 'action': 'search_history',
    //                 'id': data.id
    //             },
    //             dataSrc: ""
    //         },
    //         columns: [
    //             {"data": "date_creation"},
    //             {"data": "user_creation"},
    //             {"data": "date_update"},
    //             {"data": "user_update"},
    //         ],
    //         columnDefs: [
    //             {
    //                 targets: [-1, -2, -3, -4],
    //                 class: 'text-center',
    //                 //orderable: false,
    //             },
    //         ],
    //         initComplete: function (settings, json) {
    //         }
    //     });
    //     $('#modalInfo').modal('show');
    // });

});