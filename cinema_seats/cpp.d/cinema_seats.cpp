#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

//typedef unordered_map<int, vector<int>> reservation_map;

class Solution {
public:
    unordered_map<int, vector<int>> reservation_map;
    int seat_combinations, temp_combo, counter;
    unordered_map<int, vector<int>>::const_iterator found;
    vector<int>::iterator it1, it2;

    bool found_in_vector(int start, int end, const vector<int> seats) {
      int counter = start;
      bool int_in_vector = false;
      cout << "Scanning for ints " << start << ":" << end << " in => ";
      for (auto x: seats) cout << x << " ";
      cout << endl;
      while (counter < end and ! int_in_vector){
        cout << "Seeking " << counter << " in ";
        for (auto x: seats) cout << x << " ";
        cout << endl; 
        int_in_vector = find(seats.begin(), seats.end(), counter) != seats.end();
        if (int_in_vector) cout << "!! Found reservation at seat " << counter << endl;
        counter++;
      } 
      cout << endl;
      return int_in_vector;
    }
     
    int maxNumberOfFamilies(int n, vector<vector<int>>& reservedSeats) {

      // construct a map of rows - whith a vector of all reserved seats in row
      for (auto i: reservedSeats){
        this->found = this->reservation_map.find(i[0]);
        if (this->found == this->reservation_map.end()){
          // key not yet found - add and initialize vector with i[1]
          cout << "Adding key -> " << i[0] << " and value {" << i[1] << "}" << endl;
          this->reservation_map.insert({i[0], {i[1]}});
        } else {
          // key found - append vector with i[i]
          cout << "Appending value -> " << i[1] << " to key " << i[0] << endl;
          this->reservation_map.at(i[0]).push_back(i[1]);
        }
      }
      cout << endl;
      // begin aggregating seat combinations:
      this->seat_combinations = (n - this->reservation_map.size()) * 2;
      cout << "starting value of seat_combinations " << this->seat_combinations << endl;

      // iterate through reservation_map:
      // - seat combos: [2:6], [4:8], [6:10]
      for (auto row: this->reservation_map){
        cout << row.first << ": ";
        for (auto seat: row.second) cout << seat << " ";
        cout << endl;
        // TODO - make this work
        // ---------------------
        if (! this->found_in_vector(2, 6, row.second)){
          this->seat_combinations += 1;
          if (! this->found_in_vector(6, 10, row.second)) this->seat_combinations += 1;
        } else {
          if (! this->found_in_vector(4, 8, row.second)){
            this->seat_combinations += 1;
          } else {
            if (! this->found_in_vector(6, 10, row.second)) this->seat_combinations += 1;
          }
        }
        // ---------------------
        cout << endl;
      }
      cout << this->seat_combinations << endl;
      return this->seat_combinations;       
    }
};


int main(){
  int n = 3;
  vector<vector<int>> reservedSeats = {{1,2},{1,3},{1,8},{2,6},{3,1},{3,10}}; // -> 4

  n = 4;
  reservedSeats = {{4,3},{1,4},{4,6},{1,7}}; // -> 4

  Solution solution;
  solution.maxNumberOfFamilies(n, reservedSeats);  
  return 0;
}


/*
n = 3
reservedSeats = {{1,2},{1,3},{1,8},{2,6},{3,1},{3,10}}
### values above return -> 4 ###

n = 4
reservedSeats = {{4,3},{1,4},{4,6},{1,7}}
### values above return -> 4 ###

n = 2646
reservedSeats = Solution.reservationsFromFile()
### answer is right -> 2084
### need to optimize for time -> currenty at 7228 ms

n = 3
reservedSeats = {{1,2},{1,3},{1,8},{2,6},{3,1},{3,10}}
### values above return -> 4 ####
*/

/*
#include<unordered_map>
class Solution {
public:
    int maxNumberOfFamilies(int n, vector<vector<int>>& r) {
        unordered_map<int, int> taken;
        int res=0;
        for(auto& v : r){
            if(v[1]>1 and v[1]<6) taken[v[0]] |= 1;   //take left block
            if(v[1]>3 and v[1]<8) taken[v[0]] |= 2;   //take middle block
            if(v[1]>5 and v[1]<10) taken[v[0]] |= 4;  //take right block
        }
        res += 2*(n-taken.size());  //count all non-taken rows
        for(auto& it : taken)
            if(it.second != 7) res++;   //if at least one block is available - take it
        
        return res;
    }
};
*/

