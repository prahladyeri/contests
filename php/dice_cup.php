<?php
fscanf(STDIN, '%d %d', $n, $m);

//generate probabilities
$probs = array();
for($i=1;$i<=$n;$i++) {
	for($j=1;$j<=$m;$j++) {
		$sum = $i+$j;
		$probs[$sum] = (isset($probs[$sum])) ? $probs[$sum] + 1 : 1;
	}
}

//convert probabilities to percentages
foreach($probs as $key=>$item) {
	$probs[$key] = round($item/count($probs)*100, 2);
}

//filter the maximum probabilities
arsort($probs);
$maxprob = reset($probs);
$new = array_filter($probs, function($val) use ($maxprob) {
	return ($val === $maxprob);
	});

ksort($new);
foreach($new as $key=>$value) {
	echo "$key\n";
}
