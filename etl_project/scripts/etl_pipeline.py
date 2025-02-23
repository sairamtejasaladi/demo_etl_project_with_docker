import requests
import shutil
import tarfile
import os
import pandas as pd

staging_path = "/opt/airflow/data"  # ✅ Change this

def download_dataset():
    url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz'
    destination = os.path.join(staging_path, "tolldata.tgz")  
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(destination, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        print("Dataset downloaded successfully.")
        return True
    else:
        print("Failed to download dataset.")
        return False

def untar_dataset():
    tar_files = [f for f in os.listdir(staging_path) if f.endswith('.tgz')]
    if tar_files:
        tar_path = os.path.join(staging_path, tar_files[0])
        with tarfile.open(tar_path, 'r:gz') as tar:
            tar.extractall(path=staging_path)
        print("Dataset extracted successfully.")
    else:
        print("No tar.gz file found in staging.")

def extract_data_from_csv():
    input_file = os.path.join(staging_path,'vehicle-data.csv' )
    output_file = os.path.join(staging_path, 'csv_data.csv')
    required_fields = ['Rowid','Timestamp','Anonymized Vehicle number','Vehicle type']
    df = pd.read_csv(input_file , index_col=False, header = None) 
    print(df.columns)
    #only frst four columns are required
    data = df.iloc[:, 0:4]
    # writing to csv file
    data.columns = required_fields
    data.to_csv(output_file, index=False) #write with header
    print("Data extracted successfully.")
    return True 

def extract_data_from_tsv():
    # staging_path = r"C:\Users\saladi.sairamteja\Documents\personal_ETL_project\etl_project\data"
    input_file = os.path.join(staging_path, 'tollplaza-data.tsv')
    output_file = os.path.join(staging_path, 'tsv_data.csv')
    columns_required = ['Number of axles', 'Tollplaza id', 'Tollplaza code']
    # using pandas to read tsv file
    import pandas as pd
    df = pd.read_csv(input_file, sep='\t')
    # only last three columns are required
    df = df.iloc[:,-3:]
    df.columns = columns_required
    # writing to tsv file
    df.to_csv(output_file, index=False)
    print("Data extracted successfully.")
    return True

def extract_data_from_fixed_width():
    # staging_path = r"C:\Users\saladi.sairamteja\Documents\personal_ETL_project\etl_project\data"
    input_file = os.path.join(staging_path, "payment-data.txt")
    output_file = os.path.join(staging_path, "fixed_width_data.csv")
    
    if os.path.exists(input_file):
        colspecs = [(48, 51), (52, 57)]  # Column positions for Type of Payment code and Vehicle Code
        df = pd.read_fwf(input_file, colspecs=colspecs, header=None, names=["Type of Payment code", "Vehicle Code"])
        df.to_csv(output_file, index=False)
        print("Fixed-width data extracted successfully.")
    else:
        print("Fixed-width input file not found.")


# Function to consolidate extracted data into a single CSV
def consolidate_data():
    # staging_path = r"C:\Users\saladi.sairamteja\Documents\personal_ETL_project\etl_project\data"
    csv_file = os.path.join(staging_path, "csv_data.csv")
    tsv_file = os.path.join(staging_path, "tsv_data.csv")
    fixed_width_file = os.path.join(staging_path, "fixed_width_data.csv")
    output_file = os.path.join(staging_path, "extracted_data.csv")
    
    if os.path.exists(csv_file) and os.path.exists(tsv_file) and os.path.exists(fixed_width_file):
        df_csv = pd.read_csv(csv_file)
        df_tsv = pd.read_csv(tsv_file, sep='\t')
        df_fixed = pd.read_csv(fixed_width_file)
        
        df_final = pd.concat([df_csv, df_tsv, df_fixed], axis=1)
        df_final.to_csv(output_file, index=False)
        print("Data consolidated successfully into extracted_data.csv.")
    else:
        print("One or more input files are missing.")

# Function to transform vehicle_type field to uppercase
def transform_data():
    # staging_path = r"C:\Users\saladi.sairamteja\Documents\personal_ETL_project\etl_project\data"
    input_file = os.path.join(staging_path, "extracted_data.csv")
    output_file = os.path.join(staging_path, "transformed_data.csv")
    
    if os.path.exists(input_file):
        df = pd.read_csv(input_file)
        if "Vehicle type" in df.columns:
            df["Vehicle type"] = df["Vehicle type"].str.upper()
            df.to_csv(output_file, index=False)
            print("Data transformed successfully into transformed_data.csv.")
        else:
            print("Vehicle type column not found in extracted_data.csv.")
    else:
        print("Extracted data file not found.")


