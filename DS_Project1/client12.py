import xmlrpc.client as xc
import os
import time

# Connect to XML-RPC server
server = xc.ServerProxy("http://localhost:8000")

def list_local_files(directory):
    files_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            relative_path = os.path.relpath(os.path.join(root, file), directory)
            files_list.append(relative_path)
    return files_list

sync_directory = "dropbox/"
local_files = list_local_files(sync_directory)
if not os.path.exists(sync_directory):
    os.makedirs(sync_directory)

operation = 10
while operation != 0:
    print("-----------------------------------------------------------")
    print("Choose an operation:")
    print("1: Upload a file")
    print("2: Download a file")
    print("3: Delete a file")
    print("4: Rename a file")
    print("0: Exit")
    operation = int(input("Your choice: "))
    print("----------------------------------------------------------")

    if operation == 1:
        file_name = input("Enter the file name with extension: ")
        with open(file_name, "rb") as file:
            content = xc.Binary(file.read())
            result = server.upload_file(file_name, content)
            print(f"{file_name} UPLOADED: {result}")

    elif operation == 2:
        file_name = input("Enter the file name with extension: ")
        content = server.download_file(file_name)
        with open(file_name, "wb") as file:
            file.write(content.data)
            print(f"DOWNLOAD Result: File downloaded as {file_name}")

    elif operation == 3:
        file_name = input("Enter the file name with extension: ")
        result = server.delete_file(file_name)
        print(f"{file_name} DELETED: {result}")

    elif operation == 4:
        old_name = input("Enter the existing file name with extension: ")
        new_name = input("Enter the new file name: ")
        result = server.rename_file(old_name, new_name)

    elif operation == 0:
        break

# Synchronize local files (Dropbox) with the server
sync_interval = 2
last_sync_time = time.time()

while True:
    current_files = list_local_files(sync_directory)

    added_files = [file for file in current_files if file not in local_files]
    removed_files = [file for file in local_files if file not in current_files]
    updated_files = [file for file in local_files if file in current_files]

    for file in added_files:
        file_path = os.path.join(sync_directory, file)
        with open(file_path, "rb") as file_content:
            content = xc.Binary(file_content.read())
            result = server.upload_file(file, content)
            print(f"Uploaded: {file} ({result})")

    for file in removed_files:
        result = server.delete_file(file)
        print(f"Deleted: {file} ({result})")

    for file in updated_files:
        file_path = os.path.join(sync_directory, file)
        modification_time = os.path.getmtime(file_path)

        if modification_time > last_sync_time:
            with open(file_path, "rb") as file_content:
                content = xc.Binary(file_content.read())
                result = server.upload_file(file, content)
                print(f"Uploaded (Modified): {file} ({result})")

    local_files = current_files
    last_sync_time = time.time()

    time.sleep(sync_interval)
