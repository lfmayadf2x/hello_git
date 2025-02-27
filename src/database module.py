import requests
import pandas as pd


class DataBase:
    # Constructor
    def __init__(self):
        self.url = "https://www.datos.gov.co/resource/u3vn-bdcy.json"
    # Function get
    def get_date(self,n_data):
        request_url=self.url+f"?$limit={n_data}"
        response=requests.get(request_url)
        if response.status_code == 200:
            data = response.json()
            print(f"Datos obtenidos: {len(data)} registros")
            return pd.DataFrame(data)
        else:
            print("Error al obtener los datos:", response.status_code)
            return None

