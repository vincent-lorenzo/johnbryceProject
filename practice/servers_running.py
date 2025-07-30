
server_status = input (" what is the server status : ")

if server_status == "running" :
    print("the server is operational")
elif server_status == "stopped":
    print("the server is down. Restart required")
elif server_status == "error":
    print("the server is in an error state. immediate action required!")
else: 
    print("Invalid status entered")

servers_names = ["server1" , "server2" , "server3"]

for server in servers_names : 
    print(f"pinging <{server}>")
    print(f"Ping to <{server}> successful.")

server_dict = {
    "server1" : "running",
    "server2" : "error",
    "server3" : "stopped"
}

for server , status in server_dict.items():
    if status == "error":
        print(f"restaring {server}")
    else: 
        print(f"{server} is healthy")