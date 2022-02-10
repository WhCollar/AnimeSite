/* Для активации лайка */
$(function(){
    $('.like-toggle').click(function(){
        $(this).toggleClass('like-active');
        $(this).next().toggleClass('hidden-like-text');
    });
});
/* END Для активации лайка */