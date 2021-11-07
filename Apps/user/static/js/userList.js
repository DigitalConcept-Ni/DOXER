var tbuser;
$(function () {
    tbuser = $('.table').DataTable({
        responsive: true,
        autoWidth: false,
        detroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'search_user',
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {"data": "username"},
            {"data": "first_name"},
            {"data": "last_name"},
            {"data": "email"},
            {"data": "date_joined"},
            {"data": "date_joined"},
        ],
        columnDefs: [
            {
                targets: [0],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    if (row.branch === ''){
                        return '';
                    } else {
                        return row.branch;
                    }
                },
            },
             {
                targets: [1, 2, 3, 4, 5],
                class: 'text-center',
            },
            {
                targets: [6],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/user/update/' + row.id + '/" type="button" class="btn btn-warning"><i class="fas fa-edit"></i></a>';
                    buttons += '<a href="/user/delete/' + row.id + '/" type="button" class="btn btn-danger" style="margin: 0 5px"><i class="fas fa-trash"></i></a>';
                    // buttons += '<a title="permisos" rel="documents" type="button" class="btn btn-secondary" style="color: white"><i class="fas fa-file-alt"></i></a>';
                    return buttons;
                },
            },
        ],
        initComplete: function (settings, json) {
        }
    });

})
