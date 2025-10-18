<?php
session_start();
require_once 'connection/connect.php';
?>
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <title>Home - Brand</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Catamaran:100,200,300,400,500,600,700,800,900">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato:100,100i,300,300i,400,400i,700,700i,900,900i">
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
          display: -ms-flexbox; /* IE10 */
          display: flex;
          -ms-flex-wrap: wrap; /* IE10 */
          flex-wrap: wrap;
          padding: 0 4px;
        }

        /* Create four equal columns that sits next to each other */
        .column {
          -ms-flex: 25%; /* IE10 */
          flex: 25%;
          max-width: 25%;
          padding: 0 4px;
        }

        .column img {
          margin-top: 8px;
          vertical-align: middle;
          width: 100%;
        }

        /* Responsive layout - makes a two column-layout instead of four columns */
        @media screen and (max-width: 800px) {
          .column {
            -ms-flex: 50%;
            flex: 50%;
            max-width: 50%;
          }
        }

        /* Responsive layout - makes the two columns stack on top of each other instead of next to each other */
        @media screen and (max-width: 600px) {
          .column {
            -ms-flex: 100%;
            flex: 100%;
            max-width: 100%;
          }
        }
        /* Style the counter cards */
        .card {
          box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
          padding: 16px;
          text-align: center;
          background-color: #f1f1f1;
        }


        </style>
	
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

    <header class="masthead text-center text-white" style="background: linear-gradient(132.16deg, #190062 0%, #dd56cf 100%), #ffffff;/*background-image: url(&quot;null&quot;);*/">
        <div class="masthead-content" style="width: 100%;height: 100%;">
            <div class="container" style="width: 100%;height: 100%;">
                <h1 class="flex-shrink-1 masthead-heading mb-0" style="width: 100%;height: 100%;">Confirm Booking</h1>
                <h2 class="masthead-subheading mb-0">This is where we deliver happiness.</h2>
            </div>
        </div>
    </header>
    <section>
        <div class="container">
            <div class="row align-items-center">
            <?php
                $tablename = 'products';
                $mid = 0;
                if($_GET['id']){
                  $mid = $_GET['id'];

                }
                if(!isset($_GET[$tablename])){
                
                    global $con;
                    $get_pro = "select * from $tablename where pid=$mid";
                    $run_pro = mysqli_query($con, $get_pro);
                    $rowcount =0;

                    $row_pro=mysqli_fetch_array($run_pro);
                    $pid = $row_pro['pid'];
                    $pname = $row_pro['pname'];
                    $descp = $row_pro['descp'];
                    $price = $row_pro['price'];
                    $image = $row_pro['image'];
            
          echo "<div class='col-lg-6 order-lg-2' style='width: 100%;height: 100%;'>
                    <div class='p-5'><img src='images/$image' style='width: 100%;height: 100%;'></div>
                </div>
                <div class='col-lg-6 order-lg-1'>
                    <div class='p-5'>
                        <h2 class='display-4' style='height: 134px;margin-bottom: 100px;'>$pname<br></h2>
                        <p style='font-size: 17px;'>$descp<br><strong><em>$price</em></strong></p>
						<form class='custom-form' action='orderdone.php?mid=$mid' method='POST' >
                        <input name='quantity' required='' type='text' style='height: 35px;width: 104px;' placeholder='Quantity' inputmode='numeric'><br>
						
						<button name='doorder' class='btn btn-primary submit-button' type='submit' style='background-color: #190062;margin-top: 5px;'>Order</button>
						
						</form>
					</div>
                </div>";
              
              }
                ?>
            </div>
        </div>
        
    </section>
    <footer class="py-5 bg-black"></footer>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
	
</body>
</html>