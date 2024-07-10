def main():
    import requests
    import zipfile
    import os
    import shutil

    # URL of the ZIP file
    URL = "https://github.com/ravi46931/Default-project-structure/archive/refs/heads/main.zip"

    # Local path where you want to save the downloaded file
    local_zip_path = "project_structure.zip"
    # Directory where you want to extract the contents
    extract_to = "."

    # Step 1: Download the ZIP file
    response = requests.get(URL)
    with open(local_zip_path, "wb") as file:
        file.write(response.content)

    # Step 2: Extract the ZIP file to a temporary location
    with zipfile.ZipFile(local_zip_path, "r") as zip_ref:
        temp_extract_dir = "temp_extract"
        zip_ref.extractall(temp_extract_dir)

    # Step 3: Move the contents from the temporary extraction directory to the desired location
    source_dir = os.path.join(temp_extract_dir, "Default-project-structure-main")
    for item in os.listdir(source_dir):
        s = os.path.join(source_dir, item)
        d = os.path.join(extract_to, item)
        if os.path.isdir(s):
            if os.path.exists(d):
                shutil.rmtree(d)
            shutil.move(s, d)
        else:
            if os.path.exists(d):
                os.remove(d)
            shutil.move(s, d)

    # Clean up the temporary extraction directory and the downloaded zip file
    shutil.rmtree(temp_extract_dir)
    os.remove(local_zip_path)

    print(f"Downloaded and extracted to {extract_to}")

    # Uninstalling because when second run happens then the code of all files will be removed
    os.system("pip uninstall dstemplatest") 


