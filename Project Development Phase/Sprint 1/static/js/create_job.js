$(document).on('submit', '#job_creation_form', function (e){
    e.preventDefault();
    const job_creation_form = $(this).serialize();
    $.ajax({
        type : 'POST',
        url : '/create_job',
        data : job_creation_form,
        success : function(response) {
            console.log(response);
            alert("Working");
        }
    })
});