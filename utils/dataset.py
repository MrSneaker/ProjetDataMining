import os
import zipfile

DATASET_NAME = "olistbr/brazilian-ecommerce"

def download_dataset():
    output_path = os.path.join(os.getcwd(), "datasets")
    
    # Get the kaggle username and key from the environment variables
    user = os.getenv("KAGGLE_USERNAME")
    key = os.getenv("KAGGLE_KEY")
    
    # Api request to download the dataset
    api_cmd = f"kaggle datasets download -d {DATASET_NAME} -p {output_path}"
    os.system(f"{api_cmd}")
    
    # Extract the downloaded zip file
    with zipfile.ZipFile(os.path.join(output_path, f"{DATASET_NAME.split('/')[1]}.zip"), 'r') as zip_ref:
        for file in zip_ref.namelist():
            print(f"Zip extract : {file}", end='\t')
            try:
                zip_ref.extract(file, output_path)
                print("\x1b[32mSuccess\x1b[0m")
            except Exception as e:
                print("\x1b[31mFailed\x1b[0m")
                print(e)
                
    # Remove the zip file
    os.remove(os.path.join(output_path, f"{DATASET_NAME.split('/')[1]}.zip"))

if __name__ == "__main__":
    download_dataset()