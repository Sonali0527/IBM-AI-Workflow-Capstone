import pandas as pd
import glob
import json

def ingest_data(data_path="data/invoices-*.json"):
    """Ingest JSON invoices into DataFrame for automation"""
    files = glob.glob(data_path)
    all_data = []
    for f in files:
        with open(f) as fp:
            data = json.load(fp)
            all_data.extend(data)
    df = pd.DataFrame(all_data)
    df['invoice_date'] = pd.to_datetime(df['invoice_date'])
    return df

if __name__ == "__main__":
    df = ingest_data()
    print(f"Ingested {len(df)} records from {df['invoice_date'].min()} to {df['invoice_date'].max()}")
