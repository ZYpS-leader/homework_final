
import requests
import json


def main():
        
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=RP3sf4UYV3nNtwO3gFDkoEte&client_secret=wcybYcpRxpYyHsutWxMnPQlKvT9dLqBZ"
    
    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    t=response.text
    print(t)
    

if __name__ == '__main__':
    main()