import requests as _requests
from bs4 import BeautifulSoup as _BeautifulSoup
import json as _json

class Article:
    def __init__(self, title, content, images):
        self.title = title
        self.content = content
        self.images = images

class PollIds:
    def __init__(self, id_1, id_2):
        self.id_1 = id_1
        self.id_2 = id_2

class PollResults:
    def __init__(self, total_votes, answers):
        self.total_votes = total_votes
        self.answers = answers

class Comment:
    def __init__(self, id, content, name, pinned, published_at):
        self.id = id
        self.content = content
        self.name = name
        self.pinned = pinned
        self.published_at = published_at

class Reaction:
    def __init__(self, id, content, name, pinned, published_at):
        self.id = id
        self.content = content
        self.name = name
        self.pinned = pinned
        self.published_at = published_at

class Item:
    def __init__(self, title, id):
        self.title = title
        self.id = id

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

    return Article(title, content, image_urls)

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
    id_1 = id_2 = id_1_name = id_2_name = None
    
    for item in content:
        if item.get('type') == 'poll':
            poll_content = item.get('content', {})
            answers = poll_content.get('answers', [])
            if len(answers) >= 2:
                id_1 = answers[0].get('hash')
                id_2 = answers[1].get('hash')
                id_1_name = answers[0].get('text')
                id_2_name = answers[1].get('text')
                break
    
    if not id_1 or not id_2:
        raise Exception(f"No poll IDs found for {item_id}, maybe it doesn't contain any polls?")
    
    return PollIds({"id": id_1, "text": id_1_name}, {"id": id_2, "text": id_2_name})

def vote_in_poll(vote_hash):
    try:
        url = f'https://jeugdjournaal.nl/api/poll/vote/{vote_hash}'
        _requests.post(url)
    except _requests.exceptions.RequestException as e:
        raise Exception(f"Error voting in poll {vote_hash}: {e}")

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
            total_votes = item["content"]["noOfVotes"]
            answers = [{"text": answer["text"], "votes": answer["votes"]} for answer in item["content"]["answers"]]
            poll_results = PollResults(total_votes, answers)
            break
    
    return poll_results

def get_comments(item_id, limit):
    try:
        response = _requests.get(f"https://jeugdjournaal.nl/api/item/{item_id}/comments?limit={limit}")
        response.raise_for_status()
    except _requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching comments for item {item_id}: {e}")
    
    json_response = response.json()
    comments = [Comment(item['id'], item['text'], item['name'], item['pinned'], item['publishedAt']) for item in json_response['items']]

    return comments

def get_comment_reactions(item_id, comment_id, limit):
    try:
        response = _requests.get(f"https://jeugdjournaal.nl/api/item/{item_id}/comments/{comment_id}?limit={limit}")
        response.raise_for_status()
    except _requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching comment reactions for item {item_id}, comment {comment_id}: {e}")
    
    json_response = response.json()
    reactions = [Reaction(item['id'], item['text'], item['name'], item['pinned'], item['publishedAt']) for item in json_response['items']]

    return reactions

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

def get_items():
    try:
        r = _requests.get("https://jeugdjournaal.nl/")
        r.raise_for_status()
    except _requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching items: {e}")
    
    soup = _BeautifulSoup(r.content, 'html.parser')

    elements = soup.find_all(class_='sc-a2203b4a-5 ixVSEc')
    items = [Item(element.get_text(strip=True), element.find_parent('a')['href'].split('/')[-1].split('-')[0]) for element in elements]

    return items
