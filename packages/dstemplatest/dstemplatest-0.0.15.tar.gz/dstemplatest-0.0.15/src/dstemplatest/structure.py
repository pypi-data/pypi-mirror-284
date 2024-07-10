import requests
import zipfile
import os
import shutil
# from constants import URL
URL = "https://github.com/ravi46931/Default-project-structure/archive/refs/heads/main.zip"

# URL of the ZIP file
url = URL
# Local path where you want to save the downloaded file
local_zip_path = "project_structure.zip"
# Directory where you want to extract the contents
extract_to = "."

# Step 1: Download the ZIP file
response = requests.get(url)
with open(local_zip_path, "wb") as file:
    file.write(response.content)

# Step 2: Extract the ZIP file to a temporary location
with zipfile.ZipFile(local_zip_path, "r") as zip_ref:
    temp_extract_dir = "temp_extract"
    zip_ref.extractall(temp_extract_dir)

# Step 3: Move the contents from the temporary extraction directory to the desired location
for item in os.listdir(os.path.join(temp_extract_dir, "Default-project-structure-main")):
    s = os.path.join(temp_extract_dir, "Default-project-structure-main", item)
    d = os.path.join(extract_to, item)
    if os.path.isdir(s):
        shutil.move(s, d)
    else:
        shutil.move(s, d)

# Clean up the temporary extraction directory and the downloaded zip file
shutil.rmtree(temp_extract_dir)
os.remove(local_zip_path)

print(f"Downloaded and extracted to {extract_to}")
