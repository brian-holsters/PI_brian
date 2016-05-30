$(document).ready(function(){
	$botones_responder = $("button[data-post-id]");
	$botones_responder.click(function(){
		$(this).siblings("div[data-post-id]").toggleClass("hidden");
	});
	
	/*GESTIÓN DE FORMULARIO AJAX: */
	$formularios = $("form[data-post-id]");
	
	$formularios.submit(function(e){
		e.preventDefault();
		var csrftoken = getCookie('csrftoken');
		this.action = window.location.protocol + "//" + window.location.host + "/ajax_respuesta";
		var $this = $(this);
		
		if(this.texto.value){
			$.post(
				this.action,
				{
					"texto" : this.texto.value,
					"csrfmiddlewaretoken" : csrftoken,
					"emote_id": this.emote_id.value,
					"post_id": $this.data("post-id")
				},
				function(data, textStatus, jqXHR){
					if (textStatus === "success"){
						console.log("BIEN!");
					}
				}
			);
			this.texto.value="";
		}
	});
});