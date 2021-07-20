from urllib.request import urlopen
import json


def run(character):

    character = character.replace(" ", "+")

    url = f"https://challenges.hackajob.co/swapi/api/people/?search={character}"
    response = urlopen(url).read()

    data = json.loads(response.decode('utf-8'))
    films_in = data['results'][0]['films'] # list of films

    return len(films_in)
