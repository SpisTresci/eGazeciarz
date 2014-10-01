$(function() {
    $('form').submit(function(e) {
        var form = $(this);
        $('button').attr('disabled', true);
        $.ajax({
            type : form.attr('method'),
            url: form.attr('action'),
            data : form.serialize(),
            success: function(data) {
                var container = form.parent();
                container.html(data);
                $('button').attr('disabled', false);
            },
            error: function(data) {
                form.parent().html('Ups, coś poszło nie tak.');
                $('button').attr('disabled', false);
            }
        });
        return false;
    });
});
