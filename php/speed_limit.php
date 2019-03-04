<?php
$sets = array();
$cnt = 1;
while(true) {
	fscanf(STDIN, '%d', $n); if ($n == -1) break;
	$sets[$cnt] = array();
	for($i=0; $i<$n; $i++) {
		fscanf(STDIN, '%d %d', $s, $t);
		$sets[$cnt][$i] = array($s, $t);
	}
	$cnt++;
}

//print_r($sets);

for($i=1; $i<=count($sets); $i++) {
	$dist = 0;
	$currset = $sets[$i];
	for($j=0; $j<count($currset); $j++) {
		if ($j == 0) {
			$dist += ($currset[$j][0] * $currset[$j][1]);
		}
		else {
			$diff = $currset[$j][1] - $currset[$j-1][1];
			$dist += ($currset[$j][0] * $diff);
		}
	}
	echo "$dist miles" . ($i==count($sets) ? "" : "\n");
}
