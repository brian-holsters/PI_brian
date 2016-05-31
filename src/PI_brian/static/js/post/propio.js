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
});