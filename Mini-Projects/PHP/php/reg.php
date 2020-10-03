<?php
/* Attempt MySQL server connection.*/ 
require_once 'connection/connect.php';


$link = mysqli_connect($servername, $username, $password, $dbname);
 
// Check connection
if($link === false){
    die("ERROR: Could not connect. " . mysqli_connect_error());
}
 
// Escape user inputs for security
$name= mysqli_real_escape_string($link,$_REQUEST['name']);
$phone=mysqli_real_escape_string($link,$_REQUEST['phone']);
$email = mysqli_real_escape_string($link, $_REQUEST['email']);
$password = mysqli_real_escape_string($link,  hash('sha256', $_REQUEST['password']));
##$password2 = mysqli_real_escape_string($link,  hash('sha256', $_REQUEST['password2']));
 
 
// Attempt insert query execution
$sql = "INSERT INTO users (name, phone, email, password) VALUES ('$name', '$phone', '$email', '$password')";
if(mysqli_query($link, $sql)){
    echo "Records added successfully.";
	echo "added : ","Name : $name ","Phone : $phone ","Email : $email ","Password : $password";
	header("location:home.php");
} else{
    echo "ERROR: Could not able to execute $sql. " . mysqli_error($link);
}
 
// Close connection
mysqli_close($link);
?>