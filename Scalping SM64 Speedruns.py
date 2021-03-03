from selenium import webdriver
from selenium.webdriver.common.keys import Keys

brackets = ["0","1","16","70","120"]
while True:
    print("Which kind of run?" + '\n' + "0 Star | 1 Star | 16 Star | 70 Star | 120 Star" + '\n' + "Input number of stars below")
    stars = input("")
    if stars in brackets:
        print("Please wait. The site is loading...")
        break
    else:
        print("\n" + "Please put a valid star number" + "\n")

for number in brackets:
    if number == stars:
        division = "#" + number + "_Star"

website_link = "http://www.speedrun.com/sm64"

CHROME_DRIVER_PATH = "driver/chromedriver.exe"
driver = webdriver.Chrome(CHROME_DRIVER_PATH)
driver.get(website_link + division)


find_last = driver.find_element_by_xpath('/html/body/main/div/div[3]/div/form/div/div[2]/table/tbody/tr[last()]/td[1]').text

last_num = ""
for character in find_last:
    if str(character) in ["d","h","n","r","s","t"]:
        break
    last_num += character

while True:
    print("Search for:" + "\n" + "1 = A single rank | 2 = A range of ranks" + "\n" + "Input number")
    get_range = input("")
    if str(get_range) == "1":
        while True:
            print("Input rank number (1 to " + last_num + ")")
            find_single = input("")
            try:
                if int(find_single) <= int(last_num) and int(find_single) > 0:
                    xpath_runner = int(find_single)
                    xpath_runner += 1
                    break
                else:
                    print("\n" + "Please put a valid rank number" + "\n")
            except:
                print("\n" + "Please put a valid rank number" + "\n")
        break
    elif str(get_range) == "2":
        print("Note: The more elements you search for, the longer it takes.", "\n")
        while True:
            print("Input rank range start (1 to " + last_num + ")")
            find_start = input("")
            if int(find_start) < int(last_num) and int(find_start) > 0:
                xpath_runner = int(find_start)
                xpath_runner += 1
                break
            else:
                print("\n" + "Please put a valid rank number" + "\n")
        while True:
            print("Input rank range end (1 to " + last_num + ")")
            find_end = input("")
            if int(find_end) <= int(last_num) and int(find_end) > 0 and int(find_end) > int(find_start):
                break
            else:
                print("\n" + "Please put a valid rank number" + "\n")
        break
    else:
        print("\n" + "Please put a valid input" + "\n")

xpath_details = 2
xpath = '/html/body/main/div/div[3]/div/form/div/div[2]/table/tbody/tr[' + str(xpath_runner) + ']/td[' + str(xpath_details) + ']'

class speedrunning:
    gamers = []
    spdrnr = {}
    def get_spdrnr_rank(dictionary):
        global xpath_runner, xpath_details
        xpath_details = 1
        elem = driver.find_element_by_xpath('/html/body/main/div/div[3]/div/form/div/div[2]/table/tbody/tr[' + str(xpath_runner) + ']/td[' + str(xpath_details) + ']').text

        spdrnr_rank = ""
        for character in elem:
            if str(character) in ["d","h","n","r","s","t"]:
                break
            spdrnr_rank += character
        speedrunning.spdrnr["rank"] = spdrnr_rank

    def get_spdrnr_name(dictionary):
        global xpath_runner, xpath_details
        xpath_details = 2
        try:
            elem = driver.find_element_by_xpath('/html/body/main/div/div[3]/div/form/div/div[2]/table/tbody/tr[' + str(xpath_runner) + ']/td[' + str(xpath_details) + ']/a')
            speedrunner_link = elem.get_attribute("href")

            reversed_name = []
            for letter in speedrunner_link[::-1]:
                if letter == "/":
                    speedrunner_name = ""
                    for letter2 in reversed_name[::-1]:
                        speedrunner_name += letter2
                    break
                reversed_name.append(letter)
        except:
            placeholder = "L"

        try:
            elem = driver.find_element_by_xpath('/html/body/main/div/div[3]/div/form/div/div[2]/table/tbody/tr[' + str(xpath_runner) + ']/td[' + str(xpath_details) + ']/span').text
            speedrunner_name = elem
        except:
            placeholder = "L"

        try:
            elem = elem = driver.find_element_by_xpath('/html/body/main/div/div[3]/div/form/div/div[2]/table/tbody/tr[' + str(xpath_runner) + ']/td[' + str(xpath_details) + ']/span/span').text
            speedrunner_name = elem
        except:
            placeholder = "L"
        
        speedrunning.spdrnr["name"] = speedrunner_name

    def get_spdrnr_time(dictionary):
        global xpath_runner, xpath_details
        xpath_details = 3
        elem = driver.find_element_by_xpath('/html/body/main/div/div[3]/div/form/div/div[2]/table/tbody/tr[' + str(xpath_runner) + ']/td[' + str(xpath_details) + ']').text
        spdrnr_time = elem
        speedrunning.spdrnr["time"] = spdrnr_time

    def get_spdrnr_verify(dictionary):
        global xpath_runner, xpath_details
        xpath_details = 5
        elem = driver.find_element_by_xpath('/html/body/main/div/div[3]/div/form/div/div[2]/table/tbody/tr[' + str(xpath_runner) + ']/td[' + str(xpath_details) + ']').text
        spdrnr_verify = elem
        if str(spdrnr_verify) == "Yes":
            speedrunning.spdrnr["verified"] = "Verified"
        else:
            speedrunning.spdrnr["verified"] = "Not Verified"

    def get_spdrnr_platform(dictionary):
        global xpath_runner, xpath_details
        xpath_details = 6
        elem = driver.find_element_by_xpath('/html/body/main/div/div[3]/div/form/div/div[2]/table/tbody/tr[' + str(xpath_runner) + ']/td[' + str(xpath_details) + ']').text
        spdrnr_platform = elem
        if str(spdrnr_platform) == "N64":
            speedrunning.spdrnr["platform"] = 'Nintendo 64'
        elif str(spdrnr_platform) == "VC":
            speedrunning.spdrnr["platform"] = 'Virtual Console'
        else:
            speedrunning.spdrnr["platform"] = 'Emulator'

    def get_spdrnr_date(dictionary):
        global xpath_runner, xpath_details
        xpath_details = 7
        elem = driver.find_element_by_xpath('/html/body/main/div/div[3]/div/form/div/div[2]/table/tbody/tr[' + str(xpath_runner) + ']/td[' + str(xpath_details) + ']').text
        spdrnr_date = elem
        if str(spdrnr_date) == "":
            speedrunning.spdrnr["date of run"] = "N/A"
        else:    
            speedrunning.spdrnr["date of run"] = spdrnr_date

    def show_spdrn(dictionary):
        global xpath_runner
        elem = driver.find_element_by_xpath('/html/body/main/div/div[3]/div/form/div/div[2]/table/tbody/tr[' + str(xpath_runner) + ']')
        spdrn = elem.get_attribute("data-target")
        speedrunning.spdrnr["video"] = spdrn

speedrunner = 0
try:
    if int(find_start) == 1:
        range_end = int(find_end)
    else:
        range_end = int(find_end) - int(find_start)
        range_end += 1
except:
    range_end = int(find_single)
    speedrunner = int(find_single)
    speedrunner -= 1

print("Scalping, Please wait...")
while int(speedrunner) < int(range_end):

    speedrunning.get_spdrnr_rank(speedrunning.spdrnr)
    speedrunning.get_spdrnr_name(speedrunning.spdrnr)
    speedrunning.get_spdrnr_time(speedrunning.spdrnr)
    speedrunning.get_spdrnr_verify(speedrunning.spdrnr)
    speedrunning.get_spdrnr_platform(speedrunning.spdrnr)
    speedrunning.get_spdrnr_date(speedrunning.spdrnr)
    speedrunning.show_spdrn(speedrunning.spdrnr)

    speedrunning.gamers.append(speedrunning.spdrnr)
    speedrunning.spdrnr = {}
    xpath_runner += 1
    speedrunner += 1

driver.close()

item = 0
spdgmr = speedrunning.gamers
print("")
for index in speedrunning.gamers:
    print("Rank: " + spdgmr[item]['rank'] + " ||", "Runner: " + spdgmr[item]['name'], "(" + spdgmr[item]['time'] + ")", " [" + spdgmr[item]['verified'] + "] ", "using " + spdgmr[item]['platform'] + " <", spdgmr[item]['date of run'] + " > ", "|| Link to run: speedrun.com" + spdgmr[item]['video'])

    item += 1
print("\n", "*Same rankings mean that they have the exact same time, therefore a tie*", "\n")

# link -- https://www.youtube.com/watch?v=
