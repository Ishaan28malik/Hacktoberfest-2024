<?php include 'server.php' ?>

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <style>
/* <?php include 'css/home.css'; ?> */
</style>
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <!-- <link rel="stylesheet" href="C:\xampp\htdocs\trekbuddy\css\home.css" type="text/css"> -->
    <link rel="stylesheet" href="../css/home.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <title>Home</title>
  </head>

  <body >
    <!--start navigation-->
    <!-- A grey horizontal navbar that becomes vertical on small screens -->
    <nav class="navbar navbar-expand-md bg-dark navbar-dark fixed-top">
      <!-- Brand /logo -->
      <a class="navbar-brand" href="#">TREKBUDDY</a>
    
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

  <!--Image slider-->
  <div id="demo" class="carousel slide" data-ride="carousel">
      <ul class="carousel-indicators">
        <li data-target="#demo" data-slide-to="0" class="active"></li>
        <li data-target="#demo" data-slide-to="1"></li>
        <li data-target="#demo" data-slide-to="2"></li>
      </ul>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="images/trek1.jpg" alt="Los Angeles" width="2100" height="750">
          <div class="carousel-caption">
            <p>We had such a great time</p>
          </div>   
        </div>
        <div class="carousel-item">
          <img src="images/trek2.jpg" alt="Chicago" width="2100" height="750">
          <div class="carousel-caption">
            <p>Thank you, Chicago!</p>
          </div>   
        </div>
        <div class="carousel-item">
          <img src="images/trek4.jpg" alt="New York" width="2100" height="750">
          <div class="carousel-caption">
            <p>We love the Big Apple!</p>
          </div>   
        </div>
      </div>
      <a class="carousel-control-prev" href="#demo" data-slide="prev">
        <span class="carousel-control-prev-icon"></span>
      </a>
      <a class="carousel-control-next" href="#demo" data-slide="next">
        <span class="carousel-control-next-icon"></span>
      </a>
    </div>

    <!--what do we offer-->
      <div class="container text">
        <div class="row text-center">
          <div class="col offer">
            <h1 >What Do We Offer</h1>
            <hr>
          </div>
          </div>
          <div class="col text">
            <p class="lead text-center" >We do whatever makes people happy, <br>mostly travel because that’s something we do best,<br> creating cherishable memories and priceless smiles.</p>
          </div>
      </div>

      <!--4 sections-->
      <div class="container section">
        <div class="row ">
          <div class="col">
            <div class="image1">
            <img src="images/corporate.png" >
            </div>
            <h3>CORPORATE TRIPS</h3>
          </div>
              <div class="col">
                  <div class="image2">
                 <img src="images/collegevisit.png" >
                    </div>
                <h3>COLLEGE VISITS</h3>
              </div>
                  <div class="col">
                      <div class="image3">
                      <img src="images/holiday.png" >
                      </div>
                    <h3>HOLIDAY TRIPS</h3>
                  </div>
              <div class="col">
                  <div class="image4">
                  <img src="images/treks&camping.png" >
                </div>
                    <h3>TREKS & CAMPING</h3>
                    </div>
        </div>
      </div>

      <!--reviews section-->
      <!--Image slider-->
  <div id="reviews" class="carousel slide" data-ride="carousel">
      <ul class="carousel-indicators">
        <li data-target="#reviews" data-slide-to="0" class="active"></li>
        <li data-target="#reviews" data-slide-to="1"></li>
        <li data-target="#reviews" data-slide-to="2"></li>
      </ul>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="images/review1.png" alt="Los Angeles" width="2100" height="750">
          <div class="carousel-caption">
          </div>   
        </div>
        <div class="carousel-item">
          <img src="images/review2.png" alt="Chicago" width="2100" height="750">
          <div class="carousel-caption">
            
          </div>   
        </div>
        <div class="carousel-item">
          <img src="images/review3.png" alt="New York" width="2100" height="750">
          <div class="carousel-caption">
            
          </div>   
        </div>
      </div>
      <a class="carousel-control-prev" href="#demo" data-slide="prev">
        <span class="carousel-control-prev-icon"></span>
      </a>
      <a class="carousel-control-next" href="#demo" data-slide="next">
        <span class="carousel-control-next-icon"></span>
      </a>
    </div>
      <!--reviews section-->

      <!--blog section-->
      <div class="container section-title">
        <h3 class="section-title section-title-center ">         
          <span class="section-title-main">LATEST BLOGS</span>
          <hr>
        </h3>
      </div>

      <!--blog pics-->
      <div class="container blog-section">
          <div class="row ">
            <div class="lg-col">
         
     <div class="row">
        <div class="col-md-4">
           <div class="card">
              <img class="card-img-top" src="images/lonavala6.jpg" alt="Card image cap" height="290px">
              <div class="card-body">
                 <h5 class="card-title border-bottom pb-3">Lonavala-Hill Stations</h5>
                 <p class="card-text">Picturesque points and small caves are what make any hill station worth the money. Lonavala does not fall behind in the..</p>
                 <a href="lonavala.php" class="btn btn-sm btn-info float-right">Read more <i class="fas fa-angle-double-right"></i></a>
              </div>
           </div>
        </div>
        <div class="col-md-4">
           <div class="card">
              <img class="card-img-top" src="images/solangvalley3.jpg" alt="Card image cap">
              <div class="card-body">
                 <h5 class="card-title border-bottom pb-3">5 Things To Do In Solang Valley</h5>
                 <p class="card-text">Secluded beaches and open sandland can do wonders. It can set you free just like a mountain but mountains...</p>
                 <a href="solangvalley.php" class="btn btn-sm btn-info float-right">Read more <i class="fas fa-angle-double-right"></i></a>
              </div>
           </div>
        </div>
        <div class="col-md-4">
           <div class="card ">
              <img class="card-img-top" src="images/jaisalmer.jpg" alt="Card image cap">
              <div class="card-body">
                 <h5 class="card-title border-bottom pb-3">Jaisalmer Desert Camping</h5>
                 <p class="card-text">If you have grown up watching Satyajit Ray’s ‘Feluda’, then you would know why Jaisalmer is important...</p>
                 <a href="jaisalmer.php" class="btn btn-sm btn-info float-right">Read more <i class="fas fa-angle-double-right"></i></a>
              </div>
           </div>
        </div>
     </div>
            </div>
                
          </div>
        </div>
     
        

  <!-- Copyright -->
  <div class="footer">
  <p>TrekBuddy</p>
</div>
  <!-- Copyright -->

</footer>
<!-- Footer -->
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>




