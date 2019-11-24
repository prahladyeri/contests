<?php
fscanf(STDIN, "%d", $n);

$qaly = 0;
for ($i=0; $i<$n; $i++) {
	fscanf(STDIN, "%f %f", $q, $y);
	$qaly += ($q*$y);
	//echo "q=$q, y=$y, qaly=$qaly\n";
}

echo number_format($qaly, 3, ".", "");
