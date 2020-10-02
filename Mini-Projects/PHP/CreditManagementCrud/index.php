<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="./style.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"
  />
  </head>
<body class="indexPage">

  <nav class="navbar navbar-expand-md navbar-dark navStyle ">
    <a class="navbar-brand nava" href="#">Credit Management System</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="collapsibleNavbar">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link nava" href="./index.php">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link nava" href="./viewusers.php">View All Users</a>
        </li>
        <li class="nav-item">
          <a class="nav-link nava" href="./transactionDetails.php">Transaction History</a>
        </li>    
      </ul>
    </div>  
  </nav>
  
  <div class="container">
    <img src="./images/credit2.jpg" width="400px" height="300px" class="image">
  </div>
  <div class="main">
    <h1  style="animation-delay: 1s">We Transfer <span>Your Credits</span></h1>
  <!-- <h2 class="animate__animated animate__fadeInUp" style="animation-delay: 1s">Credit <span>Management System</span></h2> -->
  <h4  style="animation-delay: 1s">Track Your <span>Transaction!</span></h4>
  
  <a href="./viewusers.php" class="btn btn1 " role="button">View Users And Transfer Credits</a><br>
  <a href="./transactionDetails.php" class="btn btn1 btn2 " role="button">Transaction Details</a>
  </div>
  <!-- <div class="animation-area">
    <ul class="box-area">
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
    </ul>
  </div> -->

    
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
</body>
</html>