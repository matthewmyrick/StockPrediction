
function loadChart(dates, predictions){
    console.log(dates)
    console.log(predictions)
    var ctx = document.getElementById('predictionsChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: dates,
            datasets: [{
                label: 'Predictions',
                data: predictions,
                borderColor: 'rgb(75, 192, 192)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

function date(dates) {
    console.log(dates)
}

function spinner() {
    document.getElementsByClassName("loader")[0].style.display = "block";
}

function test(x){
    alert(x)
    console.log(x)
}