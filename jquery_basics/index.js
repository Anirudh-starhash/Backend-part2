$("h1").css("color","red");

// $("h1").addClass("big-title");
// $("h1").removelass("big-title");

$("h1").click(function(){
    $("h1").css("color","purple");
})

$("button").click(function(){
    $("h1").css("color","purple");
})

$(document).keypress(function(event){
   $("h1").text(event.key);
});

$("h1").on("mouseover",function(){
    $("h1").css("color","purple");
});