import urllib.request
import re
import json
from chalice import Chalice

app = Chalice(app_name='ukradlimi')
app.debug = True

@app.route('/{search_term}', cors=True)
def index(search_term):
    cards = []
    with urllib.request.urlopen('https://www.olx.pl/sport-hobby/q-' + search_term + '/?search%5Bphotos%5D=1&search%5Bdescription%5D=1') as response:
        html = response.read().decode('utf-8')

        images = [[m.start(), m.end()] for m in re.finditer('(\w|\.|\/|\_|\-|\:)+.jpg', html)]
        urls = [html[n[0]:n[1]] for n in images]

        for url in urls:
            cards.append({'imgUrl': url})
    return cards


# print(index('rower'))

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
