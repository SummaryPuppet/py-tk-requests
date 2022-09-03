import requests

# url = "https://summarypuppet.github.io/wanna-be-girlfriend/"

def fail():
    print("Your request is failed")

def get_json(url = ""):
    try:
        response = requests.get(url)
        print(response.status_code)
        print(response.json())
    except:
        fail()

def post_json(url = "", json = {}):
    try:
        response = requests.post(url, json)
        print(response.json())
    except:
        fail()


get_json("http://localhost:4000/content")
