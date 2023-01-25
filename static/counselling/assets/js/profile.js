jQuery(function ($) {
    var $inputs = $('input[name=percentage],input[name=grade]');
    $inputs.on('input', function () {
        // Set the required property of the other input to false if this input is not empty.
        $inputs.not(this).prop('required', !$(this).val().length);
    });
});