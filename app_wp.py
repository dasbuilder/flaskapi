import requests
import json
import base64
import os
from datetime import datetime

# URLs
url = 'http://correando.wpengine.com'
wapi_url = f'{url}/wp-json/wp/v2'
local_media_path = os.path.join('/Users/spencer.anderson/Documents/', 'testimages')

local_url = 'http://correando.local'
local_wapi_url = f'{local_url}/wp-json/wp/v2'


creds = f'{username}:{passwd}'
token = base64.b64encode(creds.encode())

header = {
    'Authorization':'Basic ' + token.decode('utf-8'), 
    'Content-Disposition': 'attachment; filename=desk-design.png',
    }

media = {
    'file': open(f'{local_media_path}/desk_design_01.png', 'rb'),
    'caption': 'One of two. Second API image',
    'date': f'{datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S")}',
    'description': 'Image of desk API', 
    'title': 'Desks',
    'status': 'publish'
}

media_url = f'{wapi_url}/media'
local_media_url = f'{local_wapi_url}/media'
post_url = f'{wapi_url}/posts'
local_post_url = f'{local_wapi_url}/posts'


image = requests.post(media_url, headers=header, files=media)
image = requests.post(local_media_url, headers=header, files=media)

post = requests.post(post_url, headers=header, data=media)
image_url = str(json.loads(image.content)['source_url'])

# Making a post now
post = {
    'date': f"{datetime.strftime(datetime.now(), '%Y-%m-%dT%H:%M:%S')}",
    'title': 'Second WP/Python API post with image',
    'content': f'First <img src="{image_url}"',
    'status': 'publish'
}


wp_posts_poster = requests.post(post_url, headers=header, data=post)
print(wp_posts_poster.status_code)

'''
curl -L -X POST 'https://correando.local/wp-json/wp/v2/media' \
--header "authorization: Basic pass=" \
--header 'Content-Disposition: form-data; filename="tokyo_night.jpg"' \
--header 'Content-Type: image/jpeg' \
--data-binary "@/Users/spencer.anderson/Documents/testimages/tokyo_night.jpg"
'''

'''
curl -L -X POST 'https://correando.wpengine.com/wp-json/wp/v2/media/' \
--header "authorization: Basic $(echo -n user:pass| base64)" \
--header 'Content-Disposition: form-data; filename="tokyo_night.jpg"' \
--header 'Content-Type: image/jpeg' \
--data-binary "@tokyo_night.jpg"
'''