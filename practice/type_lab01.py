server_id = 101
print(f"server_id is {server_id} and is of type : {type(server_id)}")

cpu_usage = 75.3 
print(f"cpu usage = {cpu_usage} and is of type : {type(cpu_usage)}")

status_msg = "server is missing"
print(f"status_msg = {status_msg} ans is of type : {type(status_msg)}")

is_ready = True
print(f"is_ready = {is_ready} and is of type : {type(is_ready)}")

raw_cpu_usage = "85.6"
raw_is_ready = "True"

print(float(raw_cpu_usage))
print(bool(raw_is_ready))

max_cpu_usage = 100.0
remaining_cpu = max_cpu_usage - cpu_usage  
remaining_cpu = round(remaining_cpu , 2)
print(f"remaining cpu  capacity : {remaining_cpu} %")

if is_ready and cpu_usage < 90.0 :
      print("server is operational")
else: 
    print("server is overloaded or not ready")

servers = [
{"id": 1, "cpu": 45.0, "status": "running", "ready": True},
{"id": 2, "cpu": 92.5, "status": "running", "ready": False},
{"id": 3, "cpu": 78.3, "status": "stopped", "ready": False},
]

for server in servers:
    current_server_id = server["id"]
    current_cpu_usage = server["cpu"]

    if server["ready"] and current_cpu_usage < 80.0 :
         print(f"server {current_server_id} is under normal load")
    else: 
         print(f"server {current_server_id} needs attention")