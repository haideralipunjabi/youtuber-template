$(document).ready(function(){
  $("#navbar-container").load("navbar.html", function(){
    Bulma.traverseDOM();
});
  $("#footer-container").load("footer.html");
});
