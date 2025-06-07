Import requests

ACCESS_TOKEN = 'ENTER TOKEN ...' 

def get_my_profile():
    url = 'https://graph.facebook.com/v18.0/me'
    params = {
        'access_token': ACCESS_TOKEN,
        'fields': 'id,name,email'
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        print("✅ Profile Info:")
        print(response.json())
    else:
        print("❌ Error:")
        print(response.status_code, response.text)

get_my_profile()
