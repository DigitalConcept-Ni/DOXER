var fields = {
    items: {
        departament: '',
        serial: '',
        sub_serial: '',
        document_type: '',
        personal_info: '',
        status: '',
        file_code: '',
        client_code: '',
        description: '',
        date_of: '',
        date_to: '',
        month_of: '',
        month_to: '',
        year_of: '',
        year_to: '',
        det_personal_info: [],
    },
};

$(function () {

    const container = document.getElementById('dataContainer');
    const card_personal_info = $('#card-personal');

    const getPersonalForm = () => {
        const xhr = new XMLHttpRequest();
        xhr.open('get', '/administracion/personal', true)

        // que debe hacer?
        xhr.addEventListener('load', e => {
            container.innerHTML = e.target.responseText
        })

        // Ejecutamos la peticion
        xhr.send();
    }

    // Evento para la actualizacion de los expedientes
    const updateExpedients = e => {
        getPersonalForm();

        setTimeout(() => {
            let personalInfo = fields.items.det_personal_info;

            $.each(personalInfo[0], function (a, b) {
                // console.log(a, b)
                var i = document.getElementById(`id_${a}`);
                i.value = b
            })
            card_personal_info.show();
        }, 1000)

    }

    if (fields.items.det_personal_info.length === 1) {
        // $('#id_personal_info').attr('disabled', 'true');
        // getPersonalForm();
        updateExpedients();
    }


    $('#id_personal_info').on('change', function () {
        let personal_info = $(this).val();

        if (personal_info === '0') {
            container.innerHTML = '';
            card_personal_info.hide();
        } else if (personal_info === '1') {
            getPersonalForm();
            card_personal_info.show();
        }
    })

    const collectPersonalInformation = () => {
        let personal_info = $('#id_personal_info').val();
        let id = ['names', 'surnames', 'address', 'phone_number', 'card_id'];

        if (personal_info === '1') {
            var info = {};
            $.each(id, function (a, b) {
                info[b] = $('#id_' + b).val();
            })
            fields.items.det_personal_info = [info];
        }
    }


    function values() {
        let personalSelector = $('#id_personal_info').val();
        $.each(fields.items, function (i) {
            fields.items[i] = $('#id_' + i + '').val();
        });
        // console.log(fields.items);
        if (personalSelector === '1') {
            collectPersonalInformation();
        }
    }


    $('#prueba').on('click', function () {
        return true;
    })

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
    $('form').on('submit', function (e) {
        e.preventDefault();
        values();
        // personal();
        // var parameters = $(this).serializeArray();
        // console.log(parameters)
        var parameters = new FormData(this);
        parameters.append('vents', JSON.stringify(fields.items));
        parameters.append('action', $('input[name="action"]').val());
        if ($('input[name="action"]').val() === 'edit') {
            parameters.append('id_personal', $('input[name="id_id"]').val());
        }
        console.log(fields.items)

        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
            // fields.items.personal_info.length = 0;
            // location.href = '/administracion/expedientes/list';
            // console.log('Procesos terminado con exito')
            console.log('Proceso terminado')
        });

    });
});