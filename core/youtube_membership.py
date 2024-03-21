import sys, os, io
import re
import random
import requests
import pandas as pd
from PIL import Image
from ascii_magic import AsciiArt, Back, Front

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import settings

def read_csv(file_path):
    members_df = pd.read_csv(file_path)
    return members_df

def rename_csv_columns(members_df):
    new_column_names = [
        'name',
        'profile_url',
        'membership_level',
        'total_time_in_level',
        'total_time_as_member',
        'last_update',
        'last_update_timestamp'
    ]
    
    members_df.columns = new_column_names
    return members_df

def get_members_from_csv(file_path):
    members_df = read_csv(file_path)
    members_df = rename_csv_columns(members_df)
    members = members_df.to_dict('records')
    return members

def filter_members_by_level(members, level):
    return [member for member in members if member['membership_level'] == level]

def list_membership_levels(members):
    levels = set(member['membership_level'] for member in members)
    return list(levels)

def pick_random_member(members):
    return random.choice(members)
  
# Extrai o ID do canal a partir da URL
def extract_channel_id(youtube_channel_url):
    regex = r'(?:youtube\.com\/channel\/)([^\/]+)'
    match = re.search(regex, youtube_channel_url)
    return match.group(1) if match else None

def get_user_photo_url(youtube_channel_url):
    channel_id = extract_channel_id(youtube_channel_url)
    if not channel_id:
        return None

    photo_url = fetch_channel_photo_url(channel_id)
    return photo_url

# Usa a API do YouTube para obter a URL da foto do perfil
def fetch_channel_photo_url(channel_id):
    base_url = 'https://www.googleapis.com/youtube/v3/channels'
    params = {
        'part': 'snippet',
        'id': channel_id,
        'key': settings.YOUTUBE_API_KEY,
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if 'items' in data and data['items']:
        return data['items'][0]['snippet']['thumbnails']['default']['url']
    else:
        return None

def photo_url_to_ascii_art(photo_url):
    photo = Image.open(requests.get(photo_url, stream=True).raw)
    photo_ascii_art = AsciiArt.from_pillow_image(photo)
    return photo_ascii_art.to_ascii(columns=100, char="#")

def get_membership_badge_image(months):
    badge_data = [
        (1, "new.png"),
        (2, "1_month.png"),
        (6, "2_months.png"),
        (12, "6_months.png"),
        (24, "12_months.png"),
        (36, "24_months.png"),
        (48, "36_months.png"),
        (float('inf'), "48_months.png")
    ]

    for limit, badge_file_name in badge_data:
        if months < limit:
            badge_image_path = os.path.join('assets', 'badges', badge_file_name)
            return badge_image_path

def get_member(member):
    # Carrega dados extras do membro
    photo_url = get_user_photo_url(member['profile_url'])
    photo_ascii = photo_url_to_ascii_art(photo_url)
    badge_image = get_membership_badge_image(member['total_time_as_member'])

    return {
        'name': member['name'],
        'profile_url': member['profile_url'],
        'photo_url': photo_url,
        'photo_ascii': photo_ascii,
        'membership_level': member['membership_level'],
        'total_time_in_level': member['total_time_in_level'],
        'total_time_as_member': member['total_time_as_member'],
        'last_update': member['last_update'],
        'last_update_timestamp': member['last_update_timestamp'],
        'badge_image': badge_image,
    }