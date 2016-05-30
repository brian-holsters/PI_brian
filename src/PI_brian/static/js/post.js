$(document).ready(function(){
    /*SELECCION DE EMOTE*/
	var $botones_emote = $("a[data-emote_id]");
	var $hidden_emote = $("#hidden_emote");
	var $emote_selector_imagen = $("img.emote-selector-imagen");

	$botones_emote.click(function(){
		$this = $(this);
		$hidden_emote.value = $this.data("emote_id");
		var emote_src = $this.children("img.emote-selector-imagen").attr("src");
		
		$emote_selector_imagen.attr("src", emote_src);
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