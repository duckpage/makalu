// TRANSMIT MODAL

$('#modal-transmit').on('show.bs.modal', function(e) {
    var code = $(e.relatedTarget).attr('data-code');
    if (code)
        $(e.currentTarget).find('input[id="input-code"]').val(code);
});

$('#modal-transmit').on('hide.bs.modal', function(e) {
    $(e.currentTarget).find('form[id="form-transmit"]').find('input[name="date"]').val('');
});

// DELETE MODAL

$('#modal-delete').on('show.bs.modal', function(e) {
    var message = $(e.relatedTarget).attr('data-message');
    var code = $(e.relatedTarget).attr('data-code');
    var url = $(e.relatedTarget).attr('data-url');
    var redirect = $(e.relatedTarget).attr('data-redirect');

    if (url)
        $(e.currentTarget).find('form[id="form-delete"]').attr('action', url);
    if (message)
        $(e.currentTarget).find('p[id="message-delete"]').text(message);
    if (code)
        $(e.currentTarget).find('input[id="input-code"]').val(code);
    if(redirect){
        $(e.currentTarget).find('input[id="input-redirect"]').val(redirect);
    }
        
});

$('#modal-delete').on('hide.bs.modal', function(e) {
    $(e.currentTarget).find('form[id="form-delete"]').find('div.alert').html('');
    $(e.currentTarget).find('form[id="form-delete"]').find('div.alert').addClass('d-none');
});

$('#form-delete').on('submit', function(event) {
    event.preventDefault();
    var form = $(this);
    form.find('button[type="submit"]').button('loading');
    $.ajax({
        url: form.attr('action'),
        type: 'POST',
        data: form.serialize(),
        success: function(data) {
            if (data.status == 0){
                $('#modal-delete').modal('hide'); 
                if (typeof data.redirect === 'undefined' || !data.redirect){

                    $('.dynamic__item[data-type="'+ data.type +'"][data-code="'+ data.code +'"]').fadeOut(function(){
                        $(this).remove();
                        
                        if ($('.dynamic__container[data-type="'+ data.type +'"]').children().length == 0){
                            $('.dynamic__alert[data-type="'+ data.type +'"]').removeClass('d-none');
                            $('.dynamic__area[data-type="'+ data.type +'"]').addClass('d-none');
                            $('.fileupload__alert[data-type="'+ data.type +'"]').removeClass('d-none');
                        }
                    });
                } else {
                    window.location.href = data.redirect;
                }
            } else {
                form.find('div.alert').html(data.error);
                form.find('div.alert').removeClass('d-none');
            }
            
            form.find('button[type="submit"]').button('reset');
        }
    });
});



// PASSWORD


var rule1, rule2, rule3, rule4, rule5;

function initChackPassword()
{
    $('input[data-mode="password"]').on('keyup', function() {
        var pswd = $(this).val();
        //validate the length
        if ( pswd.length < 8 ) {
            $('.password-info-box .8-char').removeClass('valid');
            rule1 = false;
        } else {
            $('.password-info-box .8-char').addClass('valid');
            rule1 = true;
        }

        //validate letter
        if ( pswd.match(/[A-z]/) ) {
            $('.password-info-box .lowercase-char').addClass('valid');
            rule2 = true;
        } else {
            $('.password-info-box .lowercase-char').removeClass('valid');
            rule2 = false;
        }
        
        //validate capital letter
        if ( pswd.match(/[A-Z]/) ) {
            $('.password-info-box .uppercase-char').addClass('valid');
            rule3 = true;
        } else {
            $('.password-info-box .uppercase-char').removeClass('valid');
            rule3 = false;
        }

        //validate number
        if ( pswd.match(/\d/) ) {
            $('.password-info-box .number-char').addClass('valid');
            rule4 = true;
        } else {
            $('.password-info-box .number-char').removeClass('valid');
            rule4 = false;
        }

        //special char
        if ( pswd.match(/[~`!#$%\^&*+=\-\[\]\\';,/{}|\\":<>\?]/) ) {
            $('.password-info-box .special-char').addClass('valid');
            rule5 = true;
        } else {
            $('.password-info-box .special-char').removeClass('valid');
            rule5 = false;
        }

        if (rule1 && rule2 && rule3 && rule4 && rule5){
            $("button[data-mode='password']").prop('disabled', false);
            $(".password-info-box").addClass('d-none');
            $(".password-success-box").removeClass('d-none');
        } else {
            $("button[data-mode='password']").prop('disabled', true);
            $(".password-info-box").removeClass('d-none');
            $(".password-success-box").addClass('d-none');
        }

    });
}

function showhidePassword(status, login, element)
{
    var change = "password";
    
    if (element.hasClass('hidepassword')){
        if (!status){
            change = "text";
            element.removeClass('d-none');
            element.parent().find('a.showpassword').addClass('d-none');
        } else {
            element.parent().find('a.showpassword').removeClass('d-none');
            element.addClass('d-none');
        }    
    } else if (element.hasClass('showpassword')){
        if (!status){
            change = "text";
            element.parent().find('a.hidepassword').removeClass('d-none');
            element.addClass('d-none');
        } else {
            element.removeClass('d-none');
            element.parent().find('a.hidepassword').addClass('d-none');
        }
    }

    var password_element = element.parent().parent().find('input[data-mode="password"]');

    rep = $("<input type='" + change + "' />")
                .attr("data-mode", password_element.attr("data-mode"))
                .attr("name", password_element.attr("name"))
                .attr('class', password_element.attr('class'))
                .val(password_element.val())
                .insertBefore(password_element);
    
    password_element.remove();
    password_element = rep;
    
    if (!login)
        initChackPassword();
}




$(document).ready(function(){
    
    initChackPassword();

    $('.showpassword').on('click', function(){
        var element = $(this);
        showhidePassword(
            false,
            false,
            element
        );
    });

    $('.hidepassword').on('click', function(){
        var element = $(this);
        showhidePassword(
            true,
            false,
            element
        );
    });
});