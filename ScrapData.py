import requests
from bs4 import BeautifulSoup

URL = "https://www.udemy.com/topic/python/"
page = requests.get(URL)

def scrap_data():
    '''
    This function parse Frequently Asked Questions, Answers and URLs for the same.\n
    Parameters:
        None
    Returns:
        list[lists[strings]]
    '''
    soup = BeautifulSoup(page.content,"html.parser")
    # print(soup,'\n\n',type(soup))

    questions = [q.text for q in soup.find_all("span",class_="udlite-accordion-panel-title")]
    # print(questions)
    answers = [a.text for a in soup.find_all("div",class_="udlite-text-sm questions-and-answers--answer--2PMFk")]
    # print(answers)
    ans_link_divs = soup.find_all("div",class_="udlite-heading-md questions-and-answers--link--11XUK")
    # print(ans_link_divs,'\n\n', type(ans_link_divs))
    urls = [ans_link_div.find("a")["href"] for ans_link_div in ans_link_divs]
    # print(urls,'\n\n', type(urls))
    print('Data Fetched...')
    parsed_data = [questions,answers,urls]
    return parsed_data

if __name__ == "__main__":
    print("Please Execute StoreData.py file")
