(function(ns) {
    var navBar = function(root) {
        var nav = this;

        console.log(root);

        nav.page = {};
        nav.actions = {};

        nav.current = null;

        nav.execAction = function(action) {
            action = nav.actions[action];
            if (action) {
                action.call();
            }
        };

        nav.execPage = function(page) {
            page = nav.actions[page];
            if (page) {
                page.call();
            }
        };

        root.find('li').on('click', function (){
            var el = $(this);
            var page = el.data('page');

            $('.nav .active').removeClass('active');
            el.addClass('active');

            if (nav.current) {
                nav.current.hide();
            }

            nav.execPage(page);
        });

        root.find('.dropdown-menu li').on('click', function() {
            var el = $(this);
            var action = el.find('a').data('action');
            nav.execAction(action);
        });
    }

    ns.ui = {
        nav: navBar
    };
})(window);

