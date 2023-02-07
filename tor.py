import requests

session = requests.session()
session.proxies = {}

session.proxies['http'] = 'socks5h://localhost:9050'
session.proxies['https'] = 'socks5h://localhost:9050'

while True :
    dest = str(input('target: '))
    try :
        while True :

            print ('____________________________YOU__________________________________')
            source = requests.get('http://httpbin.org/ip')
            fake = session.get('http://httpbin.org/ip')
            print( 'your ip: ', source.text, 'tor ip: ', fake.text)

            reply = session.get(dest)
            print ('____________________________REPLY____________________________________')
            if (reply == '') :
                print('no response, status code: ', reply)
            else:
                print(reply.text)

    except Exception as e:
        print ('____________________________ERROR____________________________________')
        print('destination host unreachable or unsupported')
        print('')
        print('')
   

