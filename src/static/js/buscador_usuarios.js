$(document).ready(function(){
    $("#select2-buscador-usuarios").select2({
        ajax: {
            url : url_buscador, //esto se recibe desde la plantilla!
            dataType : "json",
            method: "get",
            delay: 250,
            data : function(params){
                return {
                    usuario: params.term,
                    page: params.page
                };
            },
            processResults: function(data, params){
                console.log("processResults");
                params.page = params.page || 1;
                return {
                    results: data.response,
                    pagination: {
                        more: (params.page * 30) < data.total_count
                    }
                };
            },
            cache: true
        },/*FIN AJAX*/

        escapeMarkup: function(markup){
        console.log("escapeMarkup");
        console.log(markup);
            return markup;
        },
        minimumInputLength: 1,
        templateResult: function(object){
            console.log("templateResult");
            console.log(object);
            if(object.nombre){
                return "<a class='block-link' href='/perfil/" + object.nombre + "'><span>" + object.nombre + "</span></a>";
            }
            return "buscando";
        },
        templateSelection: function(cosas){
            console.log("templateSelection");
            console.log(cosas);
            return cosas.nombre || "Buscar Usuario";
        },
    });
});