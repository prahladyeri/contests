<?php
fscanf(STDIN, '%f', $cost);
fscanf(STDIN, '%f', $num_lawns);
$lawns = array();

for($i=0; $i<$num_lawns; $i++) {
	fscanf(STDIN, '%f %f', $width, $length);
	$lawns[$i] = $width * $length * $cost;
	//echo "w l c: $width, $length, $cost::" . $lawns[$i] . "\n";
}

//print_r($lawns);
echo number_format(array_sum($lawns), 7, '.', '');
