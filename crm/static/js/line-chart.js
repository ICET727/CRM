var a ;
var b;
$(document).ready(function() {
    $.ajax({
        type: 'GET',
        url: "/api/sales/report",
        dataType: 'json',
        success: function(response) {
            // console.log(response)
            a = response.result;
            b = response.amount;
// console.log(b);
var options = {
           chart: {
               height: 350,
               type: 'line',
               shadow: {
                   enabled: false,
                   color: '#bbb',
                   top: 3,
                   left: 2,
                   blur: 3,
                   opacity: 1
               },
           },
           stroke: {
               width: 7,
               curve: 'smooth'
           },
           series: [{
               name: 'Sales Value',
               data: b
           }],
           xaxis: {
               type: 'datetime',
               categories: a,
           },
           title: {
               text: 'Sales Graph',
               align: 'left',
               style: {
                   fontSize: "16px",
                   color: '#666'
               }
           },
           fill: {
               type: 'gradient',
               gradient: {
                   shade: 'dark',
                   gradientToColors: ['#FDD835'],
                   shadeIntensity: 1,
                   type: 'horizontal',
                   opacityFrom: 1,
                   opacityTo: 1,
                   stops: [0, 70, 100, 30]
               },
           },
           markers: {
               size: 4,
               opacity: 0.9,
               colors: ["#FFA41B"],
               strokeColor: "#fff",
               strokeWidth: 2,
               hover: {
                   size: 7,
               }
           },
           yaxis: {
               min: 0,
               max: 15000,
               title: {
                   text: 'Sales',
               },
           }
       }

       var chart = new ApexCharts(
           document.querySelector("#chart22"),
           options
       );
       chart.render();
    }
    });
});