#include <iostream>
#include <stdio.h>
#include <unordered_map>
#include <string>
#include <vector>
using namespace std;


class Solution{
  public:
    int minTimeToVisitAllPoints(vector<vector<int>>& points);
};

int Solution::minTimeToVisitAllPoints(vector<vector<int>>& points)
{
  printf("testing string %*s\n", 10, "formatting");

  // post-c++11 vector standard
  long *dist_counter = new long;
  int *numer_diff, *denom_diff = new int;
  *numer_diff, *denom_diff = 0;
  *dist_counter = 0;
  cout << "Initial value of dist_counter " << *dist_counter << endl;

  cout << &dist_counter << " " << &numer_diff << " " << &denom_diff << endl;

  for (int i=0; i < points.size() - 1; i++){
    cout << "Difference between X coordinates " << points[i][0]
         << " & " << points[i+1][0] << " == "
         << points[i][0] - points[i+1][0] << endl;
    cout << "Difference between Y coordinates " << points[i][0]
         << " & " << points[i+1][1] << " == "
         << points[i][1] - points[i+1][1] << endl;

    // determine whether abs diff of denom or numers is greater
    *numer_diff = abs(points[i+1][0] - points[i][0]);
    *denom_diff = abs(points[i+1][1] - points[i][1]);

    cout << "numer_diff = " << *numer_diff << "; denom_diff = " << *denom_diff << "\n\n";
    if (*numer_diff >= *denom_diff){
      *dist_counter += *numer_diff;
    } else {
      *dist_counter += *denom_diff;
    }
    cout << "Minttime variable incremented to " << *dist_counter << "\n\n";
  }

  long result = *dist_counter;
  return *dist_counter;
  //return result;
}

int main()
{
  vector<vector<int>> matrix = {{559,511},
                                {932,618},
                                {-623,-443},
                                {431,91},
                                {838,-127},
                                {773,-917}};
  Solution *tester = new Solution();
  int mintime = tester->minTimeToVisitAllPoints(matrix);
  delete tester;
  cout << mintime << endl;
  return 0;
}
