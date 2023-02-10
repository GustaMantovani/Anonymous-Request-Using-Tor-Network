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

dest = str(input('target: '))
reply = ''
e = ''
current_status = ''
   
while True:

    if e != '':
        print("error:", e)
        dest = str(input('target: '))

    elif current_status == 404:
        print('NOT FOUND')
        dest = str(input('target: '))

    try:
        reply = session.get(dest)

    except :
        e = Exception

    previous_reply = reply
    previous_status = current_status
    current_status=reply.status_code

    if current_status != 404:
        if previous_reply == '' or previous_status == '':
            print('')
            print('STATUS CODE: ', reply.status_code)
            print('')
            print('REPLY: ', reply.text)

        else:
            if current_status != previous_status:
                print('STATUS CODE CHANGED: ', current_status)
                print('')
                print('NEW REPLY: ')
                print(reply.text)

            if reply.text != previous_reply.text:
                print('NEW REPLY: ')
                print(reply.text)
       
