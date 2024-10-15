# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

# # Path to your WebDriver executable
# driver_path = '/home/shreya/Downloads/chromedriver/chromedriver'  # Update this path

# # Create a Service object
# service = Service(executable_path=driver_path)

# # Initialize the WebDriver with the Service object
# driver = webdriver.Chrome(service=service)

# try:
#     # Open the Google homepage
#     driver.get('https://www.google.com')

#     # Find the search box element using its name attribute
#     search_box = driver.find_element(By.NAME, 'q')

#     # Type a query into the search box and press Enter
#     search_box.send_keys('Selenium Python')
#     search_box.send_keys(Keys.RETURN)

#     # Wait for a few seconds to let the results load
#     driver.implicitly_wait(5)  # You can also use WebDriverWait for more precise waiting

#     # Print the title of the current page
#     print(driver.title)

# finally:
#     # Close the browser window
#     driver.quit()
