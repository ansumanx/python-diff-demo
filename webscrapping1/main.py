from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())
    # tags = soup.find('h5') # searches for the first occurence and stops the execution
    courses_html_tags = soup.find_all('h5') # returns all the occurences in a list 
    for courses in courses_html_tags:
        print(courses.text)

    # price_html_tags = soup.find_all('a')
    # for price in price_html_tags:
    #     print(price.text)

    course_cards = soup.find_all('div', class_='card')
    for card in course_cards:
        course_name = card.h5.text
        course_price = card.a.text.split()[-1]
        print(f'{course_name} costs {course_price}')
