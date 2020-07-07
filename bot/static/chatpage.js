$(document).ready(function(){
    var $target = $('.msgbox'); 
    $target.animate({scrollTop: $target.height()});
function sendMsg(){
    let msg = $('#msg').val();
    $('#msg').val('');
    let new_div = '<div class= "message sent">' + msg + '</div>';
    
    $('.msgbox').append(new_div);
    $('.msgbox').scrollTop($('.msgbox').height());
    return msg;
}
function receieveMsg(msg){
    
    let new_div = '<div class= "message recieved">' + msg + '</div>';
    
    $('.msgbox').append(new_div);
    $('.msgbox').scrollTop($('.msgbox').height());
}

function getResponse(message){
    $.ajax({
        csrfmiddlewaretoken: "{{ csrf_token }}",
        url:'/bot/getResponse',
        type: 'POST',
        data: {
            msg : message 
        }, 
        success: function(response){
            resp = response.response;
            receieveMsg(resp);
            $('.msgbox').scrollTop($('.msgbox').height());
        }
    })

}
    
$('#msgform').submit(function(e){
    e.preventDefault();
    let msg = sendMsg();
    getResponse(msg);
    


})


})