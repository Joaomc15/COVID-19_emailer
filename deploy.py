from selenium import webdriver
import selenium
from time import sleep


def request():
    chrome_path = r"D:\Programming Projects\chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    driver.get("https://coronavirus.1point3acres.com/en")

    sleep(7)

    driver.execute_script("window.scrollTo(0, window.scrollY + 800)")
    sleep(1)
    driver.execute_script("window.scrollTo(0, window.scrollY + 800)")
    sleep(3)


    is_true = False
    while not is_true: 
        driver
        try:
            driver.find_element_by_xpath('''//*[@id="map"]/div[2]/div[1]/div[5]/div[6]/div/span[1]''').click()
            is_true = True
        except selenium.common.exceptions.ElementClickInterceptedException:
            print('nope didnt work try again')

    sleep(2)

    case_value = driver.find_element_by_xpath('''/html/body/div[1]/div/div[6]/div[2]/div[1]/div[5]/div[6]/div[2]/div[1]/span[2]''')
    case_list = []
    case_list = case_value.text
    
    death_value = driver.find_element_by_xpath('''//*[@id="map"]/div[2]/div[1]/div[5]/div[6]/div[2]/div[1]/span[3]''')
    death_list = []
    death_list = death_value.text
    

    fatality_value = driver.find_element_by_xpath('''//*[@id="map"]/div[2]/div[1]/div[5]/div[6]/div[2]/div[1]/span[4]''')
    fatality_list = []
    fatality_list = fatality_value.text

    try:
        case_stop = case_list.index('\n')+1
    except ValueError: 
        case_stop = 0
        case_list + '0'
    try:
        death_stop = death_list.index('\n')+1
    except ValueError:
        death_stop = 0
        death_list + '0'




    # print(f'''New Cases: {test[0:stop]}\nTotal Cases: {test[stop+1:]} ''')
    msg = f'''New Cases: {case_list[0:case_stop-1]}\
            \nTotal Cases: {case_list[case_stop:]}\
            \nNew Deaths: {death_list[0:death_stop]}\
            \nTotal Deaths: {death_list[death_stop:]}\
            \nFatality Rate: {fatality_list}'''




    # print(f'''Total Cases: {res[1]}''')
    # print(f'''New Cases Today: {res[0]}''')


    sleep(1)
    driver.close()
    print(msg)
    

    return msg

def get_graphing_values():
    return  

request()