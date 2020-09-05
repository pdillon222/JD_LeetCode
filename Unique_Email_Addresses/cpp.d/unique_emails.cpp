#include <iostream>
#include <iomanip>
#include <memory>
#include <vector>
#include <string.h>
#include <stdio.h>
using namespace std;

class Solution{
  public:
    int numUniqueEmails(vector<string>& emails);
  private:
    int indexOfAmpersand(const string email);
    string transformString(string& email);
};


/*
  Return the index of the '@' char within the email string
*/
int Solution::indexOfAmpersand(const string email)
{
  int index = 0;
  do {
    if (email[index] == '@')
    {
      return index;
    }
    index++;
  } while (index < email.size());
  return index;
}


/*
  If '.' character exists before index of '@': erase char
  If '+' found, erase char and everything up to '@'
  return string
*/
string Solution::transformString(string& email)
{
  int *and_index = nullptr;
  and_index = new int;
  *and_index = indexOfAmpersand(email);
  //printf("Original value of and_index = %d\n", *and_index);
  for (int i=0; i< *and_index; i++)
  {
    *and_index = indexOfAmpersand(email);
    if (email[i] == '.')
      email.erase(i,1);
  }

  *and_index = indexOfAmpersand(email);
  //printf("New value of and_index = %d\n", *and_index);
  int counter = 0;
  bool plus_flag = false;
  do {
    if (email[counter] == '+')
      plus_flag = true;
    counter++;
  } while (counter < *and_index and plus_flag == false);

  if (plus_flag)
    email.erase(counter - 1, *and_index - counter + 1);

  delete and_index;
  return email;
}


/*
  Return the number of unique email strings found
  within the vector
*/
int Solution::numUniqueEmails(vector<string>& emails)
{
  vector<string> unique_emails;
  bool found_flag = false;
  bool vec_match;

  for (int i=0; i < emails.size(); i++)
  {
    cout << "Before transformation: " << emails[i] << endl;
    emails[i] = transformString(emails[i]);
    cout << "After tranfsformation: " << emails[i] << "\n\n";
  }

  cout << "Determining unique email addresses in emails vector\n\n";
  //add first entry of `emails` to `unique_emails`
  unique_emails.push_back(emails[0]);
  for (int i=0; i < emails.size(); i++)
  {
    found_flag = false;
    cout << "Starting with " << emails[i] << endl;
    for (int j=0; j < unique_emails.size(); j++)
    {
      cout << "Comparing against " << unique_emails[j] << endl;
      if (emails[i] == unique_emails[j])
      {
        cout << emails[i] << " matches " << unique_emails[j] << endl;
        found_flag = true;
      }
    }
    cout << found_flag << "\n\n";
    if (!found_flag)
    {
      cout << "Match not found, adding " << emails[i] << " to unique emails\n\n";
      unique_emails.push_back(emails[i]);
      found_flag = false;
    }
  }

  cout << "\nDisplaying altered emails\n";
  for (int i=0; i < emails.size(); i++)
    cout << emails[i] << endl;
  cout << "\nDisplaying emails set\n";
  for (int i=0; i < unique_emails.size(); i++)
    cout << unique_emails[i] << endl;

  cout << "\n\nNumber of unique emails: " << unique_emails.size() << "\n";

  return unique_emails.size();
}


int main(){
  Solution sol1;
  string arr[] = {
      "j+d.j.b.k.xr.mmp@rn.qyy.com",
      "j+yt+w.on.k.r+i.l@rn.qyy.com",
      "j+i.t.b.o.x.l.s.a.z@rn.qyy.com",
      "j+wteuapmm.y@rn.qyy.com",
      "q.z.y.znvz.d+l+p@kyf.com",
      "np.e.x+u.a+mbv+j@uadsua.rqda.com",
      "np.e.x+e.f.n.f.r.c@uadsua.rqda.com",
      "pdiykt.rh+cc@ta.bxx.com",
      "j+aqlxgyy+b.k@rn.qyy.com",
      "j+a.hm.y.t.j.d+qq@rn.qyy.com",
      "k.i.j.hy.pe.n+ea@xfeslns.com",
      "j+h.v.w.b+x+h.e.n.r@rn.qyy.com",
      "j+m+j.k.o.jl.vv+r@rn.qyy.com",
      "k.i.j.hy.pe.n+l+i@xfeslns.com",
      "k.i.j.hy.pe.n+nh@xfeslns.com",
      "j+akd.xb.xx+c.e@rn.qyy.com",
      "j+a.j.u+e.s.p+w.x.x@rn.qyy.com"
  };
  vector<string> email_vector(arr, arr + sizeof(arr)/sizeof(string));
  sol1.numUniqueEmails(email_vector);
}
