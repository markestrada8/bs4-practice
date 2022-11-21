from bs4 import BeautifulSoup
with open('index.html', 'r') as html_doc:
    soup = BeautifulSoup(html_doc, 'html.parser')
    # print(soup)
    # print(soup.prettify())

    # print(soup.title)

    # print(soup.title.name)

    # print(soup.title.string)

    # print(soup.title.parent.name)

    # print(soup.p)

    # print(soup.p['class'])

    # print(soup.a)

    # print(soup.find_all('a'))

    # print(soup.find(id="link3"))

    # for link in soup.find_all('a'):
    #     print(link['href'])

    print(soup.get_text())
