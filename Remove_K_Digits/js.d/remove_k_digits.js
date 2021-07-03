var removeKdigits = function(num, k) {
    let result = [];
    for (i in num){
        while (k > 0 & result.length > 0 & result[-1] > num[i]){
            result.pop;
            k -= 1;
        }
        console.log(`pushing ${num[i]}`);
        result.push(num[i]);
    }
    return result;
};

let res = removeKdigits('1432219', 3); // 1219
console.log(res)
