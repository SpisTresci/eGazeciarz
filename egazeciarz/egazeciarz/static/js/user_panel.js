$(function() {
    $('form').submit(function(e) {
        console.log($(this));
        $('button').attr('disabled', true);
        $(this).load(
            $(this).attr('action'),
            $(this).serialize(),
            function(responseText, responseStatus) {
                $('button').attr('disabled', false);
            }
            );
        e.preventDefault();
    });
});
