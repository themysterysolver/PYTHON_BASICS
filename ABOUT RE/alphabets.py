import re
checker=re.compile('[a-zA-Z]')
b=checker.match('A')
c=checker.match('123B')
d=checker.search('123B')
e=checker.search('123Bcd123a')
checker1=re.compile('[A-Za-z]*')
p=checker1.match('123Bcd123a')
q=checker1.search('123Bcd123a')
print('123Bcd123a\nq.span():','q=checker1.search:',q,'\n',q.span(),'\nq.start():',q.start(),'\nq.end():',q.end())
checker2=re.compile('[a-zA-Z]+')
t=checker2.search('123Bcd123a')
print('123Bcd123a\nq.span():','q=checker2.search:',t,'\n',t.span(),'\nq.start():',t.start(),'\nq.end():',t.end())
u=checker2.findall('123Bcd123a')
print(u)
r=checker.findall('123Bcd123a---123abz-Az')
s=checker1.findall('123Bcd123a---123abz-Az')
print(b,'\n',c,'\n',d,'\n',e,'\n',p,'\n',q,'\n',r,'\n',s)
