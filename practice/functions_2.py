def check_health(server): 
    print(f"Pinging {server}")
    # simulated ping command 
    print(f"{server} is healthty")

check_health("192.168.1.1")
check_health("192.168.1.2")
check_health("192.168.10.0")