<?php

$server = 'fdb31.125mb.com';
$username = '3934392_wpress29e89a1e';
$password = 'Iot2021-3';
$database = '3934392_wpress29e89a1e';

try {
  $conn = new PDO("mysql:host=$server;dbname=$database;", $username, $password);
} catch (PDOException $e) {
  die('Connection Failed: ' . $e->getMessage());
}

?>
