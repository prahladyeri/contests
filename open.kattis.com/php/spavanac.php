<?php
while(fscanf(STDIN, '%d%d', $n1, $n2) === 2){
	$H = $n1;
	$i = $n2;
	$H = sprintf("%02d", $H);
	$i = sprintf("%02d", $i);
	$s = "01-01-1972 $H:$i:00";
	
	$d1 = DateTime::createFromFormat("d-m-Y H:i:s",$s);
	$interval = new DateInterval("PT45M");
	$interval->invert =1;
	$d2 = $d1->add($interval);
	$H = trim(sprintf("%2d",$d2->format("H")));
	$i = trim(sprintf("%2d",$d2->format("i")));
	echo "$H $i";
}
