from typing import List

class Solution:
  def numUniqueEmails(self, emails: List[str]):
    emails = [email.split('@') for email in emails]
    #remove '.' from email[0] in emails if '.' in email[0]
    #strip characters after '+' if '+' in email[0]
    emails = [[email[0][:email[0].index('+')],email[1]]
              if '+' in email[0] else email for email in emails]
    emails = [[email[0].split('.'),email[1]]
              if '.' in email[0] else email[:]
              for email in emails]
    return len(set(['@'.join([''.join(email[0]),email[1]]) for email in emails]))

if __name__=="__main__":
  sol = Solution()
  emails = ["test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com"]
  print(sol.numUniqueEmails(emails)) # => 2
