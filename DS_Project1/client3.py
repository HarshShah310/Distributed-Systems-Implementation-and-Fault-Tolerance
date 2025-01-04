import xmlrpc.client
import time

# Connect to the server
client = xmlrpc.client.ServerProxy("http://localhost:8000/")

# 1. Synchronous RPCs
print("=== Synchronous RPCs ===")
result_add = client.add(5, 3)
print("Synchronous Add:", result_add)

result_sort = client.sort([5, 1, 3, 4, 2])
print("Synchronous Sort:", result_sort)

# 2. Asynchronous RPCs
print("\n=== Asynchronous RPCs ===")
request_id_add = 1
request_id_sort = 2

# Asynchronous add and sort calls
ack_add = client.async_add(5, 3, request_id_add)
ack_sort = client.async_sort([5, 1, 3, 4, 2], request_id_sort)

print(ack_add)
print(ack_sort)

print("Doing other work while waiting for results...")
time.sleep(5)

# Fetch asynchronous results
result_add_async = client.get_result(request_id_add)
result_sort_async = client.get_result(request_id_sort)

print("Asynchronous Add Result:", result_add_async)
print("Asynchronous Sort Result:", result_sort_async)