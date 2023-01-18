<?php 

function StringChallenge($str) {
  $length = strlen($str);
  // echo $str[4];
  $n= round($length/2)-1;
  $j = (int)round($length/2);
  $result="";
  for($i = 0 ; $i<$n;$i++){
    $result = $result . $str[$i] . $str[$j];
    $j=$j+1;
  }

  $ChallengeToken = "9hm8p3efc0";
  $result = $result . $ChallengeToken;
  $k=4;
  while(isset($result[$k-1])){
    $result[$k-1]= "_";
    $k= $k+4;
    // echo $k;
  }
  return $result;
  // code goes here
  // return $str;

}
   
// keep this function call here  
echo StringChallenge(fgets(fopen('php://stdin', 'r')));  



// ///
// String Merge
// HIDE QUESTION
// Have the function StringMerge(str) read the str parameter being passed which will contain a large string of alphanumeric characters with a single asterisk character splitting the string evenly into two separate strings. Your goal is to return a new string by pairing up the characters in the corresponding locations in both strings. For example: if str is "abc1*kyoo" then your program should return the string akbyco1o because a pairs with k, b pairs with y, etc. The string will always split evenly with the asterisk in the center.

// Once your function is working, take the final output string and concatenate it with your ChallengeToken, and then replace every fourth character with an underscore.

// Your ChallengeToken: 9hm8p3efc0
// ///
  
  
  ?>
