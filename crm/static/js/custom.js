// $('#mail').change(function(){
//   console.log($(this).val());
// }); 

// function emailfile(){
// 	var recipient_email = document.getElementById("recipient_email");
//   var subject = document.getElementById('subject').value;
//   var body = document.getElementById('content').value;

//   console.log(subject);
//   console.log(body);

// $.ajax({
//   url: '/api/email/v1',
//   method: 'POST',
//   data: {
//     'sender': recipient_email,
//     'subject': subject,
//     'body' : body
//   },
//   dataType: 'json',
//   success: function() {

//       alert("A user with this username already exists.");

//   }
// });
// console.log("Hello")
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
            a = '';
            if (response) {
                // console.log(response);
                for (i = 0; i < response.length; i++) {
                    a = a + '<ul class="message-list-menu ">'
                    a = a + '<li><span class="">1. </span><b> <span class="message-info ">'
                    a = a + response[i]['date'] + '</span></b> <span class="message-time ">'
                    a = a + response[i]['time'] + '</span><p style="color: black;" align="justify">'
                    a = a + response[i]['description'] + '</p>'
                    a = a + '</li>'
                    a = a + '</ul>'
                }
            } else {
                a = a + '<p> There is No Event Please Refresh Your Page</p>'
            }
            document.getElementById("test").innerHTML = a;
        }
    });

    $("#m1").click(function() {
        $.ajax({
            type: 'POST',
            url: "/api/getMeetings/v1",
            dataType: 'json',
            data: {

                'date': $('#date').val(),
                'time': $('#time').val(),
                'description': $('#description').val()

            },

            success: function(response) {
                console.log(response);

            }
        });
    });
    // $("select.a1").change(function(){
    //     var b = $(this).children("option:selected").val();
    //     var id = document.getElementById("1");
    //     console.log(id);
    //     $.ajax({
    //         type:"GET",
    //         url: "/api/stage/v1",
    //         data: {
    //             "stage": b,
    //             "id": id,
    //         },
    //         dataType: 'Json',
    //         success: function(response){
    //             // alert("status changed..");
    //         }
    //     })

    // });

});


$(document).ready(function() {
    $.ajax({
        type: 'GET',
        url: "/api/getTask/v1",
        dataType: 'json',
        // data:{

        //     'sender': $('#recipient_email').val(),
        //     'subject': $('#subject').val(),
        //     'body' : $('#body').val()

        // }, a = a + response[i]['time']

        success: function(response) {
            a = '';
            if (response) {
                // console.log(response);
                for (i = 0; i < response.length; i++) {
                    a = a + '<ul class="message-list-menu ">'
                    a = a + '<li><span class="message-serial message-cl-one ">1</span> <span class="message-info ">'
                    a = a + reponse[i]['description'] + '</span> <span class="message-time ">'
                    a = a + response[i]['time'] + '</span>'
                    a = a + '</li>'
                    a = a + '</ul>'
                }
            } else {
                a = a + '<p> There is No Task Please Refresh Your Page</p>'
            }
            document.getElementById("test1").innerHTML = a;
        }
    });

    $("#t1").click(function() {
        $.ajax({
            type: 'POST',
            url: "/api/getTask/v1",
            dataType: 'json',
            data: {

                'date': $('#date1').val(),
                'time': $('#time1').val(),
                'description': $('#description1').val()

            },

            success: function(response) {
                console.log(response);

            }
        });
    });
});
/*$('.')*/