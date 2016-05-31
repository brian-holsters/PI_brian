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


/*RESPUESTA ABSTRACTA*/
postFunction = function(formulario, respuesta_de){
	var csrftoken = getCookie('csrftoken');
	formulario.action = window.location.protocol + "//" + window.location.host + "/ajax_post";

	if(formulario.texto.value){
		/*Composición de la petición POST*/
		var post_data = {
			"texto" : formulario.texto.value,
			"csrfmiddlewaretoken" : csrftoken
		};
		if (respuesta_de !== null){
			console.log("es respuesta");
			console.log(respuesta_de);
			post_data["respuesta_de"] = respuesta_de;
		}else{
			console.log("es post original");
			post_data["emote_id"]= formulario.emote_id.value
		}
		
		/*petición POST*/
		$.post(formulario.action, post_data, function(data, textStatus, jqXHR){
			if (textStatus === "success"){
				/*comportamiento según se trate de un post original o una respuesta*/
				if(respuesta_de === null){
					$("#posts-list").prepend(data);
				}else{
					$lista = $(formulario).parents(".respuesta-container").siblings("ul.respuestas-lista");
					$lista.prepend(data);
					
					console.log($lista.parents("div.respuestas-container"));
					
					$lista.parents("div.respuestas-container").removeClass("hidden");
				}
				
			}
		});
		formulario.texto.value="";
	}
}

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
	
	/*PUBLICAR POST PROPIO*/
	$("#post-form form").submit(function(event){
		event.preventDefault();
		postFunction(this, null);
	});

	function asimilar_botones(){
		/* BOTON RESPONDER*/
		var $botones_responder = $("button[data-post-id]");
		$botones_responder.click(function(){
			$(this).siblings("div[data-post-id]").toggleClass("hidden");
		});
		
		/*RESPONDER A UN POST*/
		var $formularios = $("form[data-post-id]");
		$formularios.submit(function(event){
			event.preventDefault();
			postFunction(this, $(this).data("post-id"));
		});
	}
});