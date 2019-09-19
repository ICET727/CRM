window.onload = function() {
    var chart1 = new CanvasJS.Chart("chartCont", {
        animationEnabled: true,
        title: {
            text: "Campaing Cost by Year"
        },
        axisY: {
            title: "Cost in USD",
            suffix: "mn",
            prefix: "$"
        },
        data: [{
            type: "splineArea",
            color: "rgba(54,158,173,.7)",
            markerSize: 5,
            xValueFormatString: "YYYY",
            yValueFormatString: "$#,##0.##",
            dataPoints: [
                { x: new Date(2003, 0), y: 3000 },
                { x: new Date(2004, 0), y: 3200 },
                { x: new Date(2005, 0), y: 4000 },
                { x: new Date(2006, 0), y: 2800 },
                { x: new Date(2007, 0), y: 2300 },
                { x: new Date(2008, 0), y: 1900 },
                { x: new Date(2009, 0), y: 2800 },
                { x: new Date(2010, 0), y: 2000 },
                { x: new Date(2011, 0), y: 3700 },
                { x: new Date(2012, 0), y: 3900 },
                { x: new Date(2013, 0), y: 2800 },
                { x: new Date(2014, 0), y: 4700 },
                { x: new Date(2015, 0), y: 4500 },
                { x: new Date(2016, 0), y: 2600 },
                { x: new Date(2017, 0), y: 5000 },
                { x: new Date(2018, 0), y: 4000 },
                { x: new Date(2019, 0), y: 7000 }
            ]
        }]
    });
    chart1.render();
}