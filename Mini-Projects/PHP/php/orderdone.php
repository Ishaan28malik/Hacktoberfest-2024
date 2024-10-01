<?php
/* Attempt MySQL server connection.*/ 
require_once 'connection/connect.php';
$mid = 0;

$link = mysqli_connect($servername, $username, $password, $dbname);
 
// Check connection
if($link === false){
    die("ERROR: Could not connect. " . mysqli_connect_error());
}
 
// Escape user inputs for security
$quan= mysqli_real_escape_string($link,$_REQUEST['quantity']);

if($_GET['mid']){
    $mid = $_GET['mid'];

  }
 
// Attempt insert query execution
$sql2 = "SELECT pname FROM products where pid=$mid";
//$result = mysqli_real_escape_string($link,$sql2);
$row_pro=mysqli_fetch_array($sql2);
$sql = "INSERT INTO orders(prodname, quantity) VALUES ('$row_pro','$quan')";
if(mysqli_query($link, $sql)){
    //echo "Records added successfully.";
	//echo "added : ","Name : $name ","Phone : $phone ","Email : $email ","Password : $password";
	header("location:orderconfirm.html");
} else{
    echo "ERROR: Could not able to execute $sql. " . mysqli_error($link);
}
 
// Close connection
mysqli_close($link);
?>