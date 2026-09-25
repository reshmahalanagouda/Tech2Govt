/*
 Author : theme_ocean
 Template Name: Purdue - Education HTML Template
 Version : 1.0
*/
(function($) {
    'use strict';
    jQuery(document).on('ready', function(){
        jQuery(window).on('load',function() {
            setTimeout(function(){
                $('.preloaders').fadeToggle();
            }, 1500);
        });
        $(".mobile_menu").simpleMobileMenu({ "menuStyle": "slide" });
        $(window).on('scroll', function() {
            if ($(this).scrollTop() > 100) { $('.main_header').addClass('sticky'); }
            else { $('.main_header').removeClass('sticky'); }
        });
    });
    // SAFE SLIDER - no more classList crash
    let slides = document.querySelectorAll('.slide');
    function addActive(slide){
        if(!slide ||!slide.classList) return;
        try{ slide.classList.add('active'); }catch(e){}
    }
    function removeActive(slide){
        if(!slide ||!slide.classList) return;
        try{ slide.classList.remove('active'); }catch(e){}
    }
    try{
        if(slides && slides.length > 0){
            addActive(slides[0]);
            setInterval(function () {
                let activeIndex = -1;
                for (let i = 0; i < slides.length; i++) {
                    if (slides[i].classList.contains('active')) { activeIndex = i; break; }
                }
                if(activeIndex === -1) activeIndex = 0;
                let nextIndex = (activeIndex + 1) % slides.length;
                setTimeout(removeActive, 350, slides[activeIndex]);
                addActive(slides[nextIndex]);
            }, 3500);
        }
    }catch(e){ console.log('slider safe'); }
})(jQuery);
