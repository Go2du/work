/patient registration php code
<?php
  include ("include/connection.php");

  if(isset($_POST['create_account'])) {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $password = $_POST['password'];
    $confirm_password = $_POST['confirm_password'];

    // Basic validation
    if(empty($name) || empty($email) || empty($password) || empty($confirm_password)) {
      echo "All fields are required.";
    } elseif($password !== $confirm_password) {
      echo "<script>alert('Passwords do not match. Please try again.');</script>";
    } else {
      // Insert into database (assuming a table named 'patients')
      $query = "INSERT INTO patient (name, email, password, profile, date_reg) VALUES ('$name', '$email', '$password', 'patient.png', NOW())";
      if(mysqli_query($connect, $query)) {
       echo "<script>alert('Account created successfully');</script>";
      } else {
        echo "Error: " . mysqli_error($connect);
      }
    }
  }
?>
