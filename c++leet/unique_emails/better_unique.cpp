#include <iostream>
#include <iomanip>
#include <memory>
#include <vector>
#include <unordered_map>
#include <string.h>
#include <stdio.h>
using namespace std;


class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        hash = {};
        for (auto email : emails) {
            auto pos = email.find('@');
            string domainName = email.substr(pos);
            string localName = "";
            for (int i = 0; i < pos; i++) {
                if (email[i] == '.') {
                    continue;
                } else if (email[i] == '+') {
                    break;
                }
                localName.push_back(email[i]);
            }
            hash[localName + domainName] = true;
        }
        return hash.size();
    }

private:
    unordered_map<string, bool> hash;
};

int main()
{
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
  printf("There are %d unique emails\n", sol1.numUniqueEmails(email_vector));
  return 0;
}
