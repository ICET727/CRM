$(document).ready(function() {
    $.ajax({
        type: 'GET',
        url: "/api/getMeetings/v1",
        dataType: 'json',
        // data:{

        //     'sender': $('#recipient_email').val(),
        //     'subject': $('#subject').val(),
        //     'body' : $('#body').val()

        // },

        success: function(response) {
            // console.log(response);
            a = '';
            if (response) {
                // console.log(response);
                for (i = 0; i < response.date.length; i++) {
                    a = a + '<li><span class="message-serial message-cl-one ">'
                    a = a + (i+1) + '</span>'+ response.title[i] + ' <span class="message-info ">'
                    a = a + '</span> <span class="message-time ">'
                    a = a + response.time[i] + '</span>'+'</li>'
                }
            } else {
                a = a + '<p> There is No Event Please Refresh Your Page</p>'
            }
            // console.log(a);
            document.getElementById("test").innerHTML = a;
        }
    });


    $("#m1").click(function(){
        var d = document.getElementById("d1").value;
        var t = document.getElementById("d2").value;
        var n = document.getElementById("d3").value;
        $.ajax({
        type: 'GET',
        url: '/api/meeting/add',
        data : {

            'date': d,
            'time': t,
            'name': n,
            // 'time': $('#time1').val(),
            // 'title':$('#description1').val()
        },
        dataType: 'json',
        success: function(response){
            alert("Meeting generated")
        }
    });
    });
    

    
    
})