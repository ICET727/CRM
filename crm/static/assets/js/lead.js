$("#update_lead").click(function(e) {
            e.preventDefault();
            var first_name = document.getElementById('first_name').value;
            var last_name = document.getElementById('last_name').value;
            var website = document.getElementById('website').value;
            var source = document.getElementById('source').value;
            var account_name = document.getElementById('account_name').value;
            var address_line = document.getElementById('address_line').value;
            var street = document.getElementById('street').value;
            var tag = document.getElementById('tag').value;
            var title = document.getElementById('title').value;
            var city = document.getElementById('city').value;
            var state = document.getElementById('state').value;
            var postcode = document.getElementById('post_code').value;
            var attachment = document.getElementById('attachment').value;
            var phone = document.getElementById('phone').value;
            var country = document.getElementById('country').value;
            var description = document.getElementById('description').value;
            var email = document.getElementById('email').value;
            var status = document.getElementById('status').value;
            var assigned_user = document.getElementById('assigned_user').value;
            $.ajax({
                url: 'http://13.232.209.79:8000/apv1/leads/v1/',
                method: 'POST',
                data: {
                    'first_name': first_name,
                    'last_name': last_name,
                    'website': website,
                    'source': source,
                    'account_name': account_name,
                    'address_line': address_line,
                    'street': street,
                    'tag': tag,
                    'title': title,
                    'city': city,
                    'state': state,
                    'postcode': postcode,
                    'attachment': attachment,
                    'phone': phone,
                    'country': country,
                    'description': description,
                    'email': email,
                    'status': status,
                    'assigned_user': assigned_user,
                },
                dataType: 'json',
                success: function(data) {
                    console.log("Successfully Sent!");
                }
            });
        }