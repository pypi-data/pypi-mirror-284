# Install necessary packages using pip
# pip install selenium
# pip install webdriver-manager

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from os import getcwd

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--headless=new")

# Set up the preferences for microphone permissions
prefs = {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.notifications": 1,
}
chrome_options.add_experimental_option("prefs", prefs)

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Load the local HTML file
#website = f"file:///{getcwd()}/index.html"
website = "https://allorizenproject1.netlify.app/"
driver.get(website)

# Define the path for the output file
rec_file = f"{getcwd()}/input.txt"

def listen():
    try:
        start_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'startButton')))
        start_button.click()
        print("Listening...")
        output_text = ""

        while True:
            output_elements = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.ID, 'output')))
            if output_elements:
                current_text = output_elements[0].text.strip()  # Get text from the first element

            # Check the button text
            button_text = start_button.text

            if "Start Listening" in button_text:
                if output_text:
                    False
                
            elif "Listening..." in start_button.text:
                # continue listening
                True

            if current_text != output_text:
                output_text = current_text
                with open(rec_file, "w") as file:
                    file.write(output_text.lower())
                    print("SAKIB: " + output_text)

    except KeyboardInterrupt:
        True
    except Exception as e:
        print(e)
    finally:
        driver.quit()

listen()