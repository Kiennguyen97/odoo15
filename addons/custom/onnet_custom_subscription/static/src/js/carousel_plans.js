var screenSize= $( window ).width();

//check item > 4 show slide
if($('.plans_col').length > 4){
    $('.owl-carousel').owlCarousel({
        loop: false,
        margin:10,
        nav: false,
        responsive:{
            0:{
                items: 1
            },
            480:{
                items: 2
            },
            768:{
                items: 2
            },
            992:{
                items: 4
            }
        }
    })
}

//check if item < 5 và windown width size < 1200 show slide else do not show slides
if(screenSize < 1200 && $('.plans_col').length < 5) {
    $('.owl-carousel').owlCarousel({
        loop: false,
        margin:10,
        nav: false,
        responsive:{
            0:{
                items: 1
            },
            480:{
                items: 2
            },
            768:{
                items: 2
            },
            992:{
                items: 3
            }
        }
    })

}


