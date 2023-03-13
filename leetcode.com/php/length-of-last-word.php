<?php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function lengthOfLastWord($s) {
        $a=explode(' ', trim($s));
		$word = $a[count($a)-1];
		return strlen($word);
    }
}


//echo Solution::lengthOfLastWord("Hello World");
echo Solution::lengthOfLastWord("   fly me   to   the moon  ");