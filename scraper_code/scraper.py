import requests
from bs4 import BeautifulSoup
import re
import os




base_url = 'https://colorado.edu'
request = requests.get('https://www.colorado.edu/aerospace/people')
src = request.content
soup = BeautifulSoup(src,'html.parser')
container = soup.find_all('div',{"class":"person-view-mode-grid"})
#print(container[0].find_all('a').attrs('href'))



def get_faculty_bio_info(faculty_url):
    falculty_bio_info = []
    try:
        request = requests.get(faculty_url)
        src = request.content
        soup = BeautifulSoup(src,'html.parser')
        faculty_name = soup.find('h1',{"id":"page-title"}).get_text().strip()
    #print(faculty_name)
        falculty_bio_info.append(faculty_name + '--> ')
        falculty_container = soup.find('div',{"class":"content-wrapper section"})
        people_bio_segment = falculty_container.find('div',{"class":"people-bio"})
        people_bio_segment = people_bio_segment.find_all('p')
        people_bio_segment = ''.join([str(ele) for ele in people_bio_segment])
        people_bio_segment = re.sub(r'<br>|<br/>|</br>|<p>|</p>|<p/>|\n','',people_bio_segment)
    #print(people_bio_segment)
        falculty_bio_info.append(people_bio_segment)
        #falculty_bio_info.append('\n\n\n\n')
        falculty_bio_info = ''.join([str(faculty) for faculty in falculty_bio_info])
        return falculty_bio_info   
    except:
        print("Appriate Tag Missing from the faculty page")



def write_lst(lst,file_):
    try:
        with open(file_,'w') as f:
            for l in lst:
                f.write(l)
                f.write('\n')  
                
    except:
        print("Ohh|| Write Exception ocuuered somehow!!")





urls = []
for url_tag in container:
    urls.append(url_tag.find('a')['href'])
    
url_bio = []
faculty_bio_info_list = []

for url_new in urls:
    urls_temp = base_url + url_new
    
    url_bio.append(urls_temp)
    #print(get_faculty_bio_info(urls_temp))
    print('-'*20,'Found {} faculty profile urls'.format(len(url_new)),'-'*20)
    faculty_bio_info_list.append(get_faculty_bio_info(urls_temp))



#print(faculty_bio_info_list)


file_path = os.getcwd()
#print(file_path)


file_parts= file_path.split('/')

file_parts = '/'.join(file_parts[:-1])
file_parts = file_parts + '/'+ 'sample'+'/'
#print(file_parts)    
        
            
            
bio_urls_file = os.path.join(file_parts,'bio_urls.txt')
bios_file = os.path.join(file_parts,'bios.txt')
write_lst(url_bio,bio_urls_file)      
write_lst(faculty_bio_info_list,bios_file)





