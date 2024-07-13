import requests as _requests
from bs4 import BeautifulSoup as _BeautifulSoup
import json as _json

def get_poll_ids(item_id):
    try:
        response = _requests.get(f"https://jeugdjournaal.nl/artikel/{item_id}")
        response.raise_for_status()
    except _requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching article {item_id}: {e}")
    
    soup = _BeautifulSoup(response.text, 'html.parser')
    next_data_script = soup.find('script', id='__NEXT_DATA__')
    if not next_data_script:
        raise Exception("Next data script not found")
    
    json_str = next_data_script.string
    try:
        data = _json.loads(json_str)
    except ValueError as e:
        raise Exception(f"Error parsing JSON data: {e}")
    
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
    
    if not hash_1 or not hash_2:
        raise Exception(f"No poll IDs found for {item_id}, maybe it doesn't contain any polls?")
        
    return {
        "id_1": {
            "id": hash_1,
            "text": hash_1_name
        },
        "id_2": {
            "id": hash_2,
            "text": hash_2_name
        }
    }


def vote_in_poll(vote_hash):
    try:
        url = f'https://jeugdjournaal.nl/api/poll/vote/{vote_hash}'
        response = _requests.post(url)
        response.raise_for_status()
    except _requests.exceptions.RequestException as e:
        raise Exception(f"Error voting in poll {vote_hash}: {e}")
    
    return response.json()

def get_poll_data(item_id):
    try:
        response = _requests.get(f"https://jeugdjournaal.nl/artikel/{item_id}")
        response.raise_for_status()
    except _requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching article {item_id}: {e}")
    
    soup = _BeautifulSoup(response.text, 'html.parser')
    next_data_script = soup.find('script', id='__NEXT_DATA__')
    if not next_data_script:
        raise Exception("Next data script not found")
    
    json_str = next_data_script.string
    try:
        data = _json.loads(json_str)
    except _json.JSONDecodeError as e:
        raise Exception(f"Error decoding JSON data: {e}")
    
    poll_results = {}
    
    for item in data["props"]["pageProps"]["data"]["content"]:
        if item["type"] == "poll":
            poll_results["totalVotes"] = item["content"]["noOfVotes"]
            poll_results["answers"] = [{"text": answer["text"], "votes": answer["votes"]} for answer in item["content"]["answers"]]
            break
    
    return poll_results

def get_comments(item_id, limit):
    try:
        response = _requests.get(f"https://jeugdjournaal.nl/api/item/{item_id}/comments?limit={limit}")
        response.raise_for_status()
    except _requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching comments for item {item_id}: {e}")
    
    json_response = response.json()
    formatted_comments = []

    for item in json_response['items']:
        formatted_comment = {
            "id": item['id'],
            "content": item['text'],
            "name": item['name'],
            "pinned": item['pinned'],
            "publishedAt": item['publishedAt']
        }
        formatted_comments.append(formatted_comment)

    return {
        "comments": formatted_comments
    }


def get_comment_reactions(item_id, comment_id, limit):
    try:
        response = _requests.get(f"https://jeugdjournaal.nl/api/item/{item_id}/comments/{comment_id}?limit={limit}")
        response.raise_for_status()
    except _requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching comment reactions for item {item_id}, comment {comment_id}: {e}")
    
    json_response = response.json()
    formatted_reactions = []

    for item in json_response['items']:
        formatted_reaction = {
            "id": item['id'],
            "content": item['text'],
            "name": item['name'],
            "pinned": item['pinned'],
            "publishedAt": item['publishedAt']
        }
        formatted_reactions.append(formatted_reaction)

    return {
        "reactions": formatted_reactions
    }


def post_comment(item_id, name, content):
    payload = {
        "name": name,
        "text": content
    }
    try:
        r = _requests.post(f"https://jeugdjournaal.nl/api/item/{item_id}/comments", json=payload)
        r.raise_for_status()
    except _requests.exceptions.RequestException as e:
        raise Exception(f"Error posting comment for item {item_id}: {e}")

    return {
        "id": r.json()["id"],
        "publishedAt": r.json()["publishedAt"]
    }


def get_items():
    try:
        r = _requests.get("https://jeugdjournaal.nl/")
        r.raise_for_status()
    except _requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching items: {e}")
    
    soup = _BeautifulSoup(r.content, 'html.parser')

    elements = soup.find_all(class_='sc-a2203b4a-5 ixVSEc')
    items = []

    for element in elements:
        title = element.get_text(strip=True)
        href = element.find_parent('a')['href']
        id = href.split('/')[-1].split('-')[0]
        items.append({"title": title, "id": id})

    return {
        "items": items
    }


def read_item(item_id):
    try:
        r = _requests.get(f"https://jeugdjournaal.nl/artikel/{item_id}")
        r.raise_for_status()
    except _requests.exceptions.RequestException as e:
        raise Exception(f"Error reading article {item_id}: {e}")
    
    soup = _BeautifulSoup(r.content, 'html.parser')

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

print(get_poll_data(2528544))