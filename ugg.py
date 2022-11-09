import requests
from bs4 import BeautifulSoup


class Ugg:
    def __init__(self):
        self.url = 'https://probuildstats.com/champion/' # the base link

    # Parse the user entered string for adding onto the base link
    def key_words(self, user_message):
        words = user_message.split(' ', 1)[1]
        keywords = ''.join(words)
        return keywords

    # search the page for the correct links
    def search(self, search_words):
        # create requests and get the response
        response = requests.get(self.url + search_words)
        content = response.content
        # Parse the HTML
        soup = BeautifulSoup(content, 'html.parser')
        result_links = soup.findAll('a')
        return result_links

    # function that returns the href links
    def send_link(self, result_links, search_words):
        send_link = set()
        for link in result_links:
            text = link.text.lower()
            if search_words in text:
                send_link.add(link.get('href'))
        return send_link
