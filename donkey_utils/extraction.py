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
