<?php

$username = $_POST['username'];
$password = $_POST['password'];

if(!isset($_POST['submit'])) {
    echo " Login Error ";
}else {
    echo "Welcome $username";
}
?>