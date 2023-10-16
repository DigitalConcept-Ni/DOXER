// Funcion para mostrar datos de la tabla branches
var tbSucursal;

$(function () {

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
                var buttons = '<a title="Editar registro" href="/administracion/branches/edit/' + data + '/" type="button" class="btn btn-secondary"><i class="fas fa-edit"></i></a>';
                buttons += '<a title="Eliminar registro" href="/administracion/branches/delete/' + data + '/" type="button" class="btn btn-danger" style="margin: 0 5px 0 5px"><i class="fas fa-trash"></i></a>';
                // buttons += '<a title="Historial de modificaciones" rel="history" type="button" class="btn bg-olive" style="color: white;"><i class="fas fa-history"></i></a>';
                return buttons;
            },
        },
    ];
    let data = {
        'action': 'search_data',
        'inserInto': 'rowTable',
        'th': ['id', 'Nombre', 'Codgio', 'Responsable', 'Email', 'Numero', 'Opciones'],
        'table': 'tableData',
        'config': config,
        'modal': false
    }

    drawTables(data);

    // tbSucursal = $('.table').DataTable({
    //     deferRender: true,
    //     responsive: true,
    //     autoWidth: false,
    //     destroy: true,
    //     ajax: {
    //         url: window.location.pathname,
    //         type: 'POST',
    //         data: {
    //             'action': 'search_data'
    //         },
    //         dataSrc: ""
    //     },
    //     columns: [
    //         {"data": "id"},
    //         {"data": "name"},
    //         {"data": "code"},
    //         {"data": "code"},
    //     ],
    //     columnDefs: [
    //         {
    //             targets: [-2, -3, -4],
    //             class: 'text-center',
    //             //orderable: false,
    //         },
    //         {
    //             targets: [-1],
    //             class: 'text-center',
    //             //orderable: false,
    //             render: function (data, type, row) {
    //                 var buttons = '<a title="Editar registro" href="/panel/branches/edit/' + row.id + '/" type="button" class="btn btn-secondary"><i class="fas fa-edit"></i></a>';
    //                 buttons += '<a title="Eliminar registro" href="/panel/branches/delete/' + row.id + '/" type="button" class="btn btn-danger" style="margin: 0 5px 0 5px"><i class="fas fa-trash"></i></a>';
    //                 // buttons += '<a title="Historial de modificaciones" rel="history" type="button" class="btn bg-olive" style="color: white;"><i class="fas fa-history"></i></a>';
    //                 return buttons;
    //             },
    //         },
    //     ],
    //     initComplete: function (settings, json) {
    //         // alert('finish')
    //     }
    // });

    // $('.table tbody').on('click', 'a[rel="history"]', function () {
    //     var tr = tbIndex.cell($(this).closest('td, li')).index();
    //     var data = tbIndex.row(tr.row).data();
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
    //             {"data": "user_update"},
    //             {"data": "user_update"},
    //         ],
    //         columnDefs: [
    //             {
    //                 targets: [-3, -4, -5, -6],
    //                 class: 'text-center',
    //                 //orderable: false,
    //             },
    //             {
    //                 targets: [-1, -2],
    //                 visible: false
    //             },
    //         ],
    //         initComplete: function (settings, json) {
    //         }
    //     });
    //     $('#modalInfo').modal('show');
    // });


});