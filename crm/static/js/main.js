(function ($) {
    
    "use strict";

    
    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');

    $('.validate-form').on('submit',function(){
        var check = true;

        for(var i=0; i<input.length; i++) {
            if(validate(input[i]) == false){
                showValidate(input[i]);
                check=false;
            }
        }
        

        return check;
    });


    $('.validate-form .input100').each(function(){
        $(this).focus(function(){
           hideValidate(this);
        });
    });

    function validate (input) {
        if($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        }
        else {
            if($(input).val().trim() == ''){
                return false;
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }
    
    

})

        $("#p1").click(function(){
            username = $("#p2").val();
            password = $("#p3").val();
            $.ajax({
                type: "GET",
                url: "/validate/user",
                data: {
                    'username': username,
                    'password': password
                },
                dataType: 'Json',
                success: function(res){
                    console.log(res.data);
                    if (res.data ==false){
                        alert("Username and Password are wrong");
                    }
                }
            });
        });


  function myFunction() {
       document.getElementById("myForm").reset();
   }
   function alphaOnly(event) {
       var key = event.keyCode;
       return ((key >= 65 && key <= 90) || key == 8);
   };