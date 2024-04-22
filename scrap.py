import httpx
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self):
        self.client = httpx.Client()
        self.cek_tarif = "https://trackpage.bst-ekspres.com/?cek=tarif"


    def get_html(self, payload):
        r = self.client.post(self.cek_tarif, data=payload)
        if r.status_code == 200:
            print("Response: OK")
            html = r.text
            return html
        else:
            print(f"Get {r.status_code}. Please check {payload}")

class Parser:
    def __init__(self, html):
        self.soup = BeautifulSoup(html, "html.parser")

    def extract_ongkir(self):
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
        
def main(payload):
    scraper = Scraper()
    html = scraper.get_html(payload)

    parser = Parser(html)
    ongkir = parser.extract_ongkir()
    return ongkir


if __name__ == "__main__":
    payload = {'prom': 'JBAR', 'tujuan': 'JABAR', 'brt': '2', 'kol':'0', 'le':'10', 'pa':'10', 'ti':'10', 'da': 'CIAWI TASIK', 'tuj': 'LEMBANG', 'hitung': ''}
    
    ongkir = main(payload)
    print(ongkir)
