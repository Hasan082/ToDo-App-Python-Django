$(document).ready(function () {

    //Date field code=============================================
    $("#datepicker").datepicker({
        autoclose: true,
        todayHighlight: true,
    });

    // form validation jquery=====================================

    let formId = $("#taskform");

    formId.on("submit", function(event) {
        event.preventDefault();

        var taskTitle = $("#txtName").val();
        var taskDescription = $("#txtMsg").val();
        var dateCompleted = $("#txtDate").val();

        if (taskTitle.trim() === '') {
            alert("Please enter the Task Title.");
            return;
        }

        if (taskDescription.trim() === '') {
            alert("Please enter the Task Description.");
            return;
        }

        if (dateCompleted.trim() === '') {
            alert("Please select the Date Completed.");
            return;
        }

        formId[0].submit();
    });

    //manually remove the alert message======================================
    // $('.alert').on('click', function(){
    //     $(this).remove();
    // });
    
    //if manually not deleted, after 10sec alert emassge remove automatically
    // setTimeout(function(){
    //     $('.alert').remove();
    // }, 10000)


});
