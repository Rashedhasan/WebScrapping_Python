from bs4 import BeautifulSoup

with open('Home.html','r') as html_file:
    content=html_file.read()
    #print(content)
    soup=BeautifulSoup(content,'lxml')
    #print(soup.prettify())
    #tags=soup.find('h5')
    #tags=soup.find_all('h5')
    #tags=soup.find_all('h5')
    #for tag in tags:
        #print(tag)
        #print(tag.text)
    courses_card = soup.find_all('div',class_='card')
    for course in courses_card:
        course_name=course.h5.text
        course_price=course.a.text.split()[-1]
        print(f'{course_name} prices is {course_price}')
        #print(course_name)
        #print(course_price)
        #print(course.h5)
        #print(course)
    