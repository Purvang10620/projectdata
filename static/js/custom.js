$('#main').click(function(){
    $('.main-content').load('main');
})

$('#addarticle').click(function(){
    $('.main-content').load('addarticle');
})

$('#profile').click(function(){
    $('.main-content').load('profile');
})

$('#logout').click(function(){
    $('.top').load('logout');
})

$('#setting').click(function(){
    $('.js-scrollbar1').load('settings');
})

$('#back').click(function(){
    $('.js-scrollbar1').load('sidebar');
})

