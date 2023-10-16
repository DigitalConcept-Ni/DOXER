var list = {
    items: {
        branch: '',
        code: '',
        document: '',
        status: '',
        user: '',
        date_joined: '',
        start_date: '',
        end_date: '',
        expedientInfo: [],
    },
    list: function () {
        const action = $('input[name="action"]').val();

        tbListas = $('#tbListas').DataTable({
            dom: 'Bftip',
            deferRender: true,
            responsive: true,
            autoWidth: true,
            destroy: true,
            data: this.items.expedientInfo,
            ordering: false,
            order: false,
            columns: [
                {"data": "id"},
                {"data": "names"},
                {"data": "surnames"},
                {"data": "card_id"},
                {"data": "phone_number"},
                {"data": "file_code"},
                {"data": "client_code"},
                {"data": "address"},
                {"data": "exists"},
                {"data": "joined"},
            ],
            columnDefs: [
                {
                    targets: [0],
                    class: 'text-center',
                    //orderable: false,
                    render: function (data, type, row) {
                        return buttons = '<a rel="remove" title="Eliminar registro" type="button" class="btn btn-danger" style="color: white;"><i class="fas fa-trash"></i></a>';
                    },
                },
                {
                    targets: [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    class: 'text-center',
                },
                {
                    targets: [8],
                    class: 'text-center',
                    render: function (data, type, row) {
                        if (action === 'edit') {
                            if (data === 0 || data === '0') {
                                return '<input type="checkbox" rel="exists"/>';
                            } else if (data === 1 || data === '1') {
                                return '<input type="checkbox" checked rel="exists" />';
                            }
                        } else if (action === 'add') {
                            return '<input type="checkbox" disabled/>';
                        }
                    },
                },
                {
                    targets: [9],
                    class: 'text-center',
                    render: function (data, type, row) {
                        if (action === 'edit') {
                            if (data === 0 || data === '0') {
                                return '<input type="checkbox" rel="joined" disabled/>';
                            } else if (data === 1 || data === '1') {
                                return '<input type="checkbox" checked rel="joined" disabled />';
                            }
                        } else if (action === 'add') {
                            return '<input type="checkbox" disabled/>';
                        }
                    },
                },
            ],
            initComplete: function (settings, json) {
                // alert('finish')
            }
        });
    },
};

var follow = {
    add: 0,
    del: 0,
}

$(function () {
    let action = $('input[name=action]').val();

    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });

    //Insercion de datos a la tabla
    $('#insert_info').on('click', function () {
        let names = $('#names');
        let surnames = $('#surnames');
        let card_id = $('#card_id');
        let phone_number = $('#phone_number');
        let file_code = $('#file_code');
        let client_code = $('#client_code');
        let address = $('#address');
        let info = {};

        if (names.val() === '') {
            message_error({'error': 'Ingrese un cliente'});
        } else if (surnames.val() === '') {
            message_error({'error': 'Ingrese los apellidos'});
        } else if (card_id.val() === '') {
            message_error({'error': 'Ingrese numero de cedula'});
        } else if (phone_number.val() === '') {
            message_error({'error': 'Ingrese un numero de telefono'});
        } else if (file_code.val() === '') {
            message_error({'error': 'Ingrese codigo de expediente'});
        } else if (client_code.val() === '') {
            message_error({'error': 'Ingrese codigo del expediente [ parte cliente ]'});
        } else if (address.val() === '') {
            message_error({'error': 'Ingrese una direccion'});
        } else {
            info['id'] = 1;
            info['names'] = names.val();
            info['surnames'] = surnames.val();
            info['card_id'] = card_id.val();
            info['phone_number'] = phone_number.val();
            info['file_code'] = file_code.val();
            info['client_code'] = client_code.val();
            info['address'] = address.val();
            if (action === 'edit') {
                info['joined'] = 1;
                info['exists'] = 1;
                follow.add += 1;
            } else {
                info['joined'] = 0;
                info['exists'] = 0;
            }
            list.items.expedientInfo.push(info);
            list.list();
            names.val('');
            surnames.val('');
            card_id.val('');
            phone_number.val('');
            file_code.val('');
            client_code.val('');
            address.val('');
            names.focus();
        }
    });

    //ELIMINACION DE UN EXPEDIENTE DE LA CAJA
    $('#tbListas tbody').on('click', 'a[rel="remove"]', function () {
        let tr = tbListas.cell($(this).closest('td, li')).index();
        list.items.expedientInfo.splice(tr.row, 1);
        list.list();
        if (action === 'edit') {
            follow.del += 1;
        }
    }).on('click', 'input[rel="exists"]', function () {
        // DETALLE DEL ESTATUS DEL CONTRATO
        let tr = tbListas.cell($(this).closest('td, li')).index();
        let data = tbListas.row(tr.row).index();
        const _this = $(this);

        if (_this.prop('checked')) {
            list.items.expedientInfo[data].exists = 1
        } else {
            list.items.expedientInfo[data].exists = 0
        }
    }).on('click', 'input[rel="joined"]', function () {
        // DETALLE DEL ESTATUS DE LA CEDULA
        let tr = tbListas.cell($(this).closest('td, li')).index();
        let data = tbListas.row(tr.row).index();
        const _this = $(this);

        if (_this.prop('checked')) {
            list.items.expedientInfo[data].joined = 1
        } else {
            list.items.expedientInfo[data].joined = 0
        }
    })

    // BOX ESTATUS
    function BoxStatus() {
        let R = 0; // REVISADO
        let NR = 0; // NO REVISADO
        let status;

        $.each(list.items.expedientInfo, function (k, v) {
            if (v.exists === 0 || v.exists === '0') {
                NR += 1;
            } else if (v.exists === 1 || v.exists === '1') {
                R += 1;
            }
        });

        if (NR > 0 && R === 0) {
            status = 0
        } else if (R > 0 && NR === 0) {
            status = 2;
        } else if (R > 0 && NR > 0) {
            status = 1;
        }
        return status;
    }

    // funcion para recolectar datos de la caja

    function box_detail() {
        $.each(list.items, function (v) {
            if (v === 'expedientInfo' || v === 'follow') {
                return true;
            } else if (v === 'status') {
                list.items[v] = BoxStatus();
            } else if (v === 'date_joined' || v === 'start_date' || v === 'end_date') {
                var date = $('#id_' + v + '').val();
                list.items[v] = createDate(date);
            } else {
                list.items[v] = $('#id_' + v + '').val();
            }
        });
    }

    //Event submit
    $('form').on('submit', function (e) {
        e.preventDefault();
        if (list.items.expedientInfo.length === 0) {
            message_error({'Error de guardado': 'Agregue resgistros al detalle'});
            return false;
        } else {
            box_detail();
            //var parameters = $(this).serializeArray();
            var parameters = new FormData();
            parameters.append('action', $('input[name="action"]').val());
            parameters.append('box', JSON.stringify(list.items));
            parameters.append('follow', JSON.stringify(follow));

            submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
                location.href = '/inventario/inventario/boxes/expedients/list/';
            });

        }
    });
    list.list();
});