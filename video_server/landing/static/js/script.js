$(document).ready(function(){


    if(document.location.href.indexOf("send-request",0) != -1){
        $(".popup").css("display","block");
    }

    $(function(){
        $('#phone').each(function(){
            $(this).inputmask("9 (999) 999-99-99");
        });
//
        var form = $('.request'),
        btn = form.find('.submit-bt');

        setInterval(function(){
            var pmc = $('#phone');
            if ( (pmc.val().indexOf("_") != -1) || pmc.val() == '' ) {
              pmc.addClass('empty-field');
            } else {
                pmc.removeClass('empty-field');
            }

            var sizeEmpty = form.find('.empty-field').size();

            if(sizeEmpty > 0){
            if(btn.hasClass('disabled')){
              return false
            } else {
              btn.addClass('disabled')
            }
            } else {
            btn.removeClass('disabled')
            }

            },200);

            btn.click(function(){
            if($(this).hasClass('disabled')){
                $(".request p:nth-child(7)").text("Введен некорректный телефон");
                return false
            } else {
                form.submit();
            }
        });

    });

    $(".open-popup").click(function(){
        $(".popup").css("display","block");
    });

    $("#close").click(function(){
        $(".popup").css("display","none");
    });
});