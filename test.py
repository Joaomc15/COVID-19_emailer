from selenium import webdriver
import selenium
from time import sleep



def get_stats(state, county):
    chrome_path = r"D:\Programming Projects\chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    driver.maximize_window()
    driver.get(f"https://www.bing.com/covid/local/{county}_{state}_unitedstates")



    is_true = False
    while not is_true: 
        try:
            case_value = driver.find_element_by_xpath('''//*[@id="main"]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]''') 
            is_true = True
        except selenium.common.exceptions.NoSuchElementException:
            print('nope didnt work try again, local')
            driver.refresh()
            sleep(3)

    
    case_string = str(case_value.text)
    try:
        case_int = int(case_string.replace(',',''))
    except ValueError:
        case_int = 'Unavaible'

    active_value = driver.find_element_by_xpath('''//*[@id="main"]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/h2[1]/div[3]''')
    active_string =str(active_value.text)
    try:
        active_int = int(active_string.replace(',',''))
    except ValueError:
        active_int = 'unavailable'





    death_value = driver.find_element_by_xpath('''//*[@id="main"]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/h2[3]/div[3]''')
    death_string = str(death_value.text)
    try:
        death_int = int(death_string.replace(',',''))
    except ValueError:
        death_int = 'Unavaible'

    county_name = driver.find_element_by_xpath('''//*[@id="main"]/div/div[1]/div[2]/div[2]/div[1]/h2''').text




    #-------------------------------------------------------------------------------------------------------------------------------------
    #State Values
    driver.get(f"https://www.bing.com/covid/local/florida_unitedstates")

    is_true = False
    while not is_true: 
        try:
            state_case_value = driver.find_element_by_xpath('''//*[@id="main"]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]''')
            is_true = True
        except selenium.common.exceptions.NoSuchElementException:
            print('nope didnt work, trying again state')
            driver.refresh()
            sleep(3)

    state_case_string =str(state_case_value.text)
    try:
        state_case_int = int(state_case_string.replace(',',''))
    except ValueError:
        state_case_int = 'unavailable'
    
        
    state_active_value = driver.find_element_by_xpath('''//*[@id="main"]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/h2[1]/div[3]''')
    state_active_string =str(state_active_value.text)
    try:
        state_active_int = int(state_active_string.replace(',',''))
    except ValueError:
        state_active_int = 'unavailable'
    
    state_recovered_value = driver.find_element_by_xpath('''//*[@id="main"]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/h2[2]/div[3]''')
    state_recovered_string =str(state_recovered_value.text)
    try:
        state_recovered_int = int(state_recovered_string.replace(',',''))
    except ValueError:
        state_recovered_int = 'unavailable'
    
    
    state_death_value = driver.find_element_by_xpath('''//*[@id="main"]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/h2[3]/div[3]''')
    state_death_string =str(state_death_value.text)
    try:
        state_death_int = int(state_death_string.replace(',',''))
    except ValueError:
        state_death_int = 'unavailable'
    

    state_name = driver.find_element_by_xpath('''//*[@id="main"]/div/div[1]/div[2]/div[2]/div[1]/h2''').text



    #-------------------------------------------------------------------------------------------------------------------------------------
    #National Values
    driver.get(f"https://www.bing.com/covid/local/unitedstates")

    is_true = False
    while not is_true: 
        try:
            national_case_value = driver.find_element_by_xpath('''//*[@id="main"]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]''')
            is_true = True
        except selenium.common.exceptions.NoSuchElementException:
            print('nope didnt work, trying again national')
            driver.refresh()
            sleep(3)

    national_case_string =str(national_case_value.text)
    try:
        national_case_int = int(national_case_string.replace(',',''))
    except ValueError:
        national_case_int = 'unavailable'
    
    
        
    national_active_value = driver.find_element_by_xpath('''//*[@id="main"]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/h2[1]/div[3]''')
    national_active_string =str(national_active_value.text)
    try:
        national_active_int = int(national_active_string.replace(',',''))
    except ValueError:
        national_active_int = 'unavailable'
    

    national_recovered_value = driver.find_element_by_xpath('''//*[@id="main"]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/h2[2]/div[3]''')
    national_recovered_string =str(national_recovered_value.text)
    try:
        national_recovered_int = int(national_recovered_string.replace(',',''))
    except ValueError:
        national_recovered_int = 'unavailable'
    
    
    national_death_value = driver.find_element_by_xpath('''//*[@id="main"]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/h2[3]/div[3]''')
    national_death_string =str(national_death_value.text)
    try:
        national_death_int = int(national_death_string.replace(',',''))
    except ValueError:
        national_death_int = 'unavailable'
    

    country_name = driver.find_element_by_xpath('''//*[@id="main"]/div/div[1]/div[2]/div[2]/div[1]/h2''').text

    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #worldwide cases
    driver.get(f"https://www.bing.com/covid")

    is_true = False
    while not is_true: 
        try:
            global_case_value = driver.find_element_by_xpath('''//*[@id="main"]/div/div[1]/div[2]/div[1]/div[1]/div[2]''')
            is_true = True
        except selenium.common.exceptions.NoSuchElementException:
            print('nope didnt work, trying again global')
            driver.refresh()
            sleep(3)

    global_case_string =str(global_case_value.text)
    try:
        global_case_int = int(global_case_string.replace(',',''))
    except ValueError:
        global_case_int = 'unavailable'
    
    
        
    global_active_value = driver.find_element_by_xpath('''//*[@id="main"]/div/div[1]/div[2]/div[1]/div[1]/div[3]/h2[1]/div[3]''')
    global_active_string =str(global_active_value.text)
    try:
        global_active_int = int(global_active_string.replace(',',''))
    except ValueError:
        global_active_int = 'unavailable'
    

    global_recovered_value = driver.find_element_by_xpath('''//*[@id="main"]/div/div[1]/div[2]/div[1]/div[1]/div[3]/h2[2]/div[3]''')
    global_recovered_string =str(global_recovered_value.text)
    try:
        global_recovered_int = int(global_recovered_string.replace(',',''))
    except ValueError:
        global_recovered_int = 'unavailable'
    
    
    global_death_value = driver.find_element_by_xpath('''//*[@id="main"]/div/div[1]/div[2]/div[1]/div[1]/div[3]/h2[3]/div[3]''')
    global_death_string =str(global_death_value.text)
    try:
        global_death_int = int(global_death_string.replace(',',''))
    except ValueError:
        global_death_int = 'unavailable'
    

    # global_name = driver.find_element_by_xpath('''//*[@id="main"]/div/div[1]/div[2]/div[2]/div[1]/div''').text






    driver.close()
    return country_name, state_name, county_name, case_string, active_string, death_string, case_int, active_int, death_int,  state_case_string, state_active_string, state_recovered_string, state_death_string, state_case_int, state_active_int, state_recovered_int, state_death_int, national_case_string, national_active_string, national_recovered_string, national_death_string, national_case_int, national_active_int, national_recovered_int, national_death_int, global_case_string, global_active_string, global_recovered_string, global_death_string, global_case_int, global_active_int, global_recovered_int, global_death_int 



def make_msg():
    # state = input('State: ').lower().replace(' ','')
    # county = input('County: ').lower().replace(' ','').replace('-','')
    state = 'florida'
    county = 'miamidade'

    #for bold text
    


    country_name, state_name, county_name, case_string, active_string, death_string, case_int, death_int, active_int, state_case_string, state_active_string, state_recovered_string, state_death_string, state_case_int, state_active_int, state_recovered_int, state_death_int, national_case_string, national_active_string, national_recovered_string, national_death_string, national_case_int, national_active_int, national_recovered_int, national_death_int, global_case_string, global_active_string, global_recovered_string, global_death_string, global_case_int, global_active_int, global_recovered_int, global_death_int     =  get_stats(state, county)

    
    msg = f'''County Stats:\
            \nTotal Cases in {county_name}: {case_string}\
            \nActive Cases in {county_name}: {active_string}\
            \nTotal Deaths in {county_name}: {death_string}\
            \n\nState stats:\
            \nTotal Cases in {state_name}: {state_case_string}\
            \nActive Cases in {state_name}: {state_active_string}\
            \nRecovered Cases in {state_name}: Unavailable\nDeaths in {state_name}: {state_death_string}\
            \n\nNational Stats:\
            \nTotal Cases in the {country_name}: {national_case_string}\nActive Cases in the {country_name}: {national_active_string}\nRecovered Cases in the {country_name}: {national_recovered_string}\nDeaths in the {country_name}: {national_death_string}\
            \n\nGlobal stats:\
            \nGlobal Total cases: {global_case_string}\
            \nGlobal Active cases: {global_active_string}\
            \nGlobal Recovered cases: {global_recovered_string}\
            \nGlobal Deaths: {global_death_string}'''

    return msg





# fatality_value = driver.find_element_by_xpath('''//*[@id="map"]/div[2]/div[1]/div[5]/div[6]/div[2]/div[1]/span[4]''')
# fatality_list = []
# fatality_list = fatality_value.text

    # try:
    #     case_stop = case_list.index('\n')+1
    # except ValueError: 
    #     case_stop = 0
    #     case_list + '0'
    # try:
    #     death_stop = death_list.index('\n')+1
    # except ValueError:
    #     death_stop = 0
    #     death_list + '0'




    # # print(f'''New Cases: {test[0:stop]}\nTotal Cases: {test[stop+1:]} ''')
    # msg = f'''New Cases: {case_list[0:case_stop-1]}\
    #         \nTotal Cases: {case_list[case_stop:]}\
    #         \nNew Deaths: {death_list[0:death_stop]}\
    #         \nTotal Deaths: {death_list[death_stop:]}\
    #         \nFatality Rate: {fatality_list}'''




    # # print(f'''Total Cases: {res[1]}''')
    # # print(f'''New Cases Today: {res[0]}''')


    # sleep(1)
    # driver.close()

    

    # print(msg)

