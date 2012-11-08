var nav = new ui.nav($('.nav'));

$(function(){
    $('#page_holder').pagify({
        pages: {
            'main' : 'pages/main',
            'issues_my' : 'pages/issues/my',
            'issues_open' : 'pages/issues/open',
            'issues_delivered' : 'pages/issues/delivered',
            'issues_all' : 'pages/issues/all',
            'milestones' : 'pages/issues/milestones'
        },
        animation: 'fadeIn',
        'default': 'main',
        cache: false
    });
});
