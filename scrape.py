from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By
import csv

user=""
password=""

def scrape():
    """Function for scraping information off of solus course pages and formatting them in a csv."""

    course_code=driver.find_element(By.ID,"DERIVED_CLSRCH_DESCR200").get_attribute("innerHTML")
    course_type=driver.find_element(By.ID,"DERIVED_CLSRCH_SSS_PAGE_KEYDESCR").get_attribute("innerHTML")
    date_time=driver.find_element(By.ID,"MTG_SCHED$0").get_attribute("innerHTML")
    location=driver.find_element(By.ID,"MTG_LOC$0").get_attribute("innerHTML")
    enrollment=driver.find_element(By.ID,"SSR_CLS_DTL_WRK_ENRL_TOT").get_attribute("innerHTML")
    instructor=driver.find_element(By.ID,"MTG_INSTR$0").get_attribute("innerHTML")
    data=[course_code,course_type,date_time,location,enrollment,instructor]
    f= open('./data.csv','a')
    writer=csv.writer(f)
    writer.writerow(data)
    f.close()

#initialize csv
f= open('./data.csv','w')
header=["course","type/info","day+time","location","enrollment","Instructor"]
writer=csv.writer(f)
writer.writerow(header)
f.close()

S=Service('./chromedriver')
driver = webdriver.Chrome(service=S)

#get main homepage
driver.get('https://my.queensu.ca/')
driver.get("https://my.queensu.ca/sidebar/20")
#input user name
box1=driver.find_element(By.ID,"i0116")
box1.send_keys(user)

#click button
user_button=driver.find_element(By.ID,"idSIButton9")
user_button.click()

#enter pass
box2=driver.find_element(By.ID,"i0118")
box2.send_keys(password)
time.sleep(3)

#submit
pass_button=driver.find_element(By.CLASS_NAME,"button")
pass_button.click()

#sleep for 2fa
time.sleep(25)
course=100

while(course<600):
    #route to search
    driver.get("https://saself.ps.queensu.ca/psc/saself/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.CLASS_SEARCH.GBL?Page=SSR_CLSRCH_ENTRY&Action=U&ExactKeys=Y")
    
    #at end of search go to graduate level courses
    if(course!=599):
        driver.find_element(By.ID,"SSR_CLSRCH_WRK_CATALOG_NBR$1").send_keys(str(course))
        #select undergraduate
        select=Select(driver.find_element(By.ID,"SSR_CLSRCH_WRK_ACAD_CAREER$2"))
        select.select_by_index(3)

    #regular undergrad courses
    if(course==599):
        #change dropdown to less than or equal
        select1=Select(driver.find_element(By.ID,"SSR_CLSRCH_WRK_SSR_EXACT_MATCH1$1"))
        select1.select_by_index(4)
        #type in box
        driver.find_element(By.ID,"SSR_CLSRCH_WRK_CATALOG_NBR$1").send_keys(str(course))
        #select graduate
        select2=Select(driver.find_element(By.ID,"SSR_CLSRCH_WRK_ACAD_CAREER$2"))
        select2.select_by_index(1)
    

    #unclick checkbox
    checkbox=driver.find_element(By.ID,"SSR_CLSRCH_WRK_SSR_OPEN_ONLY$5")
    if(checkbox.get_attribute("value")!="N"):
        checkbox.click()

    #search
    submit=driver.find_element(By.ID,"CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH")
    submit.click()

    time.sleep(4)
    count=0
    
    #inner while
    while(True):
        try:
            time.sleep(2)
            current_tile=driver.find_element(By.NAME,"MTG_CLASS_NBR$"+str(count))
            current_tile.click()
            time.sleep(3)
            scrape()
            count=count+1
            return_to_search=driver.find_element(By.ID,"CLASS_SRCH_WRK2_SSR_PB_BACK")
            return_to_search.click()
            time.sleep(6)
        except:
            break

    course=course+1

time.sleep(10)