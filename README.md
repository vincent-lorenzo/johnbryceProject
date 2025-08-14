# Python Learning & DevOps Practice Repository

This repository contains Python learning exercises and DevOps automation projects, designed for hands-on practice with Python fundamentals and infrastructure automation concepts.

## Repository Structure

```
.
├── practice/                    # Python fundamentals and practice exercises
│   ├── infra-automation/       # Machine provisioning automation project
│   ├── basics.py              # Basic Python syntax
│   ├── variables.py           # Variable handling exercises
│   ├── loop_control.py        # Loop control structures
│   ├── functions_*.py         # Function definition and usage
│   ├── servers_running.py     # Server status management example
│   ├── orcatech-lab1.py      # Personal profile lab exercise
│   └── ...                   # Additional practice files
├── rolling_project/           # Project iterations and versions
│   └── infra-automation/     # Infrastructure automation project
└── README.md                 # This file
```

## Projects Overview

### 🐍 Python Fundamentals Practice

The `practice/` directory contains various Python exercises covering:

- **Basic Syntax**: Variables, data types, and basic operations
- **Control Flow**: Conditionals, loops (for, while), and control structures  
- **Functions**: Function definitions, parameters, and return values
- **Data Structures**: Lists, dictionaries, and complex data handling
- **Modules**: Import statements and module usage
- **File Handling**: Reading and writing files
- **Server Management**: Basic server status checking and management

#### Key Practice Files:

- `basics.py` - Python syntax fundamentals
- `variables.py` - Variable declaration and manipulation
- `loop_control.py`, `loop_control_2.py` - Loop structures and control
- `functions_1.py`, `functions_2.py` - Function implementation
- `servers_running.py` - Server status management simulation
- `orcatech-lab1.py` - Personal profile data structure exercise

### 🔧 Infrastructure Automation Project

Located in `practice/infra-automation/` and `rolling_project/infra-automation/`

A Python-based machine provisioning tool that provides:

- **Interactive Machine Creation**: User-friendly CLI for defining VM specifications
- **Cross-Platform Support**: Works on Linux, Windows, and macOS
- **Input Validation**: JSON schema validation for configurations
- **Automated Service Installation**: Automatic nginx installation
- **Persistent Storage**: Machine configurations saved to JSON
- **Comprehensive Logging**: Detailed operation logging

#### Project Features:
- Virtual machine configuration management
- Automated service deployment (nginx)
- JSON-based configuration storage
- Cross-platform bash script execution
- Input validation and error handling

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Git (for cloning the repository)
- Bash shell (Linux/macOS) or Git Bash (Windows)

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **For Infrastructure Automation Project**:
   ```bash
   cd practice/infra-automation
   pip install -r requirments.txt
   ```

### Running the Exercises

#### Python Practice Files:
```bash
cd practice
python3 <filename>.py
```

#### Infrastructure Automation:
```bash
cd practice/infra-automation
python3 infra_simulator.py
```

## Learning Path

### Beginner Level:
1. Start with `basics.py` for Python syntax
2. Practice variables with `variables.py`
3. Learn control flow with `condition.py` and `if.py`
4. Master loops with `for.py`, `while.py`, and loop control files

### Intermediate Level:
1. Explore functions with `functions_1.py` and `functions_2.py`
2. Work with data structures in `types_lab01.py`
3. Practice with complex scenarios in `servers_running.py`
4. Learn module usage with `modules_lab01.py`

### Advanced Level:
1. Dive into the infrastructure automation project
2. Understand JSON schema validation
3. Learn cross-platform scripting
4. Practice logging and error handling

## Project Structure Details

### Infrastructure Automation Components:
- `infra_simulator.py` - Main application entry point
- `src/machine.py` - Machine class definition
- `scripts/nginx_installer.sh` - Service installation scripts
- `configs/instances.json` - Machine configuration storage
- `logs/provisioning.log` - Application logs

## Contributing

This is a learning repository. Feel free to:
- Add new practice exercises
- Improve existing code examples
- Enhance the infrastructure automation project
- Add documentation and comments

## Skills Developed

Through this repository, you'll practice:
- **Python Programming**: Syntax, data structures, functions, modules
- **DevOps Concepts**: Infrastructure as code, automation, configuration management
- **System Administration**: Server management, service installation, logging
- **Software Engineering**: Code organization, error handling, validation
- **Cross-Platform Development**: Writing code that works across different operating systems

## License

This project is for educational purposes. Feel free to use and modify for learning.

---

**Happy Learning! 🚀**