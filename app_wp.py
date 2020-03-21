#!/usr/local/bin/env python3 

import requests
import json
import base64
import os
from datetime import datetime
from configparser import ConfigParser
import argparse


def get_conf(file):
    config = ConfigParser()
    config.read(file)
    username = config.get('wp', 'username')
    passwd = config.get('wp', 'passwd')
    return username, passwd


def format_creds(creds):
    username, passwd = creds
    return f'{username}:{passwd}'

# URLs
url = 'http://correando.wpengine.com'
wapi_url = f'{url}/wp-json/wp/v2'
local_media_path = os.path.join('/Users/spencer.anderson/Documents/', 'testimages')

local_url = 'http://correando.local'
local_wapi_url = f'{local_url}/wp-json/wp/v2'


def get_creds(file):
    return get_conf(file)


def fmt_creds(creds)
    return format_creds(creds)


def token(creds_fmt):
    return base64.b64encode(creds_fmt.encode())


def get_header(token):
    # Right now only working with the basic auth and media uploading. 
    # Will change options later. 
    return header = {
        'Authorization':'Basic ' + token.decode('utf-8'), 
        'Content-Disposition': 'attachment; filename=desk-design.png',
        }


def wapi_base(remote=None, domain):
    if 'Yes' or 'y' in remote:
        return f'{domain}.wpengine.com'
    else:
        return f'{domain}.local'


def is_media(remote=None, wapi_base):

    if 'Yes' or 'y' in remote:
        return f'{wapi_base}/media'
    else:
        return f'{wapi_base}/media'


def media_info(media_api_path):

    return media = {

        'file': open(f'{media_api_path}/desk_design_01.png', 'rb'),
        'caption': 'One of two. Second API image',
        'date': f'{datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S")}',
        'description': 'Image of desk API', 
        'title': 'Desks',
        'status': 'publish'
    }


def is_post(remote=None):
     if 'Yes' or 'y' in remote:
         return f'{wapi_url}/posts'
    else:
        return f'{local_wapi_url}/posts'


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


def arg_parse():

    parser = argparse.ArgumentParser(description='Automatically post to WP using API', prog='awapi')
    parser.add_argument('site', type=str, help="Install we're posting to")
    parser.add_argument('-r', dest='remote', help="Tell program to use remote location (wpengine server) or local")
    
    args = parser.parse_args()
    return args


def main():
    args = arg_parse()
    


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