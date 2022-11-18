$(document).on('submit', '#login_form', function (e){
    e.preventDefault();
    //  Custom Validators
    // $.validator.addMethod('uppercase',
    //     function(value) {
    //         return /(?=.*[A-Z])/.test(value)
    //     },
    //     'Password must contain one UpperCase character');
    //
    // $.validator.addMethod('lowercase',
    //     function (value) {
    //         return /(?=.*[a-z])/.test(value)
    //     },
    //     'Password must contain one LowerCase character');
    //
    // $.validator.addMethod('digit',
    //     function (value) {
    //         return /(?=.*[0-9])/.test(value)
    //     },
    //     'Password must contain one numeric value');
    //
    // $.validator.addMethod('special_char',
    //     function (value) {
    //         return /(?=.*[!.@])/.test(value)
    //     },
    //     'Password must contain one special character');
    //
    // // Form-1 Validate Rules
    // $('#form-1').validate({
    //     focusCleanup: true,
    //     focusInvalid: false,
    //     ignore: '.ignore',
    //     debug: true,
    //
    //     // Rules
    //     rules: {
    //         email: {
    //             required: true,
    //             email: true
    //         },
    //         password: {
    //             required: true,
    //             uppercase: true,
    //             lowercase: true,
    //             digit: true,
    //             special_char: true,
    //             minlength: 8,
    //         },
    //         confirm: {
    //             required: true,
    //             minlength: 8,
    //             equalTo: '#Password',
    //         },
    //     },
    //
    //     errorPlacement: function (error, element){
    //         const ele = $(element).attr("id");
    //         error.insertAfter('#'+ele+'Validate');
    //     },
    //
    //     // Error Message
    //     messages: {
    //         email: {
    //             email: 'Enter a valid email address',
    //         },
    //         password: {
    //             minlength: 'Your password must contain at least 8 characters',
    //         },
    //         confirm: {
    //             equalTo: 'Confirm Password doesn\'t match Password',
    //         },
    //     },
    // });
    // // Validate Call
    // $('#form-1').validate();

    // Submit Form if form is valid and move to Next Form
    // Form Data
    const form1 = new FormData($('#login_form')[0]);
    const form = Object.fromEntries(form1.entries());
    console.log(form)
    $.ajax({
        type: 'POST',
        url: '/login',
        data: JSON.stringify(form),
        contentType: 'application/json',
        success: function (response) {

        }
    });
});