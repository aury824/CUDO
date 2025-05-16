<?php
// vulnerable.php
$filename = $_GET['page'];
include($filename); // ./?page=../../../../etc/passwd
?>
