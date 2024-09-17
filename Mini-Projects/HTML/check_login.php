<?php

if(!isset($_POST['submit']) || !isset($_POST['username']) || !isset($_POST['password']) || empty($_POST['username']) || empty($_POST['password'])) {
    echo " Login Error ";
}else {
    $username = $_POST["username"];
    echo "Welcome $username";
}
?>
