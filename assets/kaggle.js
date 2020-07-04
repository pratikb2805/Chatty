$("#send").click(function() {

    var url = $('#send').attr('action'); // the script where you handle the form input.

    $.ajax({
           type: "POST",
           url: url,
           data: $("#send").serialize(), // serializes the form's elements.
           success: function(data)
           {
               alert(data); // show response from the php script.
           }
         });

    return false; // avoid to execute the actual submit of the form.
});
