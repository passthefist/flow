(function(ns) {

    var form = function(root, url) {
        var self = this;

        root.find('.submit').on('click', function(e) {
            e.preventDefault();

            var data = {};

            root.find('input').each(function(){
                var el = $(this);
                var name = el.attr('name');
                var val = el.val();

                data[name] = val;
            });

            $.post(url,data, function(resp, stat, o) {
                if(self.callback) {
                    self.callback.call(self,resp)
                }
            });
        });

        self.errors = function(errs) {
            if ($.isArray(errs)) {
                var el = root.find(".errors");
                el.empty();

                $.each(errs, function(idx,err) {
                    var div = $('<div class="alert alert-error"><button type="button" class="close" data-dismiss="alert">×</button></div>')
                    .append(err);
                    el.append(div);
                });
            }
        }
    };

    ns.ajaxForm = {
        form : form
    };
})(window);
