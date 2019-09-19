$(document).ready(function() {
    $("#target").click(function (){
        var code = document.getElementById("l2").value;
        var user = document.getElementById("l1").value;
        console.log(code);
        $.ajax({
            type: 'GET',
            url:'/api/target/add',
            data:{
                'amount':code,
                'user':user
            },
            dataType: 'json',
            success: function(response){
                if (response.data){
                   alert("Target saved..!!")
                }
                
    
            }
        });
    });

    $("#checkemail").change(function(){
            username = $("#checkemail").val();
            $.ajax({
                type: "GET",
                url: "/validate/user",
                data: {
                    'mail': username
                },
                dataType: 'Json',
                success: function(res){
                    console.log(res.check);
                    if (res.check == true){ 
                        $('#checkemail').parent().after("<div class='validation' style='color:red;margin-bottom: 20px;'>User Is already exist</div>")
                        $('#checkp1').attr('disabled', true);
                    }
                    else{
                        $('#checkp1').attr('disabled', false);
                    }
                }
            });
        });
});