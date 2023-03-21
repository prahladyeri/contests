<?php 
class Solution {

    /**
     * @param String[] $strs
     * @return String
     */
    function longestCommonPrefix($strs) {
		if (count($strs)==1) return $strs[0];
		if ($strs[0] == "") return "";
		sort($strs);
		$s1 = $strs[0];
		$s2 = $strs[count($strs)-1];
		$len = min(strlen($s1), strlen($s2));
		//echo "s1,s2,len::$s1 $s2 $len\n";
		for($i=0; $i<$len && $s1[$i]==$s2[$i]; $i++);
		//echo "i:".$i."\n";
		return substr($s1, 0, $i);
    }
}

//echo Solution::longestCommonPrefix(["flower","flow","flight"]);
//echo Solution::longestCommonPrefix(["dog","racecar","car"]);
//echo Solution::longestCommonPrefix([""]);
//echo Solution::longestCommonPrefix(["ab", "a"]);
echo Solution::longestCommonPrefix(["flower","flower","flower","flower"]);
