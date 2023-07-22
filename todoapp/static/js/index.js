$(document).ready(function () {

    //Date fild code===========================
    $("#datepicker").datepicker({
        autoclose: true,
        todayHighlight: true,
    });

    // form validation jquery====================

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

});
