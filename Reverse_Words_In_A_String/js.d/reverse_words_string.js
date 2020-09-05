
var reverseWords = function(s){
  s = s.trimEnd();
  s = s.trimStart();
  s = s.replace(/\s{2,}/g, ' ');
  let str_array = s.split(" ");
  str_array = str_array.reverse();
  return str_array.join(" ");
};

var test_strings = [
  "  a good  example  ",
  "the sky is blue",
  "  hello world!  ",
  " lots  of     spaces here    ",
  "1 ",
  " ",
  "",
  "  ",
  "    ",
  "a"
];

test_strings.map(x => console.log("_"+reverseWords(x)+"_"));

/* - Optimal solution
var reverseWords = function(s) {
   s=s.trim().replace(/(?=\s)(\s)(?=\s)/g,'') 
   return s.split(' ').reverse().join(' ')
};
*/
