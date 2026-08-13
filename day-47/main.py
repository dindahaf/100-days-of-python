import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

amazon_url_dummy = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/Bedsure-Pillowcases-Similar-Sleeping-Envelope/dp/B0725WFLMB?pd_rd_w=vVZIN&content-id=amzn1.sym.e4e36d35-6fa1-4c77-a0e8-c66ae402378f&pf_rd_p=e4e36d35-6fa1-4c77-a0e8-c66ae402378f&pf_rd_r=VF07KWTTM46RHQ6RHQ85&pd_rd_wg=danRc&pd_rd_r=163b1a73-2bc7-43db-a361-b552f16c67da&pd_rd_i=B0725WFLMB&ref_=dossier_default_ref_B0725WFLMB&th=1"

header = {	
    "Accept":	"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding":	"gzip, deflate, br, zstd",
    "Accept-Language":	"en-GB,en;q=0.9",
    "Priority":	"u=0, i",
    "Sec-Fetch-Dest":	"document",
    "Sec-Fetch-Mode":	"navigate",
    "Sec-Fetch-Site":	"none",
    "Sec-Fetch-User":	"?1",
    "Upgrade-Insecure-Requests":	"1",
    "User-Agent":	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:153.0) Gecko/20100101 Firefox/153.0",
}


response = requests.get(url=live_url, headers=header)

soup = BeautifulSoup(response.text, "html.parser")
price = soup.find(name="span", class_="a-price-whole").getText()

price_as_float = float(price.replace(",", ""))
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

# If you pass some headers along then Amazon's servers can give you the instant pot page in your language and also in your currency.



BUY_PRICE = 120000

if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"
    with smtplib.SMTP("smtp.gmail.com" , port=587) as connection:
        connection.starttls()
        connection.login(user=os.environ["MY_EMAIL"], password=os.environ["MY_EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["MY_EMAIL"],
            to_addrs="dindahaf@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{live_url}".encode("utf-8")
        )
        print("Email sent successfully")
