from fastapi import FastAPI
from fastapi import FastAPI
import requests



app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Eurostat API"}


@app.get("/population/")
def get_population():

  url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?sort=1&file=data%2Flfsq_pganws.tsv.gz"

  response = requests.get(url)

  with open('estat_lfsq_pganws_en.csv', 'wb') as f:
      f.write(response.content)

  return {"message": "CSV downloaded"}
