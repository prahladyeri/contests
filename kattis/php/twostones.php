<?php
fscanf(STDIN, '%d', $n);
//$temp = range(1, $n);
//$arr = array_combine($temp, $temp);
//print_r($arr);

$next_turn = "alice";
$left = $n;

for($i=1; $i<$n; $i++) {
	//echo "$i: $next_turn's turn.\n";
	$left -= 2;
	$i += 2;
	//print_r($arr);
	//echo "\n";
	$next_turn = ($next_turn=="alice" ? "bob" : "alice");
}

//echo "left: $left" , "\n";

//echo (count($arr) % 2 == 0 ? "Bob" : "Alice");
echo ($left % 2 == 0 ? "Bob" : "Alice");
