function ping(){
    button = $('#refreshButton')
    button.html('Refreshing...')
    button.attr("class", 'btn btn-warning')

    var dectStatus = $('#dect-status')
    var wifiStatus = $('#wifi-status')
    var archpadStatus = $('#archpad-status')

    $.get("ping", function(result, status){

        if(result['raspi']){
            wifiStatus.attr('class', 'badge badge-success')
            wifiStatus.html('Connected')
        }
        else {
            wifiStatus.attr('class', 'badge badge-danger')
            wifiStatus.html('Disconnected')
        }
        if(result['dect']){
            dectStatus.attr('class', 'badge badge-success')
            dectStatus.html('Connected')
        }
        else {
            dectStatus.attr('class', 'badge badge-danger')
            dectStatus.html('Disconnected')
        }
        if(result['archpad']){
            archpadStatus.attr('class', 'badge badge-success')
            archpadStatus.html('Connected')
        }
        else {
            archpadStatus.attr('class', 'badge badge-danger')
            archpadStatus.html('Disconnected')
        }

    button.html('Refresh')
    button.attr("class", 'btn btn-success')
        
    });
}

function time(){
    $.ajax({
        type: 'GET',
        url: '/time',
        success: function(){},
        error: function(){},
        complete: function(){}
    })
}

function start(){
    startButton = $('#startButton')
    startButton.attr('class', 'btn btn-danger')
    startButton.html('Stop')
    $.ajax({
        type: 'GET',
        url: '/start',
        success: function(){},
        error: function(){},
        complete: function(){
        startButton.attr('class', 'btn btn-primary')
        startButton.html('Start')
        }
    })
    
    
}
function abort(){
    $.ajax({
        type: 'GET',
        url: '/abort',
        success: function(){},
        error: function(){},
        complete: function(){}
    })
}

function exportFile(){

}

function clear(){

}

function sendForm() {
    
}