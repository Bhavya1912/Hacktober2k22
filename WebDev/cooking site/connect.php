<?php
  $FullName=$_POST['FullName'];
  $Emaill=$_POST['Email'];
  $Review=$_POST['Review'];

  $conn= new mysqli('localhost','root','','Food_Store');
  if($conn->connect_error){
    die('Connection Failed :' .$conn->connect_error);
  }else{
    $stmt=$conn->prepare("insert into Review(Full Name,Email,Review) values(?,?,?)");
    $stmt->bind_param("sss",$FullName,$Email,$Review);
    $stmt->execute();
    echo "Review recorded successfully.....";
    $stmt->close();
    $conn->close();
  }
?>