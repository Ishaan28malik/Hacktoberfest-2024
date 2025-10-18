<?php
session_start();
//db connection
require_once 'connection/connect.php';
	
	/*if($con){
		echo "Connection sucesfull";
	}else{
		echo "Not connected";
	}
	*/
    mysqli_select_db($con, 'trekbuddy');
    if(isset($_POST['login'])){
    $username = $_POST['loginEmail'];
	$password = @hash('sha256', $_POST['loginPassword']);
  //  echo $username;
	$q = "select * from users where email='$username' && password='$password'";
	//echo $password;
	$result = mysqli_query($con, $q);
	$num = mysqli_num_rows($result);
	if($num==1){
		header("location:index2.php"); //redirects
    //echo "<script> alert('login succesfully!')</script> ";	
    //echo "<script> window.location.assign('index.php')</script>";	
	//}
	}
	else{
		echo "<script> alert('Invalid Login Credentials')</script>";
    }
	//if(mysqli_query($con, $q)){
    //echo "Records added successfully.";
	//echo "added : ","Name : $name ","Phone : $phone ","Email : $email ","Password : $password";
	//header("location:index.php");
//} else{
  //  echo "ERROR: Invalid login credentials $q. " . mysqli_error($con);
//}
}
?>
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <title>signin</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <!-- <link rel="stylesheet" href="SignIn/assets/css/Pretty-Login-Form.css">
    <link rel="stylesheet" href="SignIn/assets/css/styles.css"> -->
</head>

<body>
    <nav class="navbar navbar-light navbar-expand-md justify-content-lg-end">
        <div class="container-fluid"><a class="navbar-brand" href="index.html" style="width: 121px;height: 40px;background-position: top;background-size: contain;background-image: url(&quot;SignIn/assets/img/logo.svg&quot;);background-repeat: no-repeat;"></a><button data-toggle="collapse"
                class="navbar-toggler" data-target="#navcol-1"><span class="sr-only">Toggle navigation</span><span class="navbar-toggler-icon"></span></button>
            <div class="collapse navbar-collapse justify-content-lg-end" id="navcol-1">
                <ul class="nav navbar-nav">
                    <li class="nav-item" role="presentation"><a class="nav-link active" href="laptopdesc.html">Laptops &amp; PCs</a></li>
                    <li class="nav-item" role="presentation"><a class="nav-link" href="mobiledesc.html" style="color: #000000;">Smartphones</a></li>
                    <li class="nav-item" role="presentation"><a class="nav-link" href="earphone.html" style="color: #000000;">Earphones</a></li>
                    <li class="nav-item" role="presentation"><a class="nav-link" href="sigin.php" style="color: #ffffff;background-color: #190062;">Sign In</a></li>
                </ul>
            </div>
        </div>
    </nav>
    <div class="row login-form">
        <div class="col-md-4 offset-md-4">
            <h2 class="text-center form-heading">Login Form</h2>
            <form class="custom-form" method="POST">
                <div class="form-group"><input name="loginEmail" class="form-control" type="email" placeholder="Email" required=""></div>
                <div class="form-group"><input name="loginPassword" class="form-control" type="password" placeholder="Password" required=""></div>
                <div class="form-check"><input class="form-check-input" type="checkbox" id="formCheck-6" ><label class="form-check-label" for="formCheck-6">Remember me</label></div><button name="login" class="btn btn-light btn-block submit-button" type="submit-button" style="background-color: #190062;">Sign In</button></form>
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>

</html>