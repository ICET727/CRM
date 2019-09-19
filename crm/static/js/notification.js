$(document).ready(function() {
    $("#target").click(function (){
        console.log(code);
        $.ajax({
            type: 'GET',
            url:'/get/notification',
            dataType: 'json',
            success: function(response){
                if (response.data){
                   alert("Target saved..!!")
                }
                
    
            }
        });
    });
});