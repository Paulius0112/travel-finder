import typing
from urllib import response
import pycountry
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import lxml

API = "https://www.skyscanner.net/transport/flights-from/"


class SkyScannerAPI:

    def get_country_code(self, country: str) -> str:
        code = pycountry.countries.get(name=country).alpha_2
        return str(code)

    def get_flights(self, origin: str):
        origin_code = self.get_country_code(origin)

        request_url = API + origin_code
        print(f"Request url: {request_url}")

        session = HTMLSession()
        r = session.get(request_url)
        soup = BeautifulSoup(r.html.raw_html, "html.parser")
        b = soup.find_all("div", {"class": "browse-list-category"})
        print(b.text)

        

