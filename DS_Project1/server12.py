import os
import xmlrpc.server as xs
import threading
import xmlrpc.client as xc

# Directory to store server files
server_directory = "server_storage/"

class FileService:
    def __init__(self):
        print("File server is now active...")
        self.files_on_server = {}  # Dictionary to track files and their modification times

    def upload_file(self, filename, content):
        file_path = os.path.join(server_directory, filename)
        with open(file_path, "wb") as file:
            file.write(content.data)
        self.files_on_server[filename] = os.path.getmtime(file_path)  # Update modification time
        return "Success"

    def download_file(self, filename):
        try:
            file_path = os.path.join(server_directory, filename)
            with open(file_path, "rb") as file:
                content = xc.Binary(file.read())
            return content
        except FileNotFoundError:
            raise Exception("File does not exist")

    def delete_file(self, filename):
        try:
            file_path = os.path.join(server_directory, filename)
            os.remove(file_path)
            del self.files_on_server[filename]  # Remove file from the server
            return "Success"
        except FileNotFoundError:
            raise Exception("File not found")

    def rename_file(self, old_filename, new_filename):
        try:
            old_file_path = os.path.join(server_directory, old_filename)
            new_file_path = os.path.join(server_directory, new_filename)

            # Check if the old file exists
            if not os.path.exists(old_file_path):
                raise FileNotFoundError(f"The file '{old_filename}' does not exist on the server.")

            # Check if the new file name already exists
            if os.path.exists(new_file_path):
                raise FileExistsError(f"A file with the name '{new_filename}' already exists on the server.")

            # Rename the file
            os.rename(old_file_path, new_file_path)
            self.files_on_server[new_filename] = os.path.getmtime(new_file_path)  
            del self.files_on_server[old_filename]  
            return "Success"
        except FileNotFoundError as e:
            return f"Error: {str(e)}"
        except FileExistsError as e:
            return f"Error: {str(e)}"
        except Exception as e:
            return f"{new_filename}"

    def synchronize_files(self, client_files):
        for filename, content in client_files.items():
            file_path = os.path.join(server_directory, filename)
            with open(file_path, "wb") as file:
                file.write(content.data)
            self.files_on_server[filename] = os.path.getmtime(file_path)  # Update modification time

    def list_files(self):
        return self.files_on_server

if __name__ == "__main__":
    if not os.path.exists(server_directory):
        os.makedirs(server_directory)

    server = xs.SimpleXMLRPCServer(("localhost", 8000))
    server.register_instance(FileService())

    # Handle client requests in a separate thread
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()
