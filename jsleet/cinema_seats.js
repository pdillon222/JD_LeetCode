#!/usr/bin/node

var maxNumberOfFamilies = function(n, reservedSeats) {
  let seatMap = {}; 
  let seatNums = Array(9).fill().map((_, i) => i + 1).slice(1, 9);
  /*
  let rsrv_in_range = (seats, seat_start, seat_end, reservations) => {
    return seats.slice(seat_start, seat_end).map(seat => {
      return reservations.includes(seat)}).every((element) => element === false)};
  */
  let rsrv_in_range = (seatRange, reservations) => {
    let counter = 0;
    let rsrvNotInRange = true;
    while (counter < reservations.length){
      if (seatRange.includes(reservations[counter])){
        //console.log(`Reservation -> ${reservations[counter]} found in ${seatRange.join(" ")}`);
        rsrvNotInRange = false;
        return rsrvNotInRange; 
      }
      counter++;
    }
    return rsrvNotInRange;
  };
  reservedSeats.map(function(subArray) {
    if (subArray[0] in seatMap === false){
      seatMap[subArray[0]] = [subArray[1]];
    } else {
      seatMap[subArray[0]].push(subArray[1]);
    }   
  }); 

  let max_arrangements = (n - Object.keys(seatMap).length) * 2;  
 
  // check seat reservations [2:6], [4:8], [8:10] 
  Object.keys(seatMap).map((row, index) => {
    /*
    if (rsrv_in_range(seatNums, 0, 4, seatMap[row]) && 
        rsrv_in_range(seatNums, 4, 8, seatMap[row])){
      max_arrangements += 2;
    } else if ( rsrv_in_range(seatNums, 0, 4, seatMap[row]) || 
                rsrv_in_range(seatNums, 2, 6, seatMap[row]) ||
                rsrv_in_range(seatNums, 4, 8, seatMap[row])){
      max_arrangements += 1;
    }
    */
    if (rsrv_in_range(seatNums.slice(0, 4), seatMap[row]) && 
        rsrv_in_range(seatNums.slice(4, 8), seatMap[row])){
      //console.log(`${row_num} containing reservations => ${seatMap[row].join(" ")}`);
      //console.log(`Meets conditions for no reservations in '${seatNums.slice(0,4).join(" ")}' and '${seatNums.slice(4,8).join(" ")}'`);
      max_arrangements += 2;
    } else if ( rsrv_in_range(seatNums.slice(0, 4), seatMap[row]) || 
                rsrv_in_range(seatNums.slice(2, 6), seatMap[row]) ||
                rsrv_in_range(seatNums.slice(4, 8), seatMap[row])){
      max_arrangements += 1;
    }
  });
  console.log(max_arrangements); 
  return max_arrangements; 
};

var n = 3;
var reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]];
// values above return -> 4 ###

n = 4
reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
// values above return -> 4 ###


n = 2;
reservedSeats = [[2,1],[1,8],[2,6]];
// values above return -> 2 ###


maxNumberOfFamilies(n, reservedSeats);
