// Function for the tooltips
$(function(){
  $('[data-toggle="tooltip"]').tooltip();
});

// Button click functions
$(document).on("click", "#btn-1", function(){
  $("#generated-code").text("You have clicked button number 1!");
});

$(document).on("click", "#btn-2", function(){
  $("#generated-code").text("You have clicked button number 2!");
});

$(document).on("click", "#btn-3", function(){
  $("#generated-code").text("You have clicked button number 3!");
});

$(document).on("click", "#btn-4", function(){
  $("#generated-code").text("You have clicked button number 4!");
});

$(document).on("click", "#btn-5", function(){
  $("#generated-code").text("You have clicked button number 5!");
});
