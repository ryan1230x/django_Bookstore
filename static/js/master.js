$(document).ready(function(){
  $("#sidenav-btn").on("click", () => {
    $("#sidenav").css({'width':'300px'})
  });
  $("#close-btn").on("click", () => {
    $("#sidenav").css({'width': '0px'})
  });
});

