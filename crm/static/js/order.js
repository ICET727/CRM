$(document).ready(function() {
    $("#c_name").change(function (){
        // var code = $(this).val();
        var a = document.getElementById("c_name").value;
        // var b = document.getElementById("p1");
        // console.log(a);
        $.ajax({
            type: 'GET',
            url:'/api/customer/order',
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
               street.value = response.street;
               f_address.value = response.f_address;
               g1.value = response.gst;
               

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
            console.log(response.solubility);
            // console.log(response.data[0].item_name_id);
            $('#uom').val(response.uom);
            $('#sol').val(response.solubility);
            
           // p_code.value = response.data;
           pup.value = response.price;
           // pack.value = response.packaging;
           // uom_id.value = response.uom;

           

        }
    });

});

    // product 2  js
    $("#p_name2").change(function (){
    // var code = $(this).val();
    var a = document.getElementById("p_name2").value;
    if (a.length>0){
        $("#quantity2").prop("required",true);
        $("#pup2").prop("required",true);
        $("#uom2").prop("required",true);
        $("#solu2").prop("required",true);
    }
    else{
        $("#quantity2").prop("required",false);
        $("#pup2").prop("required",false);
        $("#uom2").prop("required",false);
        $("#solu2").prop("required",false);
    };
    // console.log(a);
    $.ajax({
        type: 'GET',
        url:'/get/product',
        data:{
            'p_id':a
        },
        dataType: 'json',
        success: function(response){
            // console.log(response.solubility);
            // console.log(response.data[0].item_name_id);
            $('#uom2').val(response.uom);
            $('#solu2').val(response.solubility);
            
           // p_code.value = response.data;
           pup2.value = response.price;
           // pack.value = response.packaging;
           // uom_id.value = response.uom;

           

        },
        error: function(){
            $('#uom2').val('');
            $('#solu2').val('');
            $('#pup2').val('');
        }
    });
});

// product 3  js
    $("#p_name3").change(function (){
    // var code = $(this).val();
    var a = document.getElementById("p_name3").value;
    // var b = document.getElementById("p1");
    if (a.length>0){
        $("#quantity3").prop("required",true);
        $("#pup3").prop("required",true);
        $("#uom3").prop("required",true);
        $("#sol3").prop("required",true);
        $("#packaging3").prop("required",true);
    }
    else{
        $("#quantity3").prop("required",false);
        $("#pup3").prop("required",false);
        $("#uom3").prop("required",false);
        $("#sol3").prop("required",false);
        $("#packaging3").prop("required",false);
    };
    // console.log(a);
    $.ajax({
        type: 'GET',
        url:'/get/product',
        data:{
            'p_id':a
        },
        dataType: 'json',
        success: function(response){
            // console.log(response);
            // console.log(response.data[0].item_name_id);
            $('#uom3').val(response.uom);
            $('#sol3').val(response.solubility);
            
           // p_code.value = response.data;
           pup3.value = response.price;
           // pack.value = response.packaging;
           // uom_id.value = response.uom;

        },
        error: function(){
            $('#uom3').val('');
            $('#sol3').val('');
            $('#pup3').val('');
        }
    });
});

    // product 4  js
    $("#p_name4").change(function (){
    // var code = $(this).val();
    var a = document.getElementById("p_name4").value;
    // var b = document.getElementById("p1");
    if (a.length>0){
        $("#quantity4").prop("required",true);
        $("#pup4").prop("required",true);
        $("#uom4").prop("required",true);
        $("#sol4").prop("required",true);
        $("#packaging4").prop("required",true);
    }
    else{
        $("#quantity4").prop("required",false);
        $("#pup4").prop("required",false);
        $("#uom4").prop("required",false);
        $("#sol4").prop("required",false);
        $("#packaging4").prop("required",false);
    };
    // console.log(a);
    $.ajax({
        type: 'GET',
        url:'/get/product',
        data:{
            'p_id':a
        },
        dataType: 'json',
        success: function(response){
            // console.log(response);
            // console.log(response.data[0].item_name_id);
            $('#uom4').val(response.uom);
            $('#sol4').val(response.solubility);
            
           // p_code.value = response.data;
           pup4.value = response.price;
           // pack.value = response.packaging;
           // uom_id.value = response.uom;

           

        },
        error: function(){
            $('#uom4').val('');
            $('#sol4').val('');
            $('#pup4').val('');
        }
    });
});


 // product 5  js
    $("#p_name5").change(function (){
    // var code = $(this).val();
    var a = document.getElementById("p_name5").value;
    // var b = document.getElementById("p1");
    if (a.length>0){
        $("#quantity5").prop("required",true);
        $("#pup5").prop("required",true);
        $("#uom5").prop("required",true);
        $("#sol5").prop("required",true);
        $("#packaging5").prop("required",true);
    }
    else{
        $("#quantity5").prop("required",false);
        $("#pup5").prop("required",false);
        $("#uom5").prop("required",false);
        $("#sol5").prop("required",false);
        $("#packaging5").prop("required",false);
    };
    // console.log(a);
    $.ajax({
        type: 'GET',
        url:'/get/product',
        data:{
            'p_id':a
        },
        dataType: 'json',
        success: function(response){
            // console.log(response);
            // console.log(response.data[0].item_name_id);
            $('#uom5').val(response.uom);
            $('#sol5').val(response.solubility);
            
           // p_code.value = response.data;
           pup5.value = response.price;
           // pack.value = response.packaging;
           // uom_id.value = response.uom;

        },
        error: function(){
            $('#uom5').val('');
            $('#sol5').val('');
            $('#pup5').val('');
        }
    });
});


 // product 6  js
    $("#p_name6").change(function (){
    // var code = $(this).val();
    var a = document.getElementById("p_name6").value;
    // var b = document.getElementById("p1");
    if (a.length>0){
        $("#quantity6").prop("required",true);
        $("#pup6").prop("required",true);
        $("#uom6").prop("required",true);
        $("#sol6").prop("required",true);
        $("#packaging6").prop("required",true);
    }
    else{
        $("#quantity6").prop("required",false);
        $("#pup6").prop("required",false);
        $("#uom6").prop("required",false);
        $("#sol6").prop("required",false);
        $("#packaging6").prop("required",false);
    };
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
            $('#uom6').val(response.uom);
            $('#sol6').val(response.solubility);
            
           // p_code.value = response.data;
           pup6.value = response.price;
           // pack.value = response.packaging;
           // uom_id.value = response.uom;

        },
        error: function(){
            $('#uom6').val('');
            $('#sol6').val('');
            $('#pup6').val('');
        }
    });
});

 // product 7  js
    $("#p_name7").change(function (){
    // var code = $(this).val();
    var a = document.getElementById("p_name7").value;
    // var b = document.getElementById("p1");
    if (a.length>0){
        $("#quantity7").prop("required",true);
        $("#pup7").prop("required",true);
        $("#uom7").prop("required",true);
        $("#sol7").prop("required",true);
        $("#packaging7").prop("required",true);
    }
    else{
        $("#quantity7").prop("required",false);
        $("#pup7").prop("required",false);
        $("#uom7").prop("required",false);
        $("#sol7").prop("required",false);
        $("#packaging7").prop("required",false);
    };
    // console.log(a);
    $.ajax({
        type: 'GET',
        url:'/get/product',
        data:{
            'p_id':a
        },
        dataType: 'json',
        success: function(response){
            // console.log(response);
            // console.log(response.data[0].item_name_id);
            $('#uom7').val(response.uom);
            $('#sol7').val(response.solubility);
            
           // p_code.value = response.data;
           pup7.value = response.price;
           // pack.value = response.packaging;
           // uom_id.value = response.uom;

        },
        error: function(){
            $('#uom7').val('');
            $('#sol7').val('');
            $('#pup7').val('');
        }
    });
});

 // product 8  js
    $("#p_name8").change(function (){
    // var code = $(this).val();
    var a = document.getElementById("p_name8").value;
    // var b = document.getElementById("p1");
    if (a.length>0){
        $("#quantity8").prop("required",true);
        $("#pup8").prop("required",true);
        $("#uom8").prop("required",true);
        $("#sol8").prop("required",true);
        $("#packaging8").prop("required",true);
    }
    else{
        $("#quantity8").prop("required",false);
        $("#pup8").prop("required",false);
        $("#uom8").prop("required",false);
        $("#sol8").prop("required",false);
        $("#packaging8").prop("required",false);
    };
    // console.log(a);
    $.ajax({
        type: 'GET',
        url:'/get/product',
        data:{
            'p_id':a
        },
        dataType: 'json',
        success: function(response){
            // console.log(response);
            // console.log(response.data[0].item_name_id);
            $('#uom8').val(response.uom);
            $('#sol8').val(response.solubility);
            
           // p_code.value = response.data;
           pup8.value = response.price;
           // pack.value = response.packaging;
           // uom_id.value = response.uom;
        },
        error: function(){
            $('#uom8').val('');
            $('#sol8').val('');
            $('#pup8').val('');
        }
    });
});


 // product 9  js
    $("#p_name9").change(function (){
    // var code = $(this).val();
    var a = document.getElementById("p_name9").value;
    // var b = document.getElementById("p1");
    if (a.length>0){
        $("#quantity9").prop("required",true);
        $("#pup9").prop("required",true);
        $("#uom9").prop("required",true);
        $("#sol9").prop("required",true);
        $("#packaging9").prop("required",true);
    }
    else{
        $("#quantity9").prop("required",false);
        $("#pup9").prop("required",false);
        $("#uom9").prop("required",false);
        $("#sol9").prop("required",false);
        $("#packaging9").prop("required",false);
    };
    // console.log(a);
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
            $('#uom9').val(response.uom);
            $('#sol9').val(response.solubility);
            
           // p_code.value = response.data;
           pup9.value = response.price;
           // pack.value = response.packaging;
           // uom_id.value = response.uom;
        },
        error: function(){
            $('#uom9').val('');
            $('#sol9').val('');
            $('#pup9').val('');
        }
    });
});


 // product 10  js
    $("#p_name10").change(function (){
    // var code = $(this).val();
    var a = document.getElementById("p_name10").value;
    // var b = document.getElementById("p1");
    if (a.length>0){
        $("#quantity10").prop("required",true);
        $("#pup10").prop("required",true);
        $("#uom10").prop("required",true);
        $("#sol10").prop("required",true);
        $("#packaging10").prop("required",true);
    }
    else{
        $("#quantity10").prop("required",false);
        $("#pup10").prop("required",false);
        $("#uom10").prop("required",false);
        $("#sol10").prop("required",false);
        $("#packaging10").prop("required",false);
    };
    // console.log(a);
    $.ajax({
        type: 'GET',
        url:'/get/product',
        data:{
            'p_id':a
        },
        dataType: 'json',
        success: function(response){
            // console.log(response);
            // console.log(response.data[0].item_name_id);
            $('#uom10').val(response.uom);
            $('#sol10').val(response.solubility);
            
           // p_code.value = response.data;
           pup10.value = response.price;
           // pack.value = response.packaging;
           // uom_id.value = response.uom;
        },
        error: function(){
            $('#uom10').val('');
            $('#sol10').val('');
            $('#pup10').val('');
        }
    });
});

    $("#c_pay").change(function (){
    var code = $(this).val();
    // console.log(code);
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
            // console.log(response);
            if (response.codes.length>0){
                c = '';
                for (i = 0; i < response.codes.length; i++){
                    c = c +'<option value="'+ response.ids[i] +'">'+ response.names[i]+', ' +response.codes[i] +'</option>'
                }
                
                $("#product_pay").prepend(c);

               }
            $('#cat').val(response.cat);

        }
    });

});

    $("#product_pay").change(function (){
    var code = $(this).val();
    // console.log(code);
    // var a = document.getElementById("c_pay").value;
    // console.log("hello");
    // var b = document.getElementById("p1");
    // console.log(a);
    $.ajax({
        type: 'GET',
        url:'/get/performa/amount',
        data:{
            'id':code
        },
        dataType: 'json',
        success: function(response){
            // console.log(response);
            pay_id.value = response.amount;

        }
    });

});
// =========================================================feedback====
    $("#feed1").change(function (){
    var customer = $(this).val();
    // console.log(customer);

    $.ajax({
        type: 'GET',
        url:'/feedback/data',
        data:{
            'id':customer
        },
        dataType: 'json',
        success: function(response){
            // console.log(response);
            feedemail.value = response.email;
            feedphone.value = response.contact;
            // console.log(response.samples);
            if (response.samples.length>0) {
                c = '';
                for (i = 0; i < response.samples.length; i++){
                    c = c +'<option value="'+ response.ids[i]+'">'+ response.samples[i] +'</option>'
                }
                
                $("#feedsample1").prepend(c);
            };

        }
    });

});

$("#feedsample1").change(function (){
    var sample = $(this).val();
    // console.log(sample);

    $.ajax({
        type: 'GET',
        url:'/sample/feedback/data',
        data:{
            'id':sample
        },
        dataType: 'json',
        success: function(response){
            // console.log(response);
            s2.value = response.s2;
            s3.value = response.s3;
            s4.value = response.s4;
            s5.value = response.s5;
            s6.value = response.s6;
            s7.value = response.s7;
            s8.value = response.s8;
            s9.value = response.s9;
            s10.value = response.s10;
        }
    });

});


})
    