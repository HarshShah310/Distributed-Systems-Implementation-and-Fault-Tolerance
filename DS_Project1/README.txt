# DS_Project1

This project demonstrates a client-server architecture using Remote Procedure Call (RPC) communication. The client can interact with a file server and a computation server to perform various operations.

# Features

File Server Functions:
- Upload: Upload a file from the client's local folder to the server.
- Download: Download a file from the server's folder to the client's local machine.
- Delete: Delete a file from the server.
- Rename: Rename a file on the server.
- Dropbox-like Synchronization: Changes made to the synchronized folder at the client side will automatically trigger the corresponding operation on the server to update the folder at the server side.

Computation Server Functions:
- Add(i, j): Perform an addition of two integers and return the result.
- Sort(Array A): Sort an array of integers and return the sorted array.
- Supports both Synchronous and Asynchronous RPC calls.

# File Structure

- `server12.py`: Implements the file server functionality for UPLOAD, DELETE, RENAME, and Dropbox-like synchronization.
- `client12.py`: Implements the client that communicates with the file server.
- `server3.py`: Implements the computation server with add and sort operations using synchronous and asynchronous RPC.
- `client3.py`: Implements the client that communicates with the computation server.

# Code Execution

To execute the programs:

Part 1 & Part 2 (File Server)

1. Open the terminal or command prompt and navigate to the directory containing the project files.
2. Run the server by executing:
   ```
   python server12.py
   ```
3. Run the client by executing:
   ```
   python client12.py
   ```

Part 3 (Computation Server)

1. Open the terminal or command prompt and navigate to the directory containing the project files.
2. Run the server by executing:
   ```
   python server3.py
   ```
3. Run the client by executing:
   ```
   python client3.py
   ```

# Notes

- Python version used: 3.12.2
- Dependencies: Ensure necessary Python libraries are installed.
