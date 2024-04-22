import httpx
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self):
        self.client = httpx.Client()

    def get_html(self, url):
        # payload = {'prom': 'LGD', 'tujuan': 'RIAU', 'brt': '2', 'da': 'MOJOKERTO', 'tuj': 'PEKANBARU', 'le': '10', 'pa': '10', 'ti': '10', 'hitung': ''}
        payload = {'prom': 'LGD', 'tujuan': 'RIAU', 'brt': '2', 'da': 'MOJOKERTO', 'tuj': 'PEKANBARU', 'hitung': ''}
        r = self.client.post(url, data=payload)
        if r.status_code == 200:
            print("Response: OK")
            html = r.text
            return html
        else:
            print(f"Get {r.status_code} from {url} with data {payload}")

class Parser:
    def __init__(self, html):
        self.soup = BeautifulSoup(html, "html.parser")

    def cek_ongkir(self):
        result = dict()

        table_data = self.soup.find("table", "table table-bordered").find_all("td")
        rows_data = [row.text.strip() for row in table_data]
        if len(rows_data) == 5:
            label = ['dari', 'tujuan', 'estimasi', 'harga_kilogram', 'harga_kubikasi']
            for i in range(len(label)):
                result[label[i]] = rows_data[i]
            return result
        else:
            print("Some data might lost.")
            for i in range(len(label)):
                result[label[i]] = "None"
            return result



if __name__ == "__main__":
    url = "https://trackpage.bst-ekspres.com/?cek=tarif"
    
    scraper = Scraper()
    html = scraper.get_html(url=url)

    parser = Parser(html).cek_ongkir()
    print(parser)

    