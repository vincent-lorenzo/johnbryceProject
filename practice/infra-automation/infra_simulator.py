import logging
from jsonschema import validate, ValidationError
import subprocess
import json
from src.machine import Machine
import platform

# creating the provision log 

logging.basicConfig(
    filename='logs/provisioning.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# validate the data entered by user 

machine_validation = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 1},
        "os": {"type": "string", "enum": ["linux", "windows", "mac", "lin", "win"]},
        "cpu": {"type": "number", "minimum": 0.1},
        "ram": {"type": "number", "minimum": 0.1}
    },
    "required": ["name", "os", "cpu", "ram"]
}

# calling the bash script based on the user's platform 

def run_nginx_installer(machine_name, service_name):
    current_os = platform.system().lower()
    logging.info(f"Running service installation script for machine '{machine_name}' and service '{service_name}' on OS '{current_os}'")
    
    try:
        if current_os in ['linux', 'darwin']:
            logging.info("Using bash to run script")
            subprocess.run(
                ["bash", "scripts/nginx_installer.sh", machine_name, service_name],
                check=True
            )
        elif current_os == 'windows':
            logging.info("attempting to locate Git Bash using 'where' command")
            try:
                git_bash_path = subprocess.check_output(
                    ["where", "bash"],
                    universal_newlines=True
                ).splitlines()[0]
                logging.info(f"using Git Bash at '{git_bash_path}' to run script")
                subprocess.run(
                    [git_bash_path, "scripts/nginx_installer.sh", machine_name, service_name],
                    check=True
                )
            except subprocess.CalledProcessError:
                logging.error("Git Bash not found. Ensure Git is installed and 'bash' is in PATH.")
                print("Error: Git Bash not found. Please ensure Git is installed and added to PATH.")
                return
        else:
            logging.warning(f"Operating system not supported for bash script execution: {current_os}")
            return

        logging.info(f"Service installation script completed successfully for machine '{machine_name}'")
    except subprocess.CalledProcessError as e:
        logging.error(f"Bash script failed with return code {e.returncode}")
    except Exception as e:
        logging.error(f"Unexpected error running bash script: {e}")


# prompting the user to input machine creation details: 

def machine_creation_details(): 
    machines = []

    while True: 
        while True:
            name = input("enter machine name or enter 'done' to exit : ")
            if name.lower() == 'done':
                logging.info("user exited machine creation with 'done'.")
                return machines
            if name:
                break
            else:
                print("machine name can not be empty")
                logging.warning("user entered an empty machine name.")

        
        while True:
            os_input = input("enter your preferred operating system (linux / windows / mac): ").strip().lower()
            if os_input in ['linux', 'windows', 'mac' , 'win' , 'lin']:
                break
            else:
                print("Invalid os. please enter linux, windows, or mac.")
                logging.error(f"invalid os input: {os_input}")

        while True:
            try:
                cpu = float(input("Enter required cpu: "))
                if cpu <= 0:
                    raise ValueError("cpu must be a positive number.")
                break
            except ValueError as e:
                print("invalid input. please enter a positive number.")
                logging.error(f"invalid cpu input: {e}")

        while True:
            try:
                ram = float(input("enter your required ram in GB: "))
                if ram <= 0:
                    raise ValueError("ram must be a positive number.")
                break
            except ValueError as e:
                print("invalid ram. please enter a positive number.")
                logging.error(f"invalid ram input: {e}")

        machine_data = {
    "name": name,
    "os"  : os_input,
    "cpu" : cpu,
    "ram" : ram
}
        try:
            validate(instance=machine_data, schema=machine_validation)
            machine = Machine(**machine_data)
            machines.append(machine)
            logging.info(f"Added machine to list: {machine_data}")
        except ValidationError as e:
            print("Validation failed. Machine not added.")
            logging.error(f"Schema validation error: {e.message}")
        
        run_nginx_installer(name , "nginx")

        another_machine = input("would you like to create another machine? yes / no: ").strip().lower()
        if another_machine in ['no','n']:
            break

    return machines 

# running the script

if __name__ == "__main__":
    logging.info("machine creation started.")
    result = machine_creation_details()
    logging.info("final machine creation list:")
    for m in result:
        logging.info(m.to_dict())


# saving into a json file

instances_file = "configs/instances.json"

try:
    try:
        with open(instances_file, "r") as f:
            existing_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []

    all_data = existing_data + [machine.to_dict() for machine in result]

    with open(instances_file, "w") as f:
        json.dump(all_data, f, indent=4)
        logging.info(f"machine data saved to {instances_file}")

except Exception as e:
    logging.error(f"failed to save machine data: {e}")