import requests 
def get(to_url:str):
    request_url = "https://aip.baidubce.com/api/v1/solution/direct/imagerecognition/combination"
    try:
        params = "{\"imgUrl\":\""+to_url+"\",\"scenes\":[\"animal\",\"plant\",\"ingredient\",\"dishs\", \"red_wine\",\"currency\",\"landmark\"]}"
        access_token = '24.3bbf8fea92d39877b83e4212791799c2.2592000.1687965782.282335-34105298'
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/json'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            return response.json()
    except:pass         
