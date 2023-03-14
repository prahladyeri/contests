<?php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function romanToInt($s) {
		$lookup= array(
			'I'=>1,
			'V'=>5,
			'X'=>10,
			'L'=>50,
			'C'=>100,
			'D'=>500,
			'M'=>1000,
		);
		$sum=0;
        for($i=0; $i<strlen($s); $i++) {
			$c = substr($s, $i, 1);
			//check exceptional situations:
			$last = ($i==(strlen($s)-1));
			if(!$last) $n = substr($s, $i+1, 1);
			if (!$last && $c=='I' && $n=='V') {
				$sum += 4;
				$i++;
				continue;
			}
			else if (!$last && $c=='I' && $n=='X') {
				$sum += 9;
				$i++;
				continue;
			}
			else if (!$last && $c=='X' && $n=='L') {
				$sum += 40;
				$i++;
				continue;
			}
			else if (!$last && $c=='X' && $n=='C') {
				$sum += 90;
				$i++;
				continue;
			}
			else if (!$last && $c=='C' && $n=='D') {
				$sum += 400;
				$i++;
				continue;
			}
			else if (!$last && $c=='C' && $n=='M') {
				$sum += 900;
				$i++;
				continue;
			}
			
			//normal situations:
			$sum += (int)$lookup[$c];
		}
		return $sum;
    }
}

echo Solution::romanToInt("LVIII");
//echo Solution::romanToInt("MCMXCIV");