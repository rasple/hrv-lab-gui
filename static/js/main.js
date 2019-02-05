function ping() {
    button = $('#refreshButton')
    button.html('Refreshing...')
    button.attr('class', 'btn btn-warning')

    var dectStatus = $('#dect-status')
    var wifiStatus = $('#wifi-status')
    var archpadStatus = $('#archpad-status')

    $.get('ping', function (result, status) {

        if (result['raspi']) {
            wifiStatus.attr('class', 'badge badge-success')
            wifiStatus.html('Connected')
        }
        else {
            wifiStatus.attr('class', 'badge badge-danger')
            wifiStatus.html('Disconnected')
        }
        if (result['dect']) {
            dectStatus.attr('class', 'badge badge-success')
            dectStatus.html('Connected')
        }
        else {
            dectStatus.attr('class', 'badge badge-danger')
            dectStatus.html('Disconnected')
        }
        if (result['archpad']) {
            archpadStatus.attr('class', 'badge badge-success')
            archpadStatus.html('Connected')
        }
        else {
            archpadStatus.attr('class', 'badge badge-danger')
            archpadStatus.html('Disconnected')
        }

        button.html('Refresh')
        button.attr('class', 'btn btn-primary')

    });
}




function abort() {
    $.ajax({
        type: 'GET',
        url: '/abort',
        success: function () {enableEverything()},
    })
}

function disableEverything() {
    form.classList.add('was-validated');
    $('#startButton').prop('disabled', true)
    $('form#form :input').prop('disabled', true)
    $('#stopButton').css('display', 'float')
    console.log("Disabled")
}

function enableEverything() {
    form.classList.add('needs-validation');
    $('#startButton').prop('disabled', false)
    $('form#form :input').prop('disabled', false)
    $('#stopButton').css('display', 'none')
    console.log("Enabled")
}

function time() {
    $.get('time', function (data) {
        $('#timer').html(data['time'])
        if (data['running']) {
            setTimeout(time, 1000);
        } else {
            enableEverything()
        }
    });
}

function protocol() {
    $.get('protocol', function (data) {
        $('#protocol').html(data)
        setTimeout(protocol, 2000);
    });
}

function log() {
    $.get('log', function (data) {
        $('#log').html(data)
        setTimeout(log, 2000);
    });
}

function clearLog() {
    $.get('clearLog')
    $.get('log', function (data) {
        $('#log').html(data)
    });
}

function clearProtocol() {
    $.get('clearProtocol')
    $.get('protocol', function (data) {
        $('#protocol').html(data)
    });
}