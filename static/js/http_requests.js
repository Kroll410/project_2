

function delete_request(e, url){
    e.preventDefault()
    $.ajax({
    url,
    type: 'DELETE',
});

}

function put_request(e, url){
//    console.log(e.target[0].value)
    $.ajax({
    url,
    type: 'PUT',
    });
}
// onclick="put_request(event, '/{{ data['name']|lower }}/{{ curr_id }}')"
