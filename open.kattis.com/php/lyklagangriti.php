<?php
$l=[]; $r =[]; $ss = '';
//fscanf(STDIN, "%s", $ss);
$ss = fgets(STDIN);
// $fin = fopen ("php://stdin","r");
// $ss = fgets($fin);

// echo $ss . ":: size:";
// echo strlen($ss);
// echo "\n";
foreach(str_split($ss) as $c) {
	//echo "char==" .$c . "::" . ord($c) . "\n";
	switch($c) {
    case 'L':
        $item = array_pop($l);
		array_unshift($r, $item); //add to beginning
		break;
    case 'R':
        $item = array_shift($r);
		array_push($l, $item);
		break;
    case 'B':
		array_pop($l);
		break;
	case chr(13):
		//echo 'skip 13';
		break;
	case chr(10):
		//echo 'skip 10';
		break;
    default:
		array_push($l, $c);
	}
}
echo implode("", $l) . implode("", $r);