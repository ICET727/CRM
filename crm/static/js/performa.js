$(document).ready(function() {
    
    $("#prn1").change(function (){
    // var code = $(this).val();
    var a = document.getElementById("prn1").value;
    // var b = document.getElementById("p1");
    console.log(a);
    $.ajax({
        type: 'GET',
        url:'/get/product',
        data:{
            'p_id':a
        },
        dataType: 'json',
        success: function(response){
            console.log(response);
            pco1.value = response.data;
            rate1.value = response.price;
            

           

        }
    });

});

    // product 2  js
    $("#prn2").change(function (){
    // var code = $(this).val();
    var a = document.getElementById("prn2").value;
    // var b = document.getElementById("p1");
    console.log(a);
    $.ajax({
        type: 'GET',
        url:'/get/product',
        data:{
            'p_id':a
        },
        dataType: 'json',
        success: function(response){
            console.log(response.solubility);
           pco2.value = response.data;
            rate2.value = response.price;

        }
    });
});

// product 3  js
    $("#pcn3").change(function (){
    // var code = $(this).val();
    var a = document.getElementById("pcn3").value;
    // var b = document.getElementById("p1");
    console.log(a);
    $.ajax({
        type: 'GET',
        url:'/get/product',
        data:{
            'p_id':a
        },
        dataType: 'json',
        success: function(response){
            console.log(response);
            pco3.value = response.data;
            rate3.value = response.price;

           

        }
    });
});

    // product 4  js
    $("#pcn4").change(function (){
    // var code = $(this).val();
    var a = document.getElementById("pcn4").value;
    // var b = document.getElementById("p1");
    console.log(a);
    $.ajax({
        type: 'GET',
        url:'/get/product',
        data:{
            'p_id':a
        },
        dataType: 'json',
        success: function(response){
            console.log(response);
           pco4.value = response.data;
            rate4.value = response.price;
        }
    });
});


 // product 5  js
    $("#pcn5").change(function (){
    // var code = $(this).val();
    var a = document.getElementById("pcn5").value;
    // var b = document.getElementById("p1");
    console.log(a);
    $.ajax({
        type: 'GET',
        url:'/get/product',
        data:{
            'p_id':a
        },
        dataType: 'json',
        success: function(response){
            pco5.value = response.data;
            rate5.value = response.price;
        }
    });
});


 // product 6  js
    $("#pcn6").change(function (){
    // var code = $(this).val();
    var a = document.getElementById("pcn6").value;
    // var b = document.getElementById("p1");
    console.log(a);
    $.ajax({
        type: 'GET',
        url:'/get/product',
        data:{
            'p_id':a
        },
        dataType: 'json',
        success: function(response){
          pco6.value = response.data;
            rate6.value = response.price;
        }
    });
});

 // product 7  js
    $("#pcn7").change(function (){
    // var code = $(this).val();
    var a = document.getElementById("pcn7").value;
    // var b = document.getElementById("p1");
    console.log(a);
    $.ajax({
        type: 'GET',
        url:'/get/product',
        data:{
            'p_id':a
        },
        dataType: 'json',
        success: function(response){
           pco7.value = response.data;
            rate7.value = response.price;
        }
    });
});

 // product 8  js
    $("#pcn8").change(function (){
    // var code = $(this).val();
    var a = document.getElementById("pcn8").value;
    // var b = document.getElementById("p1");
    console.log(a);
    $.ajax({
        type: 'GET',
        url:'/get/product',
        data:{
            'p_id':a
        },
        dataType: 'json',
        success: function(response){
            pco8.value = response.data;
            rate8.value = response.price;
        }
    });
});


 // product 9  js
    $("#pcn9").change(function (){
    // var code = $(this).val();
    var a = document.getElementById("pcn9").value;
    // var b = document.getElementById("p1");
    console.log(a);
    $.ajax({
        type: 'GET',
        url:'/get/product',
        data:{
            'p_id':a
        },
        dataType: 'json',
        success: function(response){
            pco9.value = response.data;
            rate9.value = response.price;
        }
    });
});


 // product 10  js
    $("#pcn10").change(function (){
    // var code = $(this).val();
    var a = document.getElementById("pcn10").value;
    // var b = document.getElementById("p1");
    console.log(a);
    $.ajax({
        type: 'GET',
        url:'/get/product',
        data:{
            'p_id':a
        },
        dataType: 'json',
        success: function(response){
            pco10.value = response.data;
            rate10.value = response.price;
        }
    });
});
    
})
    