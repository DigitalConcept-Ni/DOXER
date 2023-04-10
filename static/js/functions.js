function message_error(obj) {
    var html = '<ul style="list-style: none" ">'
    $.each(obj, function (key, value) {
        html += '<li>' + value + '</li>'
    })
    html += '</ul>';
    Swal.fire({
        title: 'Error!',
        html: html,
        icon: 'error'
    })
}

function message_info_top(obj) {
    var html = '<ul style="list-style: none" ">'
    $.each(obj, function (key, value) {
        html += '<li>' + value + '</li>'
    })
    html += '</ul>';
    Swal.fire({
        position: 'top-end',
        icon: 'info',
        title: html,
        showConfirmButton: false,
        timer: 1200
    });
}


function message_info(obj) {
    var html = '<ul style="list-style: none;">'
    $.each(obj, function (key, value) {
        html += '<li>' + value + '</li>'
    })
    html += '</ul>';
    Swal.fire({
        title: 'Proceso Exitoso!',
        html: html,
        icon: 'success'
    })
}

function message_info2(obj) {
    var html = '<ul style="list-style: none;">'
    $.each(obj, function (key, value) {
        html += '<li>' + value + '</li>'
    })
    html += '</ul>';

    Swal.fire({
        title: 'Proceso Exitoso',
        icon: 'success',
        html: html,
        confirmButtonText: 'Ok',
    }).then((result) => {
        if (result.value === true) {
            location.reload();
        }
    })
}

function submit_with_ajax(url, title, content, parameters, callback) {
    $.confirm({
        theme: 'material',
        title: title,
        icon: 'fa fa-info',
        content: content,
        columnClass: 'small',
        typeAnimated: true,
        cancelButtonClass: 'btn-primary',
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            info: {
                text: "Si",
                btnClass: 'btn-primary',
                action: function () {
                    $.ajax({
                        url: url, //window.location.pathname
                        type: 'POST',
                        data: parameters,
                        dataType: 'json',
                        processData: false,
                        contentType: false,
                    }).done(function (data) {
                        if (!data.hasOwnProperty('error')) {
                            callback();
                            if (data.hasOwnProperty('info')) {
                                message_info(data);
                            }
                            return false;
                        } else if (!data.hasOwnProperty('info')) {
                            console.log(data)
                            message_info(data);
                        }
                        message_error(data.error);
                    }).fail(function (jqXHR, textStatus, errorThrown) {
                        alert(textStatus + ': ' + errorThrown);
                    }).always(function (data) {

                    });
                }
            },
            danger: {
                text: "No",
                btnClass: 'btn-red',
                action: function () {

                }
            },
        }
    })
}

// window.addEventListener('load', () => {
//     const contenedor_loader = document.querySelector('.preloader_container');
//     contenedor_loader.style.opacity = 0
//     contenedor_loader.style.visibility = 'hidden'
// });