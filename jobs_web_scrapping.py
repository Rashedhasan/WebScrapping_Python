from bs4 import BeautifulSoup
import requests


unfamiliar_skills=input('>')
def find_jobs():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup=BeautifulSoup(html_text,'lxml')
    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        published_date=job.find('span',class_='sim-posted').span.text
        if 'few' in published_date:
            more_info=job.header.h2.a['href']
            jo=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            skills=job.find('span',class_='srp-skills').text.replace(' ','')
            if unfamiliar_skills not in skills:
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f'company name: {jo.strip()}')
                    f.write(f'skills: {skills.strip()}')
                    f.write(f'page view: {more_info}')
    print('finished the jobs')

if __name__=='__main__':
    find_jobs()
