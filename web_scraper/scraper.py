import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    elements = soup.findAll("a", title="Wikipedia:Citation needed")
    return len(elements)


def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    elements = soup.findAll('p')
    result = ""
    for i in elements:
        citation_exist = i.findAll('a', title="Wikipedia:Citation needed")
        if citation_exist:
            result += f'Citation needed for : {i.text}'
            result += '\n'
    return result


if __name__ == '__main__':
    print(get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_Mexico'))
    print(get_citations_needed_report('https://en.wikipedia.org/wiki/History_of_Mexico'))
