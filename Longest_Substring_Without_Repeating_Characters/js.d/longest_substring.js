/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s){
    var lastIndex = Array(256).fill(-1);
    const n = s.length;
    var maxSubstrLen = 0;
    var i = 0;

    for (let j=0; j<n; j++){
        i = Math.max(i, lastIndex[s[j].charCodeAt()] + 1);
        maxSubstrLen = Math.max(maxSubstrLen, j - i + 1);
        lastIndex[s[j].charCodeAt()] = j;
    }
    return maxSubstrLen;
};

/***********Test-Driver************
***********************************/
/**
 * @param {string} s
 * @param {int} res
 * @return {bool}
 */
var functionValidate = function(s, res){
    var resValid = lengthOfLongestSubstring(s) == res;
    if (resValid){
      console.log(`String "${s}" showing correct result => ${res}`);
    } else {
      console.log(`[Error]: Incorrect result for "${s}" => ${res}`);
    }
    return resValid;
}

const stringResMap = {
  "abcabcbb": 3,
  "bbbbb": 1,
  "pwwkew": 3,
  "abcdefg": 7,
  "aab": 2,
  "dvdf": 3
}

for (const [key, value] of Object.entries(stringResMap)) {
  functionValidate(key, value);
}
/***********End-Test************
********************************/
