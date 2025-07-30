def restart_service(service_name , delay=0):
    print(f"restarting {service_name} in {delay} seconds ...")

restart_service("nginx")
restart_service("docker" , delay=5)

def create_user(username, role):
    print(f"creating user {username} with role {role}...")

create_user(role= "admin", username= "vincent")

def package_install(*packages):
    print(f"Installing {packages}...")

package_install("nginx", "docker", "git")