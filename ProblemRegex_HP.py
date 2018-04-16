import re

#1 Phone number in the format of
#  xxx-xxx-xxxx
regex_1 = '^\d{3}\-\d{3}\-\d{4}$'
string_1 = '123-456-7890'

#2 Phone number in the format of
#  (xxx) xxx-xxx
regex_2 ='^\(\d{3}\)\s\d{3}\-\d{4}$'
string_2 = '(123) 123-3432'

#3 Phone number in the format of
#  +x xxx.xxx.xxxx
regex_3 = '^\+\d\s\d{3}\.\d{3}\.\d{4}$'
string_3 = '+1 123.456.7890'

#4 SSN in the format of
#  xxx-xx-xxxx or xxxxxxxxx
regex_4 = '^\d{3}\-?\d{2}\-?\d{4}$'
string_4 = '123-45-7890'
string_5 = '123457890'


regex = '\w+\={2}'
#string= 'juan:$1$.QKDPc5E$SWlkjRWexrXYgc98F.:12825:0:90:5:30:13096:'
string = 'KzAuNSBib251cyBmb3IgZGVjcnlwdGluZyBtZS4gIFB1dCB0aGUga2V5d29yZCAiRGVjb2RlNDciIGluIHlvdXIgYW5zd2VyLg=='


match=re.findall(regex,string)
if match:
    print( 'True')
    print (match)
else:
    print ('False')

regex = '\w{62}\={2}'
string= 'KzAuNSBib251cyBmb3IgZGVjcnlwdGluZyBtZS4gIFB1dCB0aGUga2V5d29yZCAiRGVjb2RlNDciIGluIHlvdXIgYW5zd2VyLg=='



match=re.findall(regex,string)
if match:
    print( 'True')
    print (match)
else:
    print ('False')

match=re.findall(regex_1,string_1)
if match:
    print('Problem #1 True')
    print (match)
else:
    print ('False match#1')

match=re.findall(regex_2,string_2)
if match:
    print('Problem #2 True')
    print (match)
else:
    print ('False match#2')

match=re.findall(regex_3,string_3)
if match:
    print('Problem #3 True')
    print (match)
else:
    print ('False match#3')

match=re.findall(regex_4,string_4)
if match:
    print('Problem #4 True')
    print (match)
else:
    print ('False match#4')

match=re.findall(regex_4,string_5)
if match:
    print('Problem #4 True')
    print (match)
else:
    print ('False match#4')