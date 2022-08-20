var list = {
    items: {
        template_name: '',
        departament: '',
        campos: [],
    },
    list: function () {
        tbListas = $('#tbListas').DataTable({
            dom: 't',
            deferRender: true,
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.campos,
            columns: [
                {"data": "id"},
                {"data": "field_name"},
                {"data": "data_type"},
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
                    targets: [1, 2],
                    class: 'text-center',
                    //orderable: false,
                },
            ],
            initComplete: function (settings, json) {
                // alert('finish')
            }
        });
    },
};

$(function () {

    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });

    //Insercion de datos a la tabla
    $('#insert_info').on('click', function () {
        var nombre_campo = $('#nombre_campo');
        var tipo_dato = $('#data_field');

        let info = {};
        info['id'] = 1;
        info['field_name'] = nombre_campo.val();
        info['data_type'] = tipo_dato.val();

        if (nombre_campo.val() === '') {
            message_error({'error': 'Ingrese un nombre de campo'});
        } else if(tipo_dato.val() === null) {
            message_error({'error': 'Ingrese un tipo de dato para el campo'});
        } else
        {
            list.items.campos.push(info);
            list.list();
            nombre_campo.val('');
            tipo_dato.val('');
            nombre_campo.focus();
        }
    });

    // $('#insert_inf').focus(function () {
    //     $('#insert_info').css("background-color", "#446d61");
    // }).blur(function () {
    //     $('#insert_info').css("background-color", "#3d9970");
    //     $('#client').focus();
    // });

    //Eliminacion de detalle de cajas
    $('#tbListas tbody').on('click', 'a[rel="remove"]', function () {
        var tr = tbListas.cell($(this).closest('td, li')).index();
        list.items.campos.splice(tr.row, 1);
        list.list();
    })

    //Event submit
    $('form').on('submit', function (e) {
        e.preventDefault();

        if (list.items.campos.length === 0) {
            message_error({'error': 'Agregue un campo a la plantilla para continuar'});
            return false;
        }
        console.log(list.items)
        // //var parameters = $(this).serializeArray();
        list.items.template_name = $('#id_template_name').val();
        list.items.departament = $('#id_departament').val();
        var parameters = new FormData();
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('vents', JSON.stringify(list.items));

        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
            location.href = '/administration/plantillas/list';
        });
    });

    list.list();

});