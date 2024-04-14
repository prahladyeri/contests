<?php
$symbols = ["@", "8", '(', '|)', '3', '#', '6', '[-]', '|', '_|', '|<', '1', '[]\/[]'];
$symbols = array_merge($symbols, ['[]\[]', '0', '|D', '(,)', '|Z', '$', "']['", '|_|', '\/', '\/\/', '}{', '`/', '2']);


$ss;
fscanf(STDIN, "%[^\n]", $ss);
$ss = strtolower($ss);
#echo "ss:" . $ss;
$out = "";
foreach(str_split($ss) as $c)  {
    $o = ord($c);
    if ($o>=97 and $o<=122)
        $out .= $symbols[$o-97];
    else
        $out .= $c;
}
echo $out;