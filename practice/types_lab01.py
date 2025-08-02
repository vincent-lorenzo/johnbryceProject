servers = ["server1","server2", "server3"]
active_servers = servers

active_servers.append("server4")
print(servers)
print(id(servers))

print(active_servers)
print(id(active_servers))

server_ip = "192.168.1.1"
print(server_ip)
print(id(server_ip))

server_ip = server_ip + (":80")
print(server_ip)
print(id(server_ip))

server_endpoint = server_ip
print(server_endpoint)
print(id(server_endpoint))

server_roles = {
    "server1": "web",
    "server2": "db", 
    "server3": "cache"
}
print(server_roles)

server_roles["server4"] = "monitoring"
print(server_roles)

all_roles = server_roles
all_roles["server1"] = "proxy"
print(all_roles)

def update_server_list(servers): 
    servers.append("server5 ")

print(servers)

update_server_list(servers)

print(servers)

