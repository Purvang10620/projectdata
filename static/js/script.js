/* =====================================
                Preloader
======================================== */
$(window).on('load', function () { //make sure that whole site is loaded
    $('#status').fadeOut();
    $('#preloader').delay(350).fadeOut('slow');
});

/* =====================================
                Team
======================================== */
$(function () {
    $("#team-members").owlCarousel({
        items: 2,
        autoplay: true,
        smartSpeed: 700,
        loop: true,
        autoplayHoverPause: true,
        nav: true,
        dots: false,
        navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
        responsive: {
            // breakpoint from 0 up
            0: {
                items: 1
            },
            // breakpoint from 480 up
            480: {
                items: 2
            }
        }
    });
});

/* =====================================
                Progress Bar
======================================== */
$(function () {

    $("#progress-elements").waypoint(function () {

        $(".progress-bar").each(function () {
            $(this).animate({
                width: $(this).attr("aria-valuenow") + "%"
            }, 1000);
        });
        this.destroy();
    }, {
        offset: 'bottom-in-view'
    });

});

/* =====================================
                Responsive Tabs
======================================== */
$(function () {

    $("#services-tabs").responsiveTabs({
        animation: 'slide'
    });
});

/* =====================================
                Portfolio
======================================== */
$(window).on('load', function () {

    //Initialize Isotope
    $("#isotope-container").isotope({});

    //filter items on button click
    $("#isotope-filters").on('click', 'button', function () {

        //get filter value
        var filtervalue = $(this).attr('data-filter');

        //filter portfolio
        $("#isotope-container").isotope({
            filter: filtervalue
        });

        //active button
        $("#isotope-filters").find('.active').removeClass('active');
        $(this).addClass('active');
    });

});

/* =====================================
                Magnifier
======================================== */
$(function () {
    $("#portfolio-wrapper").magnificPopup({
        delegate: 'a', //child items selector, by clicking on it popup will open
        type: 'image',
        gallery: {
            enabled: true
        }
    });
});

/* =====================================
                Testimonials
======================================== */
$(function () {
    $("#testimonial-slider").owlCarousel({
        items: 1,
        autoplay: false,
        smartSpeed: 700,
        loop: true,
        autoplayHoverPause: true,
        nav: true,
        dots: false,
        navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>']
    });
});

/* =====================================
                Stats
======================================== */
$(function () {
    $(".counter").counterUp({
        delay: 10,
        time: 2000
    });
});

/* =====================================
                Clients
======================================== */
$(function () {
    $("#clients-list").owlCarousel({
        items: 6,
        autoplay: false,
        smartSpeed: 700,
        loop: true,
        autoplayHoverPause: true,
        nav: true,
        dots: false,
        navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>']
    });
});

/* =====================================
                Google Map
======================================== */
$(window).on('load', function () {

    // Map Variables
    var addressString = 'Cambay Grand, Thaltej, Ahmedabad, Gujarat';
    var myLating = {
        lat: 23.059080,
        lng: 72.522894
    };

    //1. Render Google Map
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 11,
        center: myLating
    });

    //2. Add Marker
    var marker = new google.maps.Marker({
        position: myLating,
        map: map,
        title: "Click To See Address"
    });

    //3. Add Info Window
    var infowindow = new google.maps.InfoWindow({
        content: addressString
    });

    //Show Info window when user clicks marker
    marker.addListener('click', function () {
        infowindow.open(map, marker);
    });
});

/* =====================================
                Navigation
======================================== */
/* Show & Hide White Navigation */
$(function () {

    // Show/Hide nav on page load
    showHideNav();

    $(window).scroll(function () {

        // Show/Hide nav window's scroll
        showHideNav();

    });

    function showHideNav() {

        if ($(window).scrollTop() > 50) {

            //Show white nav
            $("nav").addClass("white-nav-top");

            //Show Dark logo
            $(".navbar-brand img").attr("src", "img/logo/logo-dark.png")

            //Show back to top button
            $("#back-to-top").fadeIn();

        } else {

            //Hide white nav
            $("nav").removeClass("white-nav-top");

            //Show logo
            $(".navbar-brand img").attr("src", "img/logo/logo.png")

            //Hide back to top button
            $("#back-to-top").fadeOut();
        }
    }
});

/* Smooth Scrolling */
$(function () {
    $("a.smooth-scroll").click(function (event) {
        event.preventDefault();

        //get section id like #about, #services, #work, #team and etc.
        var section_id = $(this).attr("href");

        $("html, body").animate({
            scrollTop: $(section_id).offset().top - 64
        }, 1250, "easeInOutExpo");
    });
});