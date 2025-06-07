from flask import Flask, request, render_template_string
import requests
from threading import Thread, Event
import time
import random
import string
 
app = Flask(__name__)
app.debug = True

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
