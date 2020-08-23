#!/usr/bin/node

/*
On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.

You can move according to the next rules:

In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
You have to visit the points in the same order as they appear in the array.
*/

// https://stackabuse.com/command-line-arguments-in-node-js/

/*
doesnt_work = [[559,511],[932,618],[-623,-443],[431,91],[838,-127],[773,-917]]
# should return 4179 ; is returning 3454
*/



var tester = function(array){
  var diff_count = 0;
  for (var i=0; i < array.length-1; i++){
    let numer_diff = Math.abs(array[i][0] - array[i+1][0]);
    console.log("Testing numerator diff between " + array[i][0] + " & " + array[i+1][0]);
    console.log("Testing denominator diff between " + array[i][1] + " & " + array[i+1][1]);
    /* if distance between denom values > numer_diff:
    **   - add abs(denom_diff - numer_diff) to numer_diff*/
    let denom_diff = Math.abs(array[i][1] - array[i+1][1]);
    //let factor_diff = Math.abs(numer_diff - denom_diff);
    let factor_diff = numer_diff - denom_diff;
    console.log("[Diffs] = " + numer_diff + " " + denom_diff + " factor_diff = " + factor_diff +"\n");
    if (denom_diff > numer_diff){
      console.log("factor diff > numer_diff: adding " + factor_diff + " to " + numer_diff);
      numer_diff += denom_diff - numer_diff;
    };
    diff_count += numer_diff;  
  };
  return diff_count;
};

//this doesn't work as you would expect
//var points = [[559,511],[932,618],[-623,-443],[431,91],[838,-127],[773,-917]];
var points = [[1,1],[3,4],[-1,0]]; //returning 6; should return 7
console.log(tester(points));
