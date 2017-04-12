<!doctype html>
<html>
<head><title>UVa CS ugrads.cs auto-deploy page</title><meta http-equiv="content-type" content="text/html; charset=utf-8"></head>
<body>
<h2>UVa CS ugrads.cs auto-deploy page</h2>
<hr>
<?php
ob_end_flush();
flush();
$commands = array('git pull', '/bin/rm -rf output','mkdir output','touch output/empty','touch output/.gitignore','git checkout output/.gitignore','pelican content','cp instagram.png output/theme/images/icons/','patch output/theme/css/main.css instagram.patch','/bin/rm -rf ../ugrads','cp -a output ../ugrads');
$commanddir = "/home/www/ugrads.cs";
$path = "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin";

$date = date("Y-m-d H:i:s");
$fp = fopen("log.txt","a");
fprintf($fp,"Called from " . $_SERVER['REMOTE_ADDR'] . " at $date\n");
fclose($fp);

foreach ( $commands as $c ) {
	$cmd = "cd $commanddir; export PATH=$path; $c";
	echo "<p>Command: $cmd</p><pre>";
	echo `$cmd`;
	echo "</pre><hr>\n";
	flush();
}

$fp = fopen("log.txt","a");
fprintf($fp,"\tcompleted from " . $_SERVER['REMOTE_ADDR'] . "; started at $date; ended at " . date("Y-m-d H:i:s") . "\n");
fclose($fp);

?>
</body></html>
