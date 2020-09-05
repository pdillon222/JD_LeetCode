
/*
A general test-bed, for C++ fun times
for c++11 compilation: g++ -std=c++11 your_file.cpp -o your_program
*/

/*
  If you add periods ('.') between some characters in the local name 
  part of an email address, mail sent there will be forwarded to the 
  same address without dots in the local name.  For example, 
  "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the 
  same email address.  (Note that this rule does not apply for 
  domain names.)
  If you add a plus ('+') in the local name, everything after the 
  first plus sign will be ignored. This allows certain emails to be 
  filtered, for example m.y+name@email.com will be forwarded to 
  my@email.com.  (Again, this rule does not apply for domain names.)

  It is possible to use both of these rules at the same time.

  Given a list of emails, we send one email to each address in the list.  
  How many different addresses actually receive mails?
*/

#include <iostream>
#include <iomanip>
#include <memory>
#include <vector>
#include <string.h>
#include <stdio.h>
using namespace std;

class Solution{
  public:
    int numUniqueEmails(vector<string>& emails)
    {
      int *and_index = nullptr;
      and_index = new int;
      



    }
};



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

