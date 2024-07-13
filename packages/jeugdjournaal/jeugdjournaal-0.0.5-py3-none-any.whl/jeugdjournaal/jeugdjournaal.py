import requests as __requests
from bs4 import BeautifulSoup as __BeautifulSoup
import json as __json


def get_poll_hashes(item_id):
    response = __requests.get(f"https://jeugdjournaal.nl/artikel/{item_id}")
    soup = __BeautifulSoup(response.text, 'html.parser')
    next_data_script = soup.find('script', id='__NEXT_DATA__')
    json_str = next_data_script.string
    data = __json.loads(json_str)
    
    content = data.get('props', {}).get('pageProps', {}).get('data', {}).get('content', [])
    hash_1 = None
    hash_2 = None
    hash_1_name = None
    hash_2_name = None
    
    for item in content:
        if item.get('type') == 'poll':
            poll_content = item.get('content', {})
            answers = poll_content.get('answers', [])
            
            if len(answers) >= 2:
                hash_1 = answers[0].get('hash')
                hash_2 = answers[1].get('hash')
                hash_1_name = answers[0].get('text')
                hash_2_name = answers[1].get('text')
                break
    
    return __json.dumps({
        "hash_1": hash_1,
        "hash_1_name": hash_1_name,
        "hash_2": hash_2,
        "hash_2_name": hash_2_name
    })


def vote_in_poll(vote_hash):
    url = f'https://jeugdjournaal.nl/api/poll/vote/{vote_hash}'
    response = __requests.post(url)
    return response.json()


def get_comments(item_id, limit):
    response = __requests.get(f"https://jeugdjournaal.nl/api/item/{item_id}/comments?limit={limit}")
    return response.json()


def post_comment(item_id, name, content):
    payload = {
        "name": name,
        "text": content,
    }
    r = __requests.post(f"https://jeugdjournaal.nl/api/item/{item_id}/comments", json=payload)
    return r.json()


def get_items():
    r = __requests.get("https://jeugdjournaal.nl/")
    soup = __BeautifulSoup(r.content, 'html.parser')

    elements = soup.find_all(class_='sc-a2203b4a-5 ixVSEc')
    items = []

    for element in elements:
        title = element.get_text(strip=True)
        href = element.find_parent('a')['href']
        id = href.split('/')[-1].split('-')[0]
        items.append({"title": title, "id": id})

    return items


def read_item(id):
    r = __requests.get(f"https://jeugdjournaal.nl/artikel/{id}")
    soup = __BeautifulSoup(r.content, 'html.parser')

    title_element = soup.find(class_='sc-799cb68a-0 sc-f0a7871b-6 frnEMw fmrOZD')
    title = title_element.get_text(strip=True) if title_element else 'No title found'

    content_elements = soup.find_all(class_='sc-5ad4567c-0 bAROSX')
    content = '\n\n'.join(element.get_text(strip=True) for element in content_elements)

    image_urls = [img.get('src') for img in soup.find_all('img', src=True)]

    return {
        "title": title,
        "content": content,
        "image_urls": image_urls
    }
