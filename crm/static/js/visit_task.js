$(document).ready(function() {
    var u = document.getElementById("v1").value;
    // console.log(u);
    $.ajax({
        type: 'GET',
        url: "/api/visit/task",
        dataType: 'json',
        data:{
            'user': u,
        },
        success: function(response) {
            // console.log(response.start_date.length);
            // console.log("hello");
            a = '';
            if (response) {
                // console.log(response);
                for (i = 0; i < response.start_date.length; i++) {
                    a = a + '<ul class="message-list-menu"><li><span class="message-serial message-cl-one ">'
                    a = a + (i+1) + '</span>'+ response.title[i] + ' <span class="message-info ">'
                    a = a + '</span> <span class="message-time ">'
                    a = a + response.start_date[i] + '</span>'+'</li>'+'</ul>'
                }
            } else {
                a = a + '<p> There is No Event Please Refresh Your Page</p>'
            }
            // console.log(a);
            document.getElementById("task").innerHTML = a;
        }
    });

})