var SetIntervalTime = Array();
var SetTimeoutTime = Array();
var maxLen = 10;

var timeout;
var interval;


function doTimeConsumingCallculationsWithSetInterval() {

    SetIntervalTime.push(performance.now());
    if (SetIntervalTime.length > maxLen) {
        SetIntervalTime.shift();
    }
    calculatePrimes(1000, 100000000);
}

function doTimeConsumingCallculationsWithSetTimeout() {

    SetTimeoutTime.push(performance.now());
    if (SetTimeoutTime.length > maxLen) {
        SetTimeoutTime.shift();
    }
    calculatePrimes(1000, 100000000);
    window.setTimeout(doTimeConsumingCallculationsWithSetTimeout, document.getElementById('M').value);
}

function averageDiff(arr) {
    var diff = 0;
    for (let i = 0; i < arr.length - 1; i++) {
        diff += arr[i + 1] - arr[i];
    }
    return diff / arr.length;
}


function drawChart() {

    var avgInterval = averageDiff(SetIntervalTime);
    var avgTimeout = averageDiff(SetTimeoutTime);

    var chart = new CanvasJS.Chart("chartContainer", {
        theme: "light2",
        animationEnabled: false,
        title: {
            text: "Average time of cyclic function's calls"
        },
        axisY: {
            title: "Time [ms]"
        },
        data: [{
            type: "column",
            dataPoints: [{
                    label: "averageInterval",
                    y: avgInterval
                },
                {
                    label: "averageTimeout",
                    y: avgTimeout
                },
            ]
        }]
    });
    chart.render();
    window.requestAnimationFrame(drawChart);
}

function start() {
    var M = document.getElementById('M').value;
    interval = window.setInterval(doTimeConsumingCallculationsWithSetInterval, M);
    timeout = window.setTimeout(doTimeConsumingCallculationsWithSetTimeout, M);
    window.requestAnimationFrame(drawChart);
}

function stop() {
    clearInterval(interval);
    clearTimeout(timeout);
    window.location.reload();
    return;
}


function calculatePrimes(iterations, multiplier) {
    var primes = [];
    for (var i = 0; i < iterations; i++) {
        var candidate = i * (multiplier * Math.random());
        var isPrime = true;
        for (var c = 2; c <= Math.sqrt(candidate); ++c) {
            if (candidate % c === 0) {
                // not prime
                isPrime = false;
                break;
            }
        }
        if (isPrime) {
            primes.push(candidate);
        }
    }
    return primes;
}