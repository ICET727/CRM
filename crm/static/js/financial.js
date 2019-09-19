$.ajax({
        type: 'GET',
        url: "/api/sales/report",
        dataType: 'json',
        success: function(response) {
            // console.log(response)
            a = response.result;
            b = response.amount;
     var canvas = document.getElementById('myChart11');
       var data = {
           labels: a,
           datasets: [{
               label: "Sales Progress Data",
               backgroundColor: "rgba(75,192,192,0.4)",
               borderColor: "rgba(75,192,192,1)",
               pointBorderColor: "rgba(75,192,192,1)",
               pointBackgroundColor: "#fff",
               pointHoverBackgroundColor: "rgba(75,192,192,1)",
               pointHoverBorderColor: "rgba(220,220,220,1)",
               data: b,
           }]
       };
       var option = {
           showLines: true,
           yAxes:[{
            ticks: {
              beingAtZero: true,
              callback: function(label, index, labels){
           return label/1000 +'k';
         }
       },
       scaleLabel: {
        display: true,
        labelString: '1k = 1000'
       }
     }]
       };
       var myLineChart = Chart.Line(canvas, {
           data: data,
           options: option
       });
   }});