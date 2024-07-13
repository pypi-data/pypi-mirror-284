## JeugdjournaalPY

### Overview
The `jeugdjournaalpy` library simplifies interaction with the Jeugdjournaal website and API. It can retrieve article details, participate in polls, read/post comments, and explore articles.

### Installation
Install `jeugdjournaalpy` via pip:

```
pip install jeugdjournaalpy
```

### Example Usage
```python
import jeugdjournaalpy as jj

# Example: Retrieve article details
article_id = '2528081'
article_details = jj.read_item(article_id)
print(article_details['title'])
print(article_details['content'])

# Example: Vote in a poll
poll_id = 'Zdf'
vote_response = jj.vote_in_poll(poll_id)
print(vote_response)

# Example: Retrieve comments
comments = jj.get_comments(article_id, limit=10)
print(comments)
```
# Documentation
A full documentation can be found [here](https://github.com/hcr5/SomPy/blob/main/docs.md)