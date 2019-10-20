$("ul").on("click","li",function(){
	if($(this).css("color") == "rgb(128, 128, 128)"){
		$(this).css({
			color : "black",
		    textDecoration : "none",
		});
	}else{
		$(this).css({
			color : "gray",
		    textDecoration : "line-through",
		});
	}
});

$("ul").click("span",function(e){
	$(this).fadeOut(500);
	e.stopPropagation();
})
$("input[type =text]").keypress(function(e){
      if (e.which === 13){
          var todoText =$(this).val();
          $(this).val("");
          $("ul").append("<li><span><i class='fa fa-trash'></i></span>"+todoText+"</li>");
          
      }
});
$(".fa-plus").on("click",function(){
	$("input[type =text]").fadeToggle();
})