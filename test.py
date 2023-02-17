from selenium import webdriver

# Указываем путь к драйверу Chrome
driver_path = "/path/to/chromedriver"

# Создаем экземпляр драйвера Chrome
driver = webdriver.Chrome(driver_path)

# Открываем сайт
driver.get("https://www.google.com")

# Закрываем браузер
driver.quit()


