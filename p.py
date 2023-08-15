from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def show_progress(block_num, block_size, total_size):
    number_of_blocks = total_size / block_size
    remaining = block_num / number_of_blocks * 100
    print(int(remaining), "%", end='\r')


options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
prefs = {"download.default_directory": r"C:/Users/fady9/Desktop/NBA/videos"}
options.add_experimental_option('prefs', prefs)

try:
    driver = webdriver.Chrome(options=options)
    driver.get('https://thehighlow.io/video/ids?ids=19vOTC')
    wait = WebDriverWait(driver, 10)
    video = wait.until(EC.presence_of_element_located((By.TAG_NAME, "video")))
    video_url = video.get_property('src')

    if video_url:
        try:
            urllib.request.urlretrieve(video_url, "C:/Users/fady9/Desktop/NBA/videos\\1.mp4", show_progress)
            print("\nDownloaded from the high low")
        except Exception as e:
            print(e)
    else:
        print("no url found")
except TimeoutException as e:
    print("Can't load webpage")
except Exception as e:
    print("Error loading the video")
