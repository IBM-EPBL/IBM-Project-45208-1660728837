$(document).on('submit', '#job_request_form', function (e){
    e.preventDefault();
    const job_request_form = $(this).serialize();
    swal({
        title: "Requesting Job",
        text: "Wait for a second...",
        icon: "info",
        closeOnClickOutside: false,
        button: false,
    });
    $.ajax({
        type : 'POST',
        url : '/request_job',
        data : job_request_form,
        success : function(response) {
            $("#job_request_form")[0].reset();
            $('#job_offer_table').html(response);
            swal({
                title: "Requested",
                text: "Job successfully requested",
                icon: "success",
                button: "Done",
            });
        }
    })
});