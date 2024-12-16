# script.py
import pandas as pd
from pymongo import MongoClient
import os

# Función para conectar á base de datos MongoDB
def load_data_from_mongodb():
    client = MongoClient("mongodb://mongo:27017/")  # MongoDB no contedor
    db = client.citybikes_db
    collection = db.stations
    data = list(collection.find({}, {"_id": 0, "id": 1, "name": 1, "timestamp": 1, "free_bikes": 1, "empty_slots": 1, "uid": 1, "last_updated": 1, "slots": 1, "normal_bikes": 1, "ebikes": 1}))
    return pd.DataFrame(data)

# Función para exportar a CSV e Parquet
def export_dataframe(df):
    output_dir = "./output"
    os.makedirs(output_dir, exist_ok=True)
    
    # Exportar a CSV
    csv_path = os.path.join(output_dir, "stations_data.csv")
    df.to_csv(csv_path, index=False)
    print(f"Datos exportados a CSV: {csv_path}")

    # Exportar a Parquet
    parquet_path = os.path.join(output_dir, "stations_data.parquet")
    df.to_parquet(parquet_path, index=False)
    print(f"Datos exportados a Parquet: {parquet_path}")

if __name__ == "__main__":
    dataframe = load_data_from_mongodb()
    export_dataframe(dataframe)
