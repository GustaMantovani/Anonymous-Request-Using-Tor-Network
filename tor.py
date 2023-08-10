import requests

def setSession():
    session = requests.session()
    session.proxies = {}
    session.proxies['http'] = 'socks5h://localhost:9050'
    session.proxies['https'] = 'socks5h://localhost:9050'

    return session

def panel(session):
    print ('____________________________YOU__________________________________')
    source = requests.get('http://httpbin.org/ip')
    fake = session.get('http://httpbin.org/ip')
    print( 'your ip: ', source.text, 'tor ip: ', fake.text)
    print ('_________________________________________________________________')
    print('')

def requestAndDisplayResponses (session):
    target = input("target: ")
    while True:
        try: 
            rep = session.get(target)
            print(rep.status_code)
            while str(rep.status_code)=='404':
                target = input("Not Found\ntarget: ")
                rep = session.get(target)
        except Exception as e:
            print("Error: ", e)
            break
        else:
            print("STATUS CODE: ", rep.status_code)
            print("REPLY: ", rep.text)

def main():
    session = setSession()
    panel(session)
    requestAndDisplayResponses(session)

main()

       
