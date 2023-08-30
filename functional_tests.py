from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://127.0.0.1:8000")
assert 'The install worked successfully! Congratulations!' in browser.title
print('OK')