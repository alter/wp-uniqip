<?php
$username = "wordpress";
$password = "SECRET";
$hostname = "localhost";	
$database = "wordpress";

$dbh = mysql_connect($hostname, $username, $password) 
	or die("Unable to connect to MySQL");
$selected = mysql_select_db($database,$dbh) 
	or die("Could not select database");
$result = mysql_query("select count(*) from uniqvisitors where date=curdate()");
while ($row = mysql_fetch_array($result,MYSQL_NUM)) {
	print $row[0]."<br />"; 
}
mysql_close($dbh);
?>
