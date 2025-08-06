# Machine Provisioning Tool

A Python-based tool for creating and provisioning virtual machines with automated service installation. This tool provides an interactive command-line interface for defining machine specifications and automatically installs services like Nginx on the provisioned machines.

## Features

- **Interactive Machine Creation**: User-friendly CLI for defining machine specifications
- **Cross-Platform Support**: Works on Linux, macOS, and Windows (with Git Bash)
- **Input Validation**: JSON schema validation for machine configurations
- **Automated Service Installation**: Automatic Nginx installation via shell scripts
- **Comprehensive Logging**: Detailed logging of all provisioning activities
- **Data Persistence**: Machine configurations saved to JSON files
- **Multi-Machine Support**: Create multiple machines in a single session

## Project Structure

```
machine-provisioning/
├── src/
│   └── machine.py          # Machine class definition
├── scripts/
│   └── nginx_installer.sh  # Service installation script
├── configs/
│   └── instances.json      # Machine configurations storage
├── logs/
│   └── provisioning.log    # Application logs
├── main.py                 # Main application entry point
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Requirements

- Python 3.7+
- Bash (Linux/macOS) or Git Bash (Windows)
- Required Python packages (see `requirements.txt`)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd machine-provisioning
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create required directories:**
   ```bash
   mkdir -p src scripts configs logs
   ```

## Dependencies

The tool requires the following Python packages:

- `jsonschema` - For input validation
- Standard library modules: `logging`, `subprocess`, `json`, `platform`

Create a `requirements.txt` file with:
```
jsonschema>=4.0.0
```

## Usage

### Running the Tool

Execute the main script to start the interactive machine creation process:

```bash
python main.py
```

### Interactive Process

1. **Machine Name**: Enter a unique name for your machine
2. **Operating System**: Choose from:
   - `linux` or `lin`
   - `windows` or `win`
   - `mac`
3. **CPU Requirements**: Specify CPU cores (minimum 0.1)
4. **RAM Requirements**: Specify RAM in GB (minimum 0.1)

### Example Session

```
Enter machine name or enter 'done' to exit: web-server-01
Enter your preferred operating system (linux / windows / mac): linux
Enter required CPU: 2.0
Enter your required RAM in GB: 4.0
Would you like to create another machine? yes / no: no
```

## Machine Configuration Schema

Each machine must conform to the following JSON schema:

```json
{
  "type": "object",
  "properties": {
    "name": {"type": "string", "minLength": 1},
    "os": {"type": "string", "enum": ["linux", "windows", "mac", "lin", "win"]},
    "cpu": {"type": "number", "minimum": 0.1},
    "ram": {"type": "number", "minimum": 0.1}
  },
  "required": ["name", "os", "cpu", "ram"]
}
```

## Service Installation

The tool automatically installs Nginx on each created machine using platform-specific scripts:

- **Linux/macOS**: Uses native bash
- **Windows**: Uses Git Bash (must be installed and in PATH)

### Nginx Installer Script

Create `scripts/nginx_installer.sh`:

```bash
#!/bin/bash
MACHINE_NAME=$1
SERVICE_NAME=$2

echo "Installing $SERVICE_NAME on machine: $MACHINE_NAME"
# Add your nginx installation commands here
# Example for Ubuntu/Debian:
# sudo apt update
# sudo apt install -y nginx
# sudo systemctl start nginx
# sudo systemctl enable nginx
```

## Machine Class

Create `src/machine.py`:

```python
class Machine:
    def __init__(self, name, os, cpu, ram):
        self.name = name
        self.os = os
        self.cpu = cpu
        self.ram = ram
    
    def to_dict(self):
        return {
            "name": self.name,
            "os": self.os,
            "cpu": self.cpu,
            "ram": self.ram
        }
    
    def __repr__(self):
        return f"Machine(name='{self.name}', os='{self.os}', cpu={self.cpu}, ram={self.ram})"
```

## Logging

All activities are logged to `logs/provisioning.log` with timestamps and log levels:

- **INFO**: Normal operations and successful completions
- **WARNING**: Non-critical issues
- **ERROR**: Validation failures and script execution errors

## Output Files

- **Machine Configurations**: `configs/instances.json` - Contains all created machine specifications
- **Logs**: `logs/provisioning.log` - Detailed operation logs

## Platform Support

### Linux/macOS
- Native bash support
- Direct script execution

### Windows
- Requires Git Bash
- Automatic detection of Git Bash installation
- Falls back gracefully if Git Bash is not found

## Error Handling

The tool includes comprehensive error handling for:

- Invalid input validation
- Missing dependencies
- Script execution failures
- File I/O operations
- Platform compatibility issues

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Troubleshooting

### Common Issues

**Git Bash not found on Windows:**
- Install Git for Windows
- Ensure Git is added to system PATH
- Restart your terminal

**Permission denied on script execution:**
```bash
chmod +x scripts/nginx_installer.sh
```

**Missing directories:**
```bash
mkdir -p src scripts configs logs
```

## Support

For issues, questions, or contributions, please open an issue in the repository or contact the maintainer.