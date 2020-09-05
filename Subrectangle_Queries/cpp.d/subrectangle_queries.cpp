#include<iostream>
#include<stdio.h>
#include<vector>

using namespace std;

class SubrectangleQueries {
public:
    vector<vector<int>> rect;
    SubrectangleQueries(vector<vector<int>>& rectangle) {
      this->rect = rectangle;
    }

    void updateSubrectangle(int row1, int col1, int row2, int col2, int newValue) {
      cout << "make updates" << endl;
      for (int i=row1; i<=row2; i++){
        for (int j=col1; j<=col2; j++){
          this->rect[i][j] = newValue;
        }
      }
    }

    int getValue(int row, int col) {
      for (int i=0; i<this->rect.size(); i++){
        for (int j=0; j<this->rect[i].size(); j++){
          cout << this->rect[i][j] << " ";
        }
        cout << endl;
      }
      return this->rect[row][col];
    }
};

int main(){
  vector<vector<int>> test_rect = {{1,2,3},{4,5,6}};
  //SubrectangleQueries(test_rect) subrect;
  SubrectangleQueries subrect = SubrectangleQueries(test_rect);
  cout << "starting rectangle values:" << endl;
  subrect.getValue(1,2);
  cout << "updating rectangle values:" << endl;
  subrect.updateSubrectangle(0, 1, 1, 2, 5);
  subrect.getValue(1,2);

  cout << endl;
  ///*
  test_rect = {{1,2,1},{4,3,4},{3,2,1},{1,1,1}};
  //SubrectangleQueries(test_rect) subrect;
  subrect = SubrectangleQueries(test_rect);
  cout << "starting rectangle values:" << endl;
  subrect.getValue(1,2);
  subrect.updateSubrectangle(0, 0, 3, 2, 5);
  cout << "updating rectangle values:" << endl;
  subrect.getValue(1,2);
  //*/
  return 0;
}
