from fastapi import FastAPI

from scrap import main


app = FastAPI()


@app.get("/")
def read_root():
    return {"BarakaCustomAPI": "Build with FastApi"}

@app.get("/cek_ongkir/")
def cek_ongkir(prom, tujuan, da, tuj, brt=0, le=0, pa=0, ti=0):
    payload = {'prom': prom, 'tujuan': tujuan, 'brt': brt, 'kol':'0', 'le':le, 'pa':pa, 'ti':ti, 'da': da, 'tuj': tuj, 'hitung': ''}
    ongkir = main(payload)
    return ongkir
