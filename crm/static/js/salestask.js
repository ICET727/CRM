$(document).ready(function() {
    $.ajax({
        type: 'GET',
        url: "/api/salestask/list",
        dataType: 'json',
        // data:{

        //     'sender': $('#recipient_email').val(),
        //     'subject': $('#subject').val(),
        //     'body' : $('#body').val()

        // },

        success: function(response) {
            // console.log(response.start_date.length);
            // console.log("hello");
            a = '';
            if (response) {
                // console.log(response);
                for (i = 0; i < response.start_date.length; i++) {
                    a = a + '<ul class="message-list-menu"><li><div class="row"><div class="col-lg-6"><span class="message-serial message-cl-one ">'
                    a = a + (i+1) + '</span>'+ response.title[i] +'</div><div class="col-lg-6 ">'
                    a = a + '<span class="message-time ">'
                    a = a + response.start_date[i] + '</span>'+'</div></div></li>'+'</ul>'
                }
            } else {
                a = a + '<p> There is No Event Please Refresh Your Page</p>'
            }
            // console.log(a);
            document.getElementById("task1").innerHTML = a;
        }
    });

    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth()+1; //January is 0!
    var yyyy = today.getFullYear();
     if(dd<10){
            dd='0'+dd
        } 
        if(mm<10){
            mm='0'+mm
        } 

    today = yyyy+'-'+mm+'-'+dd;
    document.getElementById("date2").setAttribute("min", today);
    document.getElementById("date1").setAttribute("min", today);
    

    $("#t1").click(function(){
        var a = document.getElementById("date1").value;
        var c = document.getElementById("description1").value;
        var t = document.getElementById("date2").value;
        // console.log(a);
        $.ajax({
        type: 'GET',
        url: '/api/sales/task',
        data : {

            'start_date': a,
            'end_date': t,
            'title': c,
            // 'time': $('#time1').val(),
            // 'title':$('#description1').val()
        },
        dataType: 'json',
        success: function(response){
            alert("Task generated")
        }
    });
    });
    
})