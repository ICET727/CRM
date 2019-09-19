$(document).ready(function() {
    $('[data-toggle="tooltip"]').tooltip();
    var actions = $("table td:last-child").html();
    // Append table with add row form on add new button click
    $(".add-new").click(function() {
        $(this).attr("disabled", "disabled");
        var index = $("table tbody tr:last-child").index();
        var row = '<tr>' +
            '<td><select id="myInput " class="browser-default custom-select form-control"><option selected>Open this select menu</option><option value="one">One</option><option value="two">Two</option><option value="three">Three</option></select></td>' +
            '<td></td>' +
            '<td><select class=" browser-default custom-select form-control "><option selected>Open this select menu</option><option value="p1 ">Water Soluble</option><option value="p2 ">Oil Soluble</option></select></td>' +
            '<td><div class="dropdown "><select class=" browser-default custom-select form-control "><option selected>Open this select menu</option><option value="pa1 ">GRAM</option><option value="pa2 ">KILO GRAM</option><option value="pa3 ">BULK</option><option value="pa4 ">5 KGS HDPE CAN</option><option value="pa5 ">25 KGS HDPE CAN</option><option value="pa6 ">50KGS HDPE CAN</option><option value="pa7 ">FIBER DRUM OF 25KGS</option></select></div></td>' +
            '<td><input class="form-control" id="myQty" type="number" value=""></td>' +
            '<td><select id="priority " class="browser-default custom-select form-control" required><option selected>Open this select menu</option><option value="prior1">Normal</option><option value="prior2">Fast</option><option value="prior3">Urgent</option></select></td>' +
            '<td>' + actions + '</td>' +
            '</tr>';
        $("table").append(row);
        $("table tbody tr").eq(index + 1).find(".add, .edit").toggle();
        $('[data-toggle="tooltip"]').tooltip();
    });
    // Add row on add button click
    $(document).on("click", ".add", function() {
        var empty = false;
        var input = $(this).parents("tr").find('input[type="text"]');
        input.each(function() {
            if (!$(this).val()) {
                $(this).addClass("error");
                empty = true;
            } else {
                $(this).removeClass("error");
            }
        });
        $(this).parents("tr").find(".error").first().focus();
        if (!empty) {
            input.each(function() {
                $(this).parent("td").html($(this).val());
            });
            $(this).parents("tr").find(".add, .edit").toggle();
            $(".add-new").removeAttr("disabled");
        }
    });
    // Edit row on edit button click
    $(document).on("click", ".edit", function() {
        $(this).parents("tr").find(".add, .edit").toggle();
        $(".add-new").attr("disabled", "disabled");
    });
    // Delete row on delete button click
    $(document).on("click", ".delete", function() {
        $(this).parents("tr").remove();
        $(".add-new").removeAttr("disabled");
    });
});

function myFunction() {
    var text;
    var price = document.getElementById("myInput ");
    var strProducts = price.options[price.selectedIndex].text;
    switch (strProducts) {
        case "One":
            text = 500;
            break;
        case "Two":
            text = 400;
            break;
        case "Three":
            text = 300;
            break;
        default:
            text = 00;
    }
    document.getElementById("price").innerHTML = text;
    var number = document.getElementById("myQty").value;
    if (number == "") {
        var totall = 1 * text;
    } else {
        var totall = number * text;
    }
    document.getElementById("total").innerHTML = totall;
}