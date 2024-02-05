from bs4 import BeautifulSoup

def non_rawing(title,raw_data,foldername):

    # The provided text
    html_text = raw_data

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_text, 'html.parser')

    a_text = ''

    if not title:
        chapter_title = soup.find("span",class_="chr-text")
        title = chapter_title.get_text()
        a_text += '\n' + title + '\n\n'

    cont_div = soup.find("div", class_="chapter container")

    p_tags = cont_div.find_all("p")

    listed_content = []

    for index,p_tag in enumerate(p_tags):
        text = ''.join(p_tag.find_all(text=True, recursive=False))
        text += '\n\n'
        listed_content.append(text)

    a_text += ''.join(listed_content)

    x = open(f'{foldername}/{title}.txt','w',encoding='utf-8')
    x.write(a_text)
    x.close()


    return title
