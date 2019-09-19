var s;
$.ajax({
    method: "GET",
    url: "/api/opportunity/v1",
    success: function(response) {
        s = response.list;
        // console.log(s);

        var options = {
            chart: {
                height: 405,
                width: 350,
                type: 'donut',
            },
            series: s,
            labels: {

            },
            responsive: [{
                breakpoint: 480,
                options: {
                    chart: {
                        width: 200
                    },
                    legend: {
                        position: 'bottom'
                    }
                }
            }],
            legend: {
                show: true,
                showForSingleSeries: false,
                showForNullSeries: true,
                showForZeroSeries: true,
                position: 'bottom',
                horizontalAlign: 'left',
                left: '0px',
                floating: false,
                fontSize: '12px',
                fontFamily: 'Helvetica, Arial',
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
                    radius: 9,
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
            theme: {
                palette: 'palette1',
            },
            labels: ['ANALYSIS', 'ANALYSIS APPROVED', 'DELIVERED', 'REJECTED', 'ORDER DISPATCHED'],
            colors: ['#61234e', '#38470b', '#8bbabb', '#ff5858', '#a1aa10', '#10aaa1', '#1aa111', '#dbbdd1']
        }


        var chart = new ApexCharts(
            document.querySelector("#donchart"),
            options
        );
        chart.render();
    }

})