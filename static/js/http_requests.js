


function delete_request(e, url){
    e.preventDefault()
    $.ajax({
    url,
    type: 'DELETE',
    success: function(result) {
        // Do something with the result
    }
});

}


function put_request(e, url){
//    e.preventDefault()
    console.log(e.target[0].value)
    $.ajax({
    url,
    type: 'PUT',
    });
}

//<form onsubmit="put_request(event, '/remove/{{ data['name'] }}/{{ idx + 1}}')">
//                    <input type="text" name="sample-text">
//                    <button type="submit" class="btn btn-primary btn-sm"
//                            onclick="">Edit</button>
//                </form>


function foo(e){
//    e.preventDefault()
    console.log('kek')
}