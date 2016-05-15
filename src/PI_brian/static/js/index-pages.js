$(document).ready(function(){
    var $pages = $("section[data-index-page]");
    var height =  $(window).height() - $("#cabecera").height();
    // La altura de cada sección se corresponde con lo que se ve en el total de la ventana.
    $pages.css("height", height+"px");
});