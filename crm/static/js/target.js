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



    $("#email1").change(function (){
    var email = $(this).val();
    var password = document.getElementById("pass1").value;
    
    if (password=='' || email==''){
                console.log();
    }
    else{
        $.ajax({
        type: 'GET',
        url:'/mail/check',
        data:{
            'email':email,
            'password':password
        },
        dataType: 'json',
        success: function(response){
            // console.log(response);
            if (response.data==false){
            $('#email1').parent().after("<div class='validation' id='em1' style='color:red;margin-bottom: 20px;'>Email and Password are not correct..</div>")
            }
            if (response.data==true){
            $("#em1").hide();
        }
        }
    });

    }
    

});
    $("#pass1").change(function (){
    var password = $(this).val();
    var email = document.getElementById("email1").value;
    if (password=='' || email==''){
        console.log("");
    }
    else{
        $.ajax({
        type: 'GET',
        url:'/mail/check',
        data:{
            'email':email,
            'password':password
        },
        dataType: 'json',
        success: function(response){
            // console.log(response);
            if (response.data==false){
            $('#pass1').parent().after("<div class='validation' id='em1' style='color:red;margin-bottom: 20px;'>Email and Password are not correct..</div>")
        }
        if (response.data==true){
            $("#em1").hide();
        }
        }
    });

    }
    

});
});