<?php
while(fscanf(STDIN, '%d%d', $n1, $n2) === 2){
    //$ar = explode(" ",$input);
	$H = $n1;//$ar[0];
	$i = $n2;//rtrim($ar[1],"\r\n");
	//var_dump($ar);
	$H = sprintf("%02d", $H);
	$i = sprintf("%02d", $i);
	$s = "01-01-1972 $H:$i:00";
	
	//echo "$s\n";
	$d1 = DateTime::createFromFormat("d-m-Y H:i:s",$s); //mktime($h,$m,0,1,1,1971);
	$interval = new DateInterval("PT45M");
	$interval->invert =1;
	$d2 = $d1->add($interval);
	//var_dump($d2);
	$H = trim(sprintf("%2d",$d2->format("H")));
	$i = trim(sprintf("%2d",$d2->format("i")));
	echo "$H $i";
}