<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Users Details</title>
    <link rel="stylesheet" href="./style.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>
<body class="indexPage">
<?php
    require 'config.php';
    $query = "SELECT * FROM users";
    $result = mysqli_query($conn,$query);
?>

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
    <div class="container">
       
            <div class="row">
                <div class="col">
                    <div class="table-responsive-sm">
                    <table class="table table-hover tableStyle table-sm table-res">
                        <thead>
                            <tr>
                            <th scope="col">ID</th>
                            <th scope="col">Name</th>
                            <th scope="col">Email Id</th>
                            <th scope="col">Credits</th>
                            <th scope="col">Operations</th>
                            </tr>
                        </thead>
                        <tbody>
                <?php 
                    while($rows=mysqli_fetch_assoc($result)){
                ?>

                        <tr>
                        <td><?php echo $rows['id'] ?></td>
                        <td><?php echo $rows['name']?></td>
                        <td><?php echo $rows['email']?></td>
                        <td><?php echo $rows['credit']?></td> 
                        <td><a href="selectedUserdetail.php?id= <?php echo $rows['id'] ;?>"class="text-red"> <button type="button" class="btn btnStyle">View</button></a></td>

                    </tr>
                    <?php
                    }
                        ?>
            
                        </tbody>
                    </table>
                    </div>
                </div>
            </div>  
    
</div>


<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
</body>
</html>