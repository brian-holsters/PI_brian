$(document).ready(function(){

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
});