import re
m = re.match('foo','food on the table')
if m is not None:
    print('...')
    print(m.group())
#print(m)

n = re.search('foo','seafood')
if n is not None:
    print('...')
    print(m.group())

bt = 'bat|bet|bit'
m = re.match(bt,'bat')
if m is not None:
    print(m.group())
m = re.search(bt,'He bit me!')
if m is not None:
    print(m.group())

patt314 = '3.14'
pi_patt =  '3\.14'
m = re.match(pi_patt,'3.14')
if m is not None:
    print(m.group())
m = re.match(patt314,'3014')
if m is not None:
    print(m.group())
m = re.match(patt314,'3.14')
if m is not None:
    print(m.group())

m = re.match('[cr][23][dp][o2]','c3po')
if m is not None:
    print(m.group())
m = re.match('[cr][23][dp][o2]','c2do')
if m is not None:
    print(m.group())
m = re.match('r2d2|c2po','c2do')
if m is not None:
    print(m.group())
m = re.match('r2d2|c2po','r2d2')
if m is not None:
    print(m.group())

patt = '\w+@(\w+\.)?\w+\.com'
print(re.match(patt,'nobody@xxx.com').group())
print(re.match(patt,'nobody@www.xxx.com').group())
