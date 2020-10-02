<?php 

$dbhost = "localhost";
$dbuser = "id14996795_root";
$dbpass = "Mehendi@Shadi98";
$dbname = "id14996795_creditsystem";

$conn = mysqli_connect($dbhost, $dbuser, $dbpass, $dbname);

    if(!$conn){
        die("Could not connect to the Database".mysqli_connect_error());
    }

?>