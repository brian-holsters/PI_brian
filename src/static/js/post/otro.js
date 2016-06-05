$(document).ready(function(){

	/* BOTON RESPONDER*/
	var $botones_responder = $("button[data-post-id]");
	$botones_responder.click(function(){
	    $target = $("div.responder-container[data-post-id=" + $(this).data("post-id") + "]")
		$target.toggleClass("hidden");
		console.log($target.children().children(".respuesta-texto"));
		$target.children().children(".respuesta-texto").focus();
	});

	/*RESPONDER A UN POST*/
	var $formularios = $("form[data-post-id]");
	$formularios.submit(function(event){
		event.preventDefault();
		postFunction(this, $(this).data("post-id"));
	});
});