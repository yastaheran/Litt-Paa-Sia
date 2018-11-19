//Hide all areas except selectionArea
$("#selectionArea, #specificationArea, #quizArea, #jokeArea, #alertArea").hide();

//dadjoke
var dadjoke = "";
$.getJSON("https://icanhazdadjoke.com/").done(function(result) {
  dadjoke = result.joke;
  document.getElementById("joke").innerHTML = dadjoke;
});

//Get list of all categories and append to the selectionArea
function selection() {
  $("#start").hide();
  $("#selectionArea").fadeIn("slow");
  //Get list of all categories and append to the selectionArea
  $.getJSON("https://icanhazdadjoke.com/").done(function(result) {
    dadjoke = result.joke;
    document.getElementById("joke2").innerHTML = dadjoke;
  });

  fetch("https://opentdb.com/api_category.php")
    .then(function(response) {
      return response.json();
    })
    .then(function(data) {
      var list = data.trivia_categories;
      list.forEach(function(quiz){
        var categoryList = document.getElementById("quizList");
        var listElement = document.createElement("li");
        var name = document.createTextNode(quiz.name);

        listElement.appendChild(name);
        listElement.setAttribute("id", quiz.id);
        listElement.setAttribute("class", "quiz");
        categoryList.appendChild(listElement);
      });

      //Adding eventListeners to trigger next page
      document.querySelectorAll(".quiz").forEach(function(quiz) {
       quiz.addEventListener("click", function() {
          toSpecification(quiz.id);
        });
      });
    })
    .catch(function(error) {
      handleFetchError(error);
    });
}
//Handles fetch errors
function handleFetchError(response) {
  $("#start, #selectArea, #specificationArea, #quizArea, #jokeArea").hide();
  $("#alertArea").show();
  $(".alert").html( "Something went wrong. We were unable to retrieve any quiz data.<br><br> <img src='http://placekitten.com/g/200/300' alt='Kitten' />");
}

//Quiz specification
function toSpecification(id) {
  var db= "https://opentdb.com/api.php",
      level = "",
      numberOfQs = 0;

  //Hide the current area and show the specificationArea
  $("#selectionArea, #start" ).hide();
  $("#specificationArea").fadeIn("slow");

  //Dadjoke
  $.getJSON("https://icanhazdadjoke.com/").done(function(result) {
    dadjoke = result.joke;
    document.getElementById("joke3").innerHTML = dadjoke;
  });

  //get input from user
  $("#generateQBtn").click(function() {
    level = $("#level").val();
    numberOfQs = $("#num").val();
    //get questions and pass quiz data
    var query = db + "?amount=" + numberOfQs + "&category=" + id + "&difficulty=" + level + "&type=multiple";

    getQuiz(query, "same-origin");
  });

}

function getQuiz(query) {
  fetch(query)
    .then(function(response) {
      return response.json();
    })
    .then(function(data) {
      quizAndJoke(data.results);
    })
    .catch(function(error) {
      handleFetchError(error);
    });
}

//Shows a new quiz with answers and jokes
function quizAndJoke(questions) {
  //show playlis and quiz area
  $("#specificationArea").hide();
  $("#quizArea, #jokeArea").fadeIn("slow");

  //variables
  var q = "";
  var a = "";
  var i = 1;
  //Display all questions
  $.each(questions, function() {
    console.log(i);
    q = this.question;
    a = this.correct_answer;
    $("#quizArea").append("<h3>Q: " + q + "</h3>" + "<p> A: " + a + "</p><br>");
    $.getJSON("https://icanhazdadjoke.com/").done(function(result) {
      dadjoke = result.joke;
      $("#jokeArea").append("<p>"+ i + ". " + dadjoke + "</p>");
      i++;
    });
  });


}
