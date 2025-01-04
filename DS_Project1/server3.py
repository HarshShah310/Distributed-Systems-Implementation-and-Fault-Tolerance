from xmlrpc.server import SimpleXMLRPCServer
from concurrent.futures import ThreadPoolExecutor
import time

# Thread pool to handle asynchronous tasks
executor = ThreadPoolExecutor(max_workers=4)
results = {}

# Synchronous RPC functions
def add(i, j):
    return i + j

def sort_array(A):
    return sorted(A)

# Asynchronous RPC functions
def async_add(i, j, request_id):
    def perform_add():
        time.sleep(2)  
        result = i + j
        results[request_id] = result
    
    executor.submit(perform_add)
    return f"Request {request_id} acknowledged."

def async_sort(A, request_id):
    def perform_sort():
        time.sleep(3)  
        result = sorted(A)
        results[request_id] = result
    
    executor.submit(perform_sort)
    return f"Request {request_id} acknowledged."

def get_result(request_id):
    return results.pop(request_id, "Result not ready yet")

# Setting up the server
server = SimpleXMLRPCServer(("localhost", 8000))
print("Computation Server is running...")

# Register synchronous functions
server.register_function(add, "add")
server.register_function(sort_array, "sort")

# Register asynchronous functions
server.register_function(async_add, "async_add")
server.register_function(async_sort, "async_sort")
server.register_function(get_result, "get_result")

# Run the server
server.serve_forever()