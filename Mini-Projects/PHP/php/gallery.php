<!doctype html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  <link rel="stylesheet" href="C:\Users\omkar\Desktop\trekbuddy\gallerycss.css">

  <title>Gallery</title>
  <style>
      * {
        box-sizing: border-box;
      }
      
      body {
        margin: 0;
        font-family: Arial, Helvetica, sans-serif;
      }
      
      .header {
        text-align: center;
        padding: 32px;
      }
      
      .row {
        display: -ms-flexbox; /* IE 10 */
        display: flex;
        -ms-flex-wrap: wrap; /* IE 10 */
        flex-wrap: wrap;
        padding: 0 4px;
      }
      
      /* Create two equal columns that sits next to each other */
      .column {
        -ms-flex: 50%; /* IE 10 */
        flex: 50%;
        padding: 0 4px;
      }
      
      .column img {
        margin-top: 8px;
        vertical-align: middle;
      }
      
      /* Style the buttons */
      .btn {
        border: none;
        outline: none;
        padding: 10px 16px;
        background-color: #f1f1f1;
        cursor: pointer;
        font-size: 18px;
      }
      
      .btn:hover {
        background-color: #ddd;
      }
      
      .btn.active {
        background-color: #666;
        color: white;
      }
      </style>
          

</head>

<body>

  <!-- Header -->
<div class="header" id="myHeader" style="padding-top: 100px">
    <h1>Image Grid</h1>
    <p>Click on the buttons to change the grid view.</p>
    <button class="btn" onclick="one()">1</button>
    <button class="btn active" onclick="two()">2</button>
    <button class="btn" onclick="four()">4</button>
  </div>
  

  <!--start navigation-->
  <!-- A grey horizontal navbar that becomes vertical on small screens -->
  <nav class="navbar navbar-expand-md bg-dark navbar-dark fixed-top">
    <!-- Brand /logo -->
    <a class="navbar-brand" href="#">TREK BUDDY</a>

    <!-- Toggler/collapsibe Button -->
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive">
      <span class="navbar-toggler-icon"></span>
    </button>
    <!-- Navbar links -->
    <div class="collapse navbar-collapse" id="navbarResponsive">
      <ul class="navbar-nav ml-auto">
        <li class="nav-item">
          <a class="nav-link" href="home.php">HOME</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="aboutus.php">ABOUT US</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="signup.php">SIGN UP</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="gallery.php">GALLERY</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="trips.php">TRIPS & TREKS</a>
        </li>
      </ul>
    </div>
  </nav>
  <!--end navigation-->

  <!--Image Gallery-->
  <div class="row"> 
      <div class="column">
        <img src="images/Rajmachi-Fort.jpg" style="width:100%">
        <img src="images/trek2.jpg" style="width:100%">
        <img src="images/thumbs_20180714_102339-e1561353913829.jpg" style="width:100%">
        <img src="images/trek4.jpg" style="width:100%">
        <img src="images/Valley-Of-Flowers-768x525.jpg" style="width:100%">
        <img src="images/thumbs_IMG_20180701_111358.jpg" style="width:100%">
        <img src="images/jaisalmer2.jpg" style="width:100%">
      </div>
      <div class="column">
          <img src="images/solangvalley.jpg" style="width:100%">
          <img src="images/lonavala.jpg" style="width:100%">
          <img src="images/jaisalmer3.jpg" style="width:100%">
          <img src="images/solangvalley3.jpg" style="width:100%">
          <img src="images/Garbett.jpg" style="width:100%">
          <img src="images/lonavala5.jpg" style="width:100%">
          <img src="images/Movie.jpg" style="width:100%">
        </div>
        <div class="column">
            <img src="images/solangvalley2.jpg" style="width:100%">
            <img src="images/lonavala4.jpg" style="width:100%">
            <img src="images/jaisalmer4.jpg" style="width:100%">
            <img src="images/Stargazing-1-768x420.jpg" style="width:100%">
            <img src="images/Tung-Fort.jpg" style="width:100%">
            <img src="images/lonavala2.jpg" style="width:100%">
            <img src="images/Paragliding-768x432.png" style="width:100%">
          </div>
          <div class="column">
              <img src="images/gokarna.jpg" style="width:100%">
              <img src="images/lonavala3.jpg" style="width:100%">
              <img src="images/lonavala4.jpg" style="width:100%">
              <img src="images/Tarkarli.jpg" style="width:100%">
              <img src="images/Sandhan-Valley-768x420.jpg" style="width:100%">
              <img src="images/thumbs_20180714_102339-e1561353913829.jpg" style="width:100%">
              <img src="images/thumbs_IMG_20180701_111358.jpg" style="width:100%">
            </div>
      </div>
      
  <!-- Optional JavaScript -->
  <!-- jQuery first, then Popper.js, then Bootstrap JS -->
  <script>

  // Get the elements with class="column"
var elements = document.getElementsByClassName("column");

// Declare a loop variable
var i;

// Full-width images
function one() {
    for (i = 0; i < elements.length; i++) {
    elements[i].style.msFlex = "100%";  // IE10
    elements[i].style.flex = "100%";
  }
}

// Two images side by side
function two() {
  for (i = 0; i < elements.length; i++) {
    elements[i].style.msFlex = "50%";  // IE10
    elements[i].style.flex = "50%";
  }
}

// Four images side by side
function four() {
  for (i = 0; i < elements.length; i++) {
    elements[i].style.msFlex = "25%";  // IE10
    elements[i].style.flex = "25%";
  }
}

// Add active class to the current button (highlight it)
var header = document.getElementById("myHeader");
var btns = header.getElementsByClassName("btn");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}

  

  </script>
  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
    integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
    crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
    integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"
    crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
    integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"
    crossorigin="anonymous"></script>
</body>

</html>