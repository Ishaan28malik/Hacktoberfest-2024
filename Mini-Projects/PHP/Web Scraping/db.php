<?php

    $servername = "localhost";
    $username = "debian-sys-maint";
    $password = "CMh8AaggOu6EyKho";
    $dbName  = "scrapingDB";

    // Create connection    
    $conn = new mysqli($servername, $username, $password, $dbName);

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);  
    }
    echo "Connected successfully";

    // Create database
    // $sql = "CREATE DATABASE scrapingDB";
    // if ($conn->query($sql) === TRUE) {
    //     echo "Database created successfully";
    // } else {
    //     echo "Error creating database: " . $conn->error;
    // }

    // $conn->close();

    // sql to create table
    // $sql = "CREATE TABLE FanOfTMBData (
    //     id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    //     title VARCHAR(30) NOT NULL,
    //     icon VARCHAR(30) NOT NULL
    //     )";
        
    // if ($conn->query($sql) === TRUE) {
    //     echo "Table MyGuests created successfully";
    // } else {
    //     echo "Error creating table: " . $conn->error;
    // }

?>