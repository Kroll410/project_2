function delete_request(e, url){
    e.preventDefault()
    $.ajax({
        url,
        type: 'DELETE',
        complete: function(){
            top.location.href = url.split('/').slice(0, -1).join('')
        }
    });
}


function timeout_delete_request(e, url){
    e.preventDefault()
    $.ajax({
        url,
        type: 'DELETE',
        complete: function(){
            top.location.href = '/'
        }
    });
}