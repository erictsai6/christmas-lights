(function() {

    window.submitFile = function() {
        var input = document.querySelector('input[type="file"]')

        var data = new FormData()
        data.append('audio', input.files[0])

        fetch('/upload', {
            method: 'POST',
            body: data       
        })
        .then(function(r) {
            console.log(r);
            return r.json();  
        }).then(function(response) {
            if (response.state === 'SUCCESS') {
                console.log('success');
            } else {
                console.log(response);
            }
            
        }).catch(function(err) {
            console.log(err);
        })

    }

}());