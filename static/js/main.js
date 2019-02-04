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

function stop() {

}


function abort() {
    $.ajax({
        type: 'GET',
        url: '/abort',
        success: function () { },
        error: function () { },
        complete: function () { }
    })
}

function disableEverything(){
    form.classList.add('was-validated');
    $('#startButton').prop('disabled', true)
    $('form#form :input').prop('disabled', true)
    $('#stopButton').css('display', 'block')
}

function enableEverything(){
    form.classList.add('needs-validation');
    $('#startButton').prop('disabled', false)
    $('form#form :input').prop('disabled', false)
    $('#stopButton').css('display', 'none')
}

function time() {
    $.get('time', function (data) {
        $('#timer').html(data)
        if(data == 'Done!'){
            enableEverything()
        }
        setTimeout(time, 1000);
    });
}

function protocol() {
    $.get('protocol', function (data) {
        $('#protocol').html(data)
        setTimeout(protocol, 2000);
    });
}

function log(){
    $.get('log', function (data) {
        $('#log').html(data)
        setTimeout(log, 2000);
    }); 
}

function clearLog(){
    $.get('clearLog')
}

function clearProtocol(){
    $.get('clearProtocol')
}