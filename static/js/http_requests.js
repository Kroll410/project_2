

function delete_request(e, url){
    $.ajax({
        url,
        type: 'DELETE',
    });
}


//function put_request(e, url){
//    e.preventDefault()
//    $.ajax({
//        url,
//        type: 'PUT',
//    });
//    console.log(e)
//}
