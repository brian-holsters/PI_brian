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
    /*SELECCION DE EMOTE*/
    var $botones_emote = $("a[data-emote_id]");
    var $hidden_emote = $("#hidden_emote");

    $botones_emote.click(function(){
    $this = $(this);
        $hidden_emote.value = $this.data("emote_id");
        console.log($hidden_emote);
    });

    /*PROCESO AJAX*/
    $("#post-form form").submit(function(event){
        var csrftoken = getCookie('csrftoken');
        event.preventDefault();
        this.action = window.location.protocol + "//" + window.location.host + "/ajax_post";

        if(this.texto.value){
            $.post(
                this.action,
                {
                    "texto" : this.texto.value,
                    "csrfmiddlewaretoken" : csrftoken,
                    "emote_id": this.emote_id.value
                },
                function(data, textStatus, jqXHR){
                    if (textStatus === "success"){
                        $("#posts-list").prepend(data);
                    }
                }
            );
            this.texto.value="";
        }
    });
});