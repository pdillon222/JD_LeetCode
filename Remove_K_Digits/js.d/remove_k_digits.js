var removeKdigits = function(num, k) {
    let result = [];
    for (i in num){
        while (k > 0 & result.length > 0 & result[result.length -1] > num[i]){
            console.log(`popping ${num[i]}`)
            result.pop();
            k -= 1;
        }
        result.push(num[i]);
    }
    while (result[0] == '0'){result.shift()};
    result = result.join("").slice(0, result.length - k);
    return (result ? result : '0');
};

let res = removeKdigits('1432219', 8); // 1219
console.log(res)

/* Optimized version:
--------------------
var removeKdigits = function(num, k) {
    const buffer = [];
    for (const n of num) {
        while (buffer.length && buffer[buffer.length - 1] > +n && k) {
            k--;
            buffer.pop();
        }
        buffer.push(n);
    }
    while (k--)
        buffer.pop();
    while (buffer[0] === "0")
        buffer.shift();
    return buffer.join("") || "0";
};
*/
