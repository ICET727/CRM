$("#update_case").click(function(e) {
            e.preventDefault();
            var name = document.getElementById('name').value;
            var closed_date = document.getElementById('billing_address').value;
            var contacts = document.getElementById('contacts').value;
            var status = document.getElementById('status').value;
            var assigned_user = document.getElementById('assigned_user').value;
            var description = document.getElementById('description').value;
            var proirity = document.getElementById('proirity').value;
            var account = document.getElementById('account').value;
            var type_of_case = document.getElementById('type_of_case').value;
            var attachment = document.getElementById('attachment').value;
            $.ajax({
                url: 'http://13.232.209.79:8000/apv1/cases/v1/',
                method: 'POST',
                data: {
                    'name': name,
                    'closed_date': losed_date,
                    'contacts': contacts,
                    'status': status,
                    'assigned_user': ssigned_user,
                    'description': description,
                    'proirity': proirity,
                    'account': account,
                    'type_of_case': city,
                    'attachment': attachment,
                },
                dataType: 'json',
                success: function(data) {
                    console.log("Successfully Sent!");
                }
            });
        }