import requests

API_KEY = "26c60a008851db0e385d276273650b39031375570e06f7b62d608925d11022b6"
def scan_url(input):
    url = "https://www.virustotal.com/api/v3/urls"

    payload = {"url": input}
    headers = {
        "accept": "application/json",
        "x-apikey": API_KEY,
        "content-type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=payload, headers=headers).json()
    return response["data"]["id"]

def get_url_report(id):
    url = f"https://www.virustotal.com/api/v3/analyses/{id}"
    headers = {
        "accept": "application/json",
        "x-apikey": API_KEY,
    }

    response = requests.get(url, headers=headers)
    return response.json()