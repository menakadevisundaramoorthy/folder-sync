function createSyncTimeMetrics(sync_number, sync_time) {

    window.onload = function() {

        var dps = []; // dataPoints
        var chart = new CanvasJS.Chart("chartContainer", {
            title: {
                text: "Folder sync number and the time taken for the sync"
            },
            axisX: {
                title: "Sync number",
            },
            axisY: {
                title: "Time taken for sync",
            },
            animationEnabled: true,
            data: [{
                type: "column",
                dataPoints: dps
            }]
        });

        var xVal = 0;
        var yVal = 100;
        var updateInterval = 1000;
        var dataLength = 20; // number of dataPoints visible at any point

        var updateChart = function(count) {

            count = count || 0;

            for (var j = 0; j < count; j++) {
                dps.push({
                    x: sync_number[j],
                    y: sync_time[j]
                });
            }

            if (dps.length > dataLength) {
                dps.shift();
            }

            chart.render();
        };

        updateChart(sync_time.length);
        setInterval(function() { updateChart() }, updateInterval);

    }

}

function createSyncTimeMetricsTable(jsonData) {
    displayJsonToTable(jsonData)
}

$(document).ready(function() {
    $('#display_csv_data').DataTable();

});

//Method to get the data for the Table
function getTableData(jsonData) {
    if (jsonData.length > 0) {
        var headers = Object.keys(jsonData[0]);

        var htmlBody = '<tbody>';
        for (var i = 0; i < jsonData.length; i++) {
            var row = jsonData[i];
            htmlBody += '<tr>';
            for (var j = 0; j < headers.length; j++) {
                var key = headers[j];
                htmlBody += '<td>' + row[key] + '</td>';
            }
            htmlBody += '</tr>';
        }
        htmlBody += '</tbody>';
        return htmlBody;
    } else {
        return 'There is no data in CSV';
    }
}