$(document).ready(function(){
	/*SELECCION DE EMOTE*/
	var $botones_emote = $("a[data-emote_id]");
	var $hidden_emote = $("#hidden_emote");
	console.log($hidden_emote);
	var $emote_selector_imagen = $("img.emote-selector-imagen");

	$botones_emote.click(function(){
		$this = $(this);
		$hidden_emote.attr('value', $this.data("emote_id"));
		console.log($this.data("emote_id"), $hidden_emote.value);
		var emote_src = $this.children("img.emote-selector-imagen").attr("src");
		$emote_selector_imagen.attr("src", emote_src);
    });

	/*PUBLICAR POST PROPIO*/
	$("#post-form form").submit(function(event){
		event.preventDefault();
		console.log($(this).children("input#hidden_emote"));
		postFunction(this, null);
	});
});