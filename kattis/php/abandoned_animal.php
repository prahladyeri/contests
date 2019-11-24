<?php
fscanf(STDIN, '%d', $n);
fscanf(STDIN, '%d', $k);
$stores = array();
for($i=0; $i<$k; $i++) {
	fscanf(STDIN, "%d %s", $j, $ss);
	//$ss = explode(" ", $ss);
	//$j = $ss[0];
	//print_r($ss);
	if (!isset($stores[$j])) $stores[$j] = array();
	array_push($stores[$j], $ss);
	//add item to array
	//if (!isset($items[$ss])) array_push($items, $ss);
}

fscanf(STDIN, '%d', $m); //no. of items purchased
for($i=0; $i<$m; $i++) {
	fscanf(STDIN, "%s", $ss);
	//echo "\";
}

print_r($stores);
