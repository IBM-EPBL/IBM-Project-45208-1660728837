$(document).on('submit', '#job_creation_form', function (e){
    e.preventDefault();
    const job_creation_form = $(this).serialize();
    $('#create_job').modal('hide');
    swal({
        title: "Posting Job",
        text: "Wait for a second...",
        icon: "info",
        closeOnClickOutside: false,
        button: false,
    });
    $.ajax({
        type : 'POST',
        url : '/create_job',
        data : job_creation_form,
        success : function(response) {
            $("#job_creation_form")[0].reset();
            $('#job_offer_table').html(response);
            swal({
                title: "Posted",
                text: "Job successfully posted",
                icon: "success",
                button: "Done",
            });
        }
    })
});