<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Transaction Details</title>
    <link rel="stylesheet" href="./style.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    
    <style>
       

        h2{
            margin-top:30px;
            color: #0A6F6B;
        }

        
    </style>
</head>
<body class="indexPage">

<nav class="navbar navbar-expand-md bg-dark navbar-dark navStyle ">
        <a class="navbar-brand nava" href="#">Credit Management System</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="collapsibleNavbar">
            <ul class="navbar-nav">
            <li class="nav-item">
                <a class="nav-link nava" href="./index.php">Home</a>
            </li>
            <li class="nav-item">
                <a class="nav-link nava" href="./viewusers.php">View All Users</a>
            </li>
            <li class="nav-item">
                <a class="nav-link nava" href="./transactionDetails.php">Transaction History</a>
            </li>    
            </ul>
        </div>  
     </nav>
        <div class="container divStyle">
        <h2 class="text-center">Transaction History</h2>
        
       <br>
       <div class="table-responsive-sm">
    <table class="table text-center table-striped table-hover tableStyle ">
            <thead>
            <tr>
            <th>Id</th>
            <th>Sender</th>
            <th>Receiver</th>
            <th>Credits</th>
        
            </tr>
        </thead>
        <tbody>
            <?php

            include 'config.php';

            $sql ="select * from transaction";

            $query =mysqli_query($conn, $sql);

            while($rows = mysqli_fetch_array($query))
            {
                ?>
            <tr>
            <td><?php echo $rows['id']; ?></td>
            <td><?php echo $rows['sender']; ?></td>
            <td><?php echo $rows['receiver']; ?></td>
            <td><?php echo $rows['amount']; ?> </td>
                
            <?php
            }

            ?>
            


        </tbody>
    </table>
    </div>
        </div>
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>

</body>
</html>