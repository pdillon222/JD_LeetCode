var printListMessage = function(list, msg_string){
  console.log(msg_string);
  for (i=0; i < list.length; i++){
    console.log(list[i]);
  }
};

var numUniqueEmails = function(emails) {
    unique_emails = [];
    emails = emails.map(email => {
      if (email.search('\\+') !== -1){
        email = email.substring(0, email.search('\\+')) +
                email.substring(email.search('@'), email[-1]);
      }
      return email.split('@')[0].split('.').join("") + "@" + email.split('@')[1];
    });

    unique_emails.push(emails[0]);
    for (i=0; i < emails.length; i++){
      found_flag = false;
      for (j=0; j < unique_emails.length; j++){
        if (emails[i] == unique_emails[j])
          found_flag = true;
      }
      if (found_flag == false)
        unique_emails.push(emails[i]);
    }

    return unique_emails.length;
};

var emails = [
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
];

numUniqueEmails(emails);
