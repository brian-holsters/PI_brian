function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


$(document).ready(function(){
    $("#post-form form").submit(function(event){
        var csrftoken = getCookie('csrftoken');
        event.preventDefault();
        this.action = window.location.protocol + "//" + window.location.host + "/ajax_post";

        $.post(
            this.action,
            {
                "texto" : this.texto.value,
                "csrfmiddlewaretoken" : csrftoken
            },
            function(data, textStatus, jqXHR){
                if (textStatus === "success"){
                    $("#posts-list").prepend(data);
                }
            }
        );

    });
});