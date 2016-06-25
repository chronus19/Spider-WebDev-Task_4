

function delete_post(post) {

    var t = confirm("Are you sure you want to delete this post ?");
    if (t===false) 
        return;

    document.location.href = '/delete_post/?post_id=' + post.id;
    

}