$(document).ready(function() {
    
    $("#c_name").change(function (){
        // var code = $(this).val();
        var a = document.getElementById("c_name").value;
        // var b = document.getElementById("p1");
        console.log(a);
        $.ajax({
            type: 'GET',
            url:'/api/customer/data',
            data:{
                'customer_id':a
            },
            dataType: 'json',
            success: function(response){
                console.log(response);
                // console.log(response.data[0].item_name_id);
               customer_code.value = response.data;
               city.value = response.city;
               country.value = response.country;
               state.value = response.state;
               postal_code.value = response.postal_code;

               if (response.previous_data){
                c = '';
                for (i = 0; i < response.previous_data.length; i++){
                    c = c +'<option>'+ response.previous_data[i] +'</option>'
                }
                
                $("#product_name").prepend(c);
               }
    
            }
        });
        });
    $("#p_name").change(function (){
    // var code = $(this).val();
    var a = document.getElementById("p_name").value;
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
            // console.log(response.data[0].item_name_id);
           p_code.value = response.data;
           pack.value = response.packaging;
           uom_id.value = response.uom;
           

        }
    });

});
    $("#c_pay").change(function (){
    var code = $(this).val();
    console.log(code);
    // var a = document.getElementById("c_pay").value;
    // console.log("hello");
    // var b = document.getElementById("p1");
    // console.log(a);
    $.ajax({
        type: 'GET',
        url:'/pay/order/track',
        data:{
            'customer_id':code
        },
        dataType: 'json',
        success: function(response){
            console.log(response);
            if (response.codes.length>0){
                c = '';
                for (i = 0; i < response.codes.length; i++){
                    c = c +'<option value="'+ response.codes[i] +'">'+ response.names[i], response.codes[i] +'</option>'
                }
                
                $("#product_pay").prepend(c);
               }

        }
    });

});
})
    