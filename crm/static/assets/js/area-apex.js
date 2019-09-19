
$.ajax({
    method:"GET",
    url:"/api/sales/report",
    success: function(response){
        // console.log(response);
        var dataSeries = response.result;
        // console.log(dataSeries[0][1].value);
       
    var ts2 = 1484418600000;
    var dates = [];
    var spikes = [5, -5, 3, -3, 8, -8]
    for (var i = 0; i < response.result.length; i++) {
        ts2 = ts2 + 86400000;
        var innerArr = [ts2, dataSeries[0][i].value];
        console.log(dates.push(innerArr));
        dates.push(innerArr)
    }

        var options = {
            chart: {
                type: 'area',
                stacked: false,
                height: 350,
                zoom: {
                    type: 'x',
                    enabled: true
                },
                toolbar: {
                    autoSelected: 'zoom'
                }
            },
            dataLabels: {
                enabled: false
            },
            series: [{
                name: 'XYZ MOTORS',
                data: dates
            }],
            markers: {
                size: 0,
            },
            title: {
                text: 'Sales Projection',
                align: 'left'
            },
            fill: {
                type: 'gradient',
                gradient: {
                    shadeIntensity: 1,
                    inverseColors: false,
                    opacityFrom: 0.5,
                    opacityTo: 0,
                    stops: [0, 90, 100]
                },
            },
            yaxis: {
                min: 20000000,
                max: 250000000,
                labels: {
                    formatter: function(val) {
                        return (val / 1000000).toFixed(0);
                    },
                },
            },
            xaxis: {
                type: 'datetime',
            },

            tooltip: {
                shared: false,
                y: {
                    formatter: function(val) {
                        return (val / 1000000).toFixed(0)
                    }
                }
            }
        }

        var chart = new ApexCharts(
            document.querySelector("#chart"),
            options
        );

        chart.render();

 }
    });