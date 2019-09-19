$.ajax({
    method:"GET",
    url:"/api/sales/person/lead/v1",
    success: function(response){
        // console.log(response.list)
        var s = response.list
    
function func1() {
    var options = {
        animationEnabled: true,
        chart: {
            height: 400,
            width: 320,
            type: 'radialBar',
        },
        title: {
            align: 'center',
            style: {
                fontSize: '26px',
                color: '#263238'
            },
        },
        plotOptions: {
            radialBar: {
                dataLabels: {
                    name: {
                        fontSize: '22px',
                    },
                    value: {
                        fontSize: '16px',
                    },
                    total: {
                        show: true,
                        label: 'Total',
                        formatter: function(w) {
                            var sum = 0;
                            // By default this function returns the average of all series. The below is just an example to show the use of custom formatter function
                            for (var i = 0; i < s.length; i++) {
                                sum = sum + s[i]
                            }
                            return sum
                        }
                    }
                }
            }
        },
        series: s,
        labels: ['Calls', 'Emails', 'Existing Customer', 'Partner', 'Public Relation', 'Campaigns', 'Others'],
        legend: {
            show: true,
            showForSingleSeries: false,
            showForNullSeries: true,
            showForZeroSeries: true,
            position: 'bottom',
            horizontalAlign: 'left',
            floating: false,
            fontSize: '14px',
            fontFamily: 'Helvetica, Arial',
            width: undefined,
            height: undefined,
            formatter: undefined,
            offsetX: 0,
            offsetY: 0,
            labels: {
                colors: undefined,
                useSeriesColors: false
            },
            markers: {
                strokeWidth: 0,
                strokeColor: '#fff',
                radius: 12,
                customHTML: undefined,
                onClick: undefined,
                offsetX: 0,
                offsetY: 0
            },
            
            onItemClick: {
                toggleDataSeries: true
            },
            onItemHover: {
                highlightDataSeries: true
            },
        },

    }

    var chart = new ApexCharts(
        document.querySelector("#rad-chart"),
        options
    );

    chart.render();
}

function func2() {

}

function addLoadEvent(func) {
    var oldonload = window.onload;
    if (typeof window.onload != 'function') {
        window.onload = func;
    } else {
        window.onload = function() {
            if (oldonload) {
                oldonload();
            }
            func();
        }
    }
}
addLoadEvent(func1);
addLoadEvent(func2);
addLoadEvent(function() {
    document.body.style.backgroundColor = '#F4F4F5';
})

function explodePie(e) {
    if (typeof(e.dataSeries.dataPoints[e.dataPointIndex].exploded) === "undefined" || !e.dataSeries.dataPoints[e.dataPointIndex].exploded) {
        e.dataSeries.dataPoints[e.dataPointIndex].exploded = true;
    } else {
        e.dataSeries.dataPoints[e.dataPointIndex].exploded = false;
    }
    e.chart.render();
}

}

})