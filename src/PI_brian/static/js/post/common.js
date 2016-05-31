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
					post_id = $(formulario).data("post-id");
					$lista = $("ul#respuestas-lista_"+post_id);
					$lista.prepend(data);
					
					$contenedor = $("div#respuestas_"+post_id);
					$contenedor.removeClass("hidden");
				}

			}
		});
		formulario.texto.value="";
	}
}