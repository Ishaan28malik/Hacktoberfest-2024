
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <title>Sign Up Trekbuddy</title>
    <link rel="stylesheet" href="Signup/assets/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="Signup/assets/css/Pretty-Registration-Form.css">
    <link rel="stylesheet" href="Signup/assets/css/styles.css">
</head>

<body>
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
    <div class="row register-form">
        <div class="col-md-8 offset-md-2">
            <form class="custom-form" action="reg.php" method="POST">
                <h1>Create an account.</h1>
                <div class="form-row form-group">
                    <div class="col-sm-4 label-column"><label class="col-form-label" for="name-input-field">Name </label></div>
                    <div class="col-sm-6 input-column"><input name='name' class="form-control" type="text" required=""></div>
                </div>
                <div class="form-row form-group">
                    <div class="col-sm-4 label-column"><label class="col-form-label" for="dropdown-input-field">Phone</label></div>
                    <div class="col-sm-4 input-column"><input name='phone' class="form-control" type="tel" required=""></div>
                </div>
                <div class="form-row form-group">
                    <div class="col-sm-4 label-column"><label class="col-form-label" for="email-input-field">Email </label></div>
                    <div class="col-sm-6 input-column"><input name='email' class="form-control" type="email" required=""></div>
                </div>
                <div class="form-row form-group">
                    <div class="col-sm-4 label-column"><label class="col-form-label" for="pawssword-input-field">Password </label></div>
                    <div class="col-sm-6 input-column"><input name='password' class="form-control" type="password" required=""></div>
                </div>
                <!--<div class="form-row form-group">
                    <div class="col-sm-4 label-column"><label class="col-form-label" for="repeat-pawssword-input-field">Repeat Password </label></div>
                    <div class="col-sm-6 input-column"><input name='password2' class="form-control" type="password" required=""></div>
                </div>-->
                <div class="form-check"><input class="form-check-input" type="checkbox" id="formCheck-1" required=""><label class="form-check-label" for="formCheck-1">I've read and accept the terms and conditions</label></div><button class="btn btn-light submit-button" name="reg_user" type="submit-button"
                    style="background-color: #190062;">Sign Up</button></form>
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script></body>

</html>