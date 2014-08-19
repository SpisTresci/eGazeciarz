$(function() {
    var form = $('#change_password_form');
    form.submit(function(e) {
        console.log('clicked');
        $('#submit_change_password_form').attr('disabled', true);
        $('#ajaxwrapper').load(
            form.attr('action') + '#ajaxwrapper',
            form.serializeArray(),
            function(responseText, responseStatus) {
                $('#submit_change_password_form').attr('disabled', false);
            }
            );
        e.preventDefault();
    });
});
