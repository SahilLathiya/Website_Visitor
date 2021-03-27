from selenium import webdriver
import pyautogui
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time

for i in range(27,2000):
    profile = FirefoxProfile(r'D:\\PROGRAM FILES\\Tor Browser\\Browser\\TorBrowser\\Data\\Browser\\profile.default')
    profile.set_preference('network.proxy.type', 1)
    profile.set_preference('network.proxy.socks', '127.0.0.1')
    profile.set_preference('network.proxy.socks_port', 9150)
    profile.set_preference("network.proxy.socks_remote_dns", False)
    profile.update_preferences()
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.binary_location = r'C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'
    driver = webdriver.Firefox(firefox_profile= profile, options = firefox_options, executable_path=r'D:\\Collage\\Sem 4\\Python\\Project\\geckodriver.exe')

    try:
        driver.get("https://diskoflyrics.blogspot.com/")
        time.sleep(10)
        driver.execute_script("window.scrollTo(0, 300)")
        python_button = driver.find_elements_by_xpath('''//*[@id="Blog1"]/div[1]/div[1]/div[1]/div/div[1]/a/img''')[0]
        python_button.click()
        driver.execute_script("window.scrollTo(0, 140)")
        driver.save_screenshot("D:\\Collage\\Sem 4\\Python\\Project\\Screenshots\\image{}.png".format(i))
        print('Took screenshot {}'.format(i))
        time.sleep(10)
    except Exception as e:
        print(e)
    driver.quit()
