$(document).ready(function() {
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



	var a;
	var code = document.getElementById("code");
	var add = document.getElementById("ad");
	var pc = document.getElementById("pc");
	$("#cu_nameq").change(function(){
		a = $(this).val();
		$.ajax({
        type: 'GET',
        url: '/get/quotation',
        data : {

            'customer_id': a
            // 'time': $('#time1').val(),
            // 'title':$('#description1').val()
        },
        dataType: 'json',
        success: function(response){
            // console.log(response);
            code.value = response.data;
            add.value = response.address;
            $("name").val(response.name);
        }
    });
	});
	$("#prnq1").change(function(){
		a = $(this).val();
        // console.log(a);
		$.ajax({
        type: 'GET',
        url: '/get/product',
        data : {

            'p_id': a
            // 'time': $('#time1').val(),
            // 'title':$('#description1').val()
        },
        dataType: 'json',
        success: function(response){
            // console.log(response);
            pcoq1.value = response.data;
            price11.value = response.price
            
        }
    });
	});
    $("#prnq2").change(function(){
        a = $(this).val();
        // console.log(a);
        $.ajax({
        type: 'GET',
        url: '/get/product',
        data : {

            'p_id': a
            // 'time': $('#time1').val(),
            // 'title':$('#description1').val()
        },
        dataType: 'json',
        success: function(response){
            // console.log(response);
            pcoq2.value = response.data;
            price12.value = response.price
            
        }
    });

    });
    $("#prnq3").change(function(){
        a = $(this).val();
        // console.log(a);
        $.ajax({
        type: 'GET',
        url: '/get/product',
        data : {

            'p_id': a
            // 'time': $('#time1').val(),
            // 'title':$('#description1').val()
        },
        dataType: 'json',
        success: function(response){
            // console.log(response);
            pcoq3.value = response.data;
            price13.value = response.price
            
        }
    });
        
    });
    $("#prnq4").change(function(){
        a = $(this).val();
        // console.log(a);
        $.ajax({
        type: 'GET',
        url: '/get/product',
        data : {

            'p_id': a
            // 'time': $('#time1').val(),
            // 'title':$('#description1').val()
        },
        dataType: 'json',
        success: function(response){
            // console.log(response);
            pcoq4.value = response.data;
            price14.value = response.price
            
        }
    });
        
    });
    $("#prnq5").change(function(){
        a = $(this).val();
        // console.log(a);
        $.ajax({
        type: 'GET',
        url: '/get/product',
        data : {

            'p_id': a
            // 'time': $('#time1').val(),
            // 'title':$('#description1').val()
        },
        dataType: 'json',
        success: function(response){
            // console.log(response);
            pcoq5.value = response.data;
            price15.value = response.price
            
        }
    });
        
    });
    $("#prnq6").change(function(){
        a = $(this).val();
        // console.log(a);
        $.ajax({
        type: 'GET',
        url: '/get/product',
        data : {

            'p_id': a
            // 'time': $('#time1').val(),
            // 'title':$('#description1').val()
        },
        dataType: 'json',
        success: function(response){
            // console.log(response);
            pcoq6.value = response.data;
            price16.value = response.price
            
        }
    });
        
    });
    $("#prnq7").change(function(){
        a = $(this).val();
        // console.log(a);
        $.ajax({
        type: 'GET',
        url: '/get/product',
        data : {

            'p_id': a
            // 'time': $('#time1').val(),
            // 'title':$('#description1').val()
        },
        dataType: 'json',
        success: function(response){
            // console.log(response);
            pcoq7.value = response.data;
            price17.value = response.price
            
        }
    });
        
    });
    $("#prnq8").change(function(){
        a = $(this).val();
        // console.log(a);
        $.ajax({
        type: 'GET',
        url: '/get/product',
        data : {

            'p_id': a
            // 'time': $('#time1').val(),
            // 'title':$('#description1').val()
        },
        dataType: 'json',
        success: function(response){
            // console.log(response);
            pcoq8.value = response.data;
            price18.value = response.price
            
        }
    });
        
    });
    $("#prnq9").change(function(){
        a = $(this).val();
        // console.log(a);
        $.ajax({
        type: 'GET',
        url: '/get/product',
        data : {

            'p_id': a
            // 'time': $('#time1').val(),
            // 'title':$('#description1').val()
        },
        dataType: 'json',
        success: function(response){
            // console.log(response);
            pcoq9.value = response.data;
            price19.value = response.price
            
        }
    });
        
    });
    $("#prnq10").change(function(){
        a = $(this).val();
        // console.log(a);
        $.ajax({
        type: 'GET',
        url: '/get/product',
        data : {

            'p_id': a
            // 'time': $('#time1').val(),
            // 'title':$('#description1').val()
        },
        dataType: 'json',
        success: function(response){
            // console.log(response);
            pcoq10.value = response.data;
            price110.value = response.price
            
        }
    });
        
    });


});
