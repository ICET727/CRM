$(document).ready(function() {
    $.ajax({
        type: 'GET',
        url: "/api/task/v1",
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
            document.getElementById("test1").innerHTML = a;
        }
    });


    $("#t1").click(function(){
        var a = document.getElementById("date1").value;
        var c = document.getElementById("description1").value;
        var u = document.getElementById("s1").value;
        var t = document.getElementById("date2").value;
        $.ajax({
        type: 'GET',
        url: '/api/task/add',
        data : {

            'start_date': a,
            'end_date': t,
            'title': c,
            'user': u
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