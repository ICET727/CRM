$("#update_account").click(function(e) {
    e.preventDefault();
    var name = document.getElementById('name').value;
    var billing_address = document.getElementById('billing_address').value;
    var status = document.getElementById('status').value;
    var website = document.getElementById('website').value;
    var street = document.getElementById('street').value;
    var post_code = document.getElementById('post_code').value;
    var tags = document.getElementById('tagElement').value;
    var phone = document.getElementById('phone').value;
    var city = document.getElementById('city').value;
    var state = document.getElementById('state').value;
    var attachment = document.getElementById('attachment').value;
    var email = document.getElementById('email').value;
    var country = document.getElementById('country').value;
    var leads = document.getElementById('leads').value;
    var contacts = document.getElementById('contacts').value;
    console.log(name, email, phone, leads);
    $.ajax({
        url: 'http://13.232.209.79:8000/apv1/accounts/v1/',
        method: 'POST',
        data: {
            'name': name,
            // 'billing_address': billing_address,
            // 'status': status,
            // 'website': website,
            // 'street': street,
            // 'post_code': post_code,
            // 'tags': tags,
            'phone': phone,
            // 'city': city,
            // 'state': state,
            // 'attachment': attachment,
            'email': email,
            'country': country,
            'lead': 1,
            'contact_name': "Hello"
        },
        dataType: 'json',
        success: function(data) {
            console.log(data);
        }
    });
});