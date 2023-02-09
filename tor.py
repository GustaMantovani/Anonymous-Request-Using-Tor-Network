import requests

session = requests.session()
session.proxies = {}
session.proxies['http'] = 'socks5h://localhost:9050'
session.proxies['https'] = 'socks5h://localhost:9050'

print ('____________________________YOU__________________________________')
source = requests.get('http://httpbin.org/ip')
fake = session.get('http://httpbin.org/ip')
print( 'your ip: ', source.text, 'tor ip: ', fake.text)
print ('_________________________________________________________________')
print('')

current_status = 404
reply = ''

while True:

    if current_status == 404:
        dest = str(input('target: '))

    previous_reply = reply
    reply = session.get(dest)

    previous_status = current_status
    current_status=reply.status_code

    if current_status != previous_status:
        print('STATUS CODE CHANGED: ', current_status)
        print('')

        if reply != previous_reply:
            print('REPLY: ')
            print(reply.text)
       

