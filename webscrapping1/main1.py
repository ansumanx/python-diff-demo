from bs4 import BeautifulSoup
import requests # it is actually requesting information from a website
import time


print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}....')

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
# test = soup.find_all('ul', class_="new-joblist")
# for t in test:
#     print(t.text)
def find_job():
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        post_status =  job.find('span', class_='sim-posted').span.text
        if 'few' in post_status:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_='srp-skills').text.replace('"','')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required skills: {skills.strip()} \n")
                    f.write(f"More Info: {more_info}")
                print(f'File saved: {index}')


if __name__ == '__main__':
    count = 0
    while True:
        find_job()
        def timer():
            global count
            time_wait = 10
            count += 1
            total_wait_time = count * time_wait
            print(f'Waiting {time_wait} minutes')
            print(f'total wait time {total_wait_time}')
            time.sleep(time_wait * 60)
        timer()
        
        
        
        
        



# not an effiecient way of printing value 
        # print(f'''
        # Company Name: {company_name}
        # Required Skills: {skills}
        # ''')
        # print('')


