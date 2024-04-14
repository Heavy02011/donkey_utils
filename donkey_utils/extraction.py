import zipfile
import os

def extract_all_zips(source_folder, target_folder):
    """
    Extracts all ZIP files found in the source_folder into the target_folder.

    Parameters:
    - source_folder (str): The folder where ZIP files are located.
    - target_folder (str): The folder where the contents of the ZIP files should be extracted.
    """
    # Ensure the target folder exists
    os.makedirs(target_folder, exist_ok=True)
    
    # List all files in the source folder
    for filename in os.listdir(source_folder):
        #print(filename)
        if filename.endswith(".zip"):
            # Construct full file path
            zip_path = os.path.join(source_folder, filename)
            print(zip_path)
            # Open the ZIP file
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                # Extract all the contents into the target folder
                zip_ref.extractall(target_folder)
                print(f"Extracted {filename} into {target_folder}")

import gzip
import os
import shutil

def extract_all_gzs(source_folder, target_folder):
    """
    Extracts all .gz files found in the source_folder into the target_folder.

    Parameters:
    - source_folder (str): The folder where .gz files are located.
    - target_folder (str): The folder where the contents of the .gz files should be extracted.
    """
    # Ensure the target folder exists
    os.makedirs(target_folder, exist_ok=True)
    
    # List all files in the source folder
    for filename in os.listdir(source_folder):
        if filename.endswith(".gz"):
            # Construct full file path
            gz_path = os.path.join(source_folder, filename)
            # Construct target file path (without .gz extension)
            target_file_path = os.path.join(target_folder, filename[:-3])
            
            # Open the .gz file
            with gzip.open(gz_path, 'rb') as f_in:
                # Open the target file
                with open(target_file_path, 'wb') as f_out:
                    # Copy the decompressed data to the target file
                    shutil.copyfileobj(f_in, f_out)
                    print(f"Extracted {filename} into {target_folder}")

# Example usage
#source_folder = '/path/to/source/folder'  # Adjust to your source folder path
#target_folder = '/root'  # Adjust to your target folder path
#extract_all_gzs(source_folder, target_folder)

import tarfile
import os

def extract_all_tar_gzs(source_folder, target_folder):
    """
    Extracts all .tar.gz files found in the source_folder into the target_folder.

    Parameters:
    - source_folder (str): The folder where .tar.gz files are located.
    - target_folder (str): The folder where the contents of the .tar.gz files should be extracted.
    """
    # Ensure the target folder exists
    os.makedirs(target_folder, exist_ok=True)
    
    # List all files in the source folder
    for filename in os.listdir(source_folder):
        if filename.endswith(".tar.gz"):
            # Construct full file path
            tar_gz_path = os.path.join(source_folder, filename)
            # Open the .tar.gz file
            with tarfile.open(tar_gz_path, "r:gz") as tar:
                # Extract all the contents into the target folder
                tar.extractall(target_folder)
                print(f"Extracted {filename} into {target_folder}")

# Example usage
#source_folder = '/path/to/source/folder'  # Adjust to your source folder path
#target_folder = '/root'  # Adjust to your target folder path
#extract_all_tar_gzs(source_folder, target_folder)




########
import zipfile
import os

def extract_all_zips(source_folder, target_folder):
    os.makedirs(target_folder, exist_ok=True)
    for filename in os.listdir(source_folder):
        if filename.endswith(".zip"):
            zip_path = os.path.join(source_folder, filename)
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(target_folder)

def extract_all_gzs(source_folder, target_folder):
    import gzip
    import shutil
    os.makedirs(target_folder, exist_ok=True)
    for filename in os.listdir(source_folder):
        if filename.endswith(".gz"):
            gz_path = os.path.join(source_folder, filename)
            target_file_path = os.path.join(target_folder, filename[:-3])
            with gzip.open(gz_path, 'rb') as f_in, open(target_file_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

def extract_all_tar_gzs(source_folder, target_folder):
    import tarfile
    os.makedirs(target_folder, exist_ok=True)
    for filename in os.listdir(source_folder):
        if filename.endswith(".tar.gz"):
            tar_gz_path = os.path.join(source_folder, filename)
            with tarfile.open(tar_gz_path, "r:gz") as tar:
                tar.extractall(target_folder)
