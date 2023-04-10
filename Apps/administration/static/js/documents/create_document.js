var fields = {
    items: {
        expedients: '',
        document_type: '',
        date: '',
        file: '',
    },
};

$(function () {

    function values() {
        $.each(fields.items, function (i) {
            if (i === 'file') {
                const file = $('#id_file').val();
                if (file === '') {
                    const files = $('#before-file'); // CONTAINER DONDE SE ECUENTRAN LA ETIQUETA A CON LA RUTA
                    if (files.find('a').length) {
                        // fields.items[i] = files.children('a').attr('href');
                        fields.items[i] = files.children('a').text();
                    } else {
                        fields.items[i] = '';
                    }
                } else {
                    fields.items[i] = $('#id_' + i + '')[0].files[0]
                }
            } else {
                fields.items[i] = $('#id_' + i + '').val();
            }
        });
    }

// Capturando el evento de FECHA_DE, para obtener el año completo de la fecha ingresada
    $('#id_date_of').on('blur', function () {
        const year = new Date($('#id_date_of').val());
        $('#id_year_of').val(year.getFullYear());
    });

// Capturando el evento de FECHA_HASTA, para obtener el año completo de la fecha ingresada
    $('#id_date_to').on('blur', function () {
        const year = new Date($('#id_date_to').val());
        $('#id_year_to').val(year.getFullYear());
    });

// Evento envio de informacion
    $('#form-document').on('submit', function (e) {
        e.preventDefault();
        values();
        // var parameters = $(this).serializeArray();
        // console.log(parameters)
        var parameters = new FormData(this);
        parameters.append('vents', JSON.stringify(fields.items));
        parameters.append('action', $('input[name="action"]').val());

        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
            location.href = '/administracion/documentos/list';
        });
    });
})
;