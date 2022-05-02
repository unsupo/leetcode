import requests
from bs4 import BeautifulSoup


soup = BeautifulSoup(requests.get("https://e-com.secure.force.com/adidasUSContact/").content, "html.parser")

key = soup.select_one("#ncaptchaRecaptchaId")["data-sitekey"]
