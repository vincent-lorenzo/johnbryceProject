# Machine Provisioning Tool

A Python-based tool for creating and managing virtual machine configurations with automated service installation. This tool provides an interactive interface for defining machine specifications and automatically installs nginx on each created machine.

## Features

- **Interactive Machine Creation**: User-friendly prompts for defining machine specifications
- **Cross-Platform Support**: Works on Linux, Windows, and macOS
- **Input Validation**: JSON schema validation for machine configurations
- **Automated Service Installation**: Automatic nginx installation via bash scripts
- **Persistent Storage**: Machine configurations saved to JSON files
- **Comprehensive Logging**: Detailed logging of all operations

## Project Structure

```
.
├── README.md
├── main.py                    # Main application entry point
├── src/
│   └── machine.py            # Machine class definition
├── scripts/
│   └── nginx_installer.sh    # Nginx installation script
├── configs/
│   └── instances.json        # Stored machine configurations
└── logs/
    └── provisioning.log      # Application logs
```

## Requirements

### Python Dependencies

```
jsonschema
```

### System Requirements

- Python 3.6+
- Bash (Linux/macOS) or Git Bash (Windows)
- Internet connection for package installation

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd machine-provisioning-tool
   ```

2. **Install Python dependencies**:
   ```bash
   pip install jsonschema
   ```

3. **Create required directories**:
   ```bash
   mkdir -p src scripts configs logs
   ```

4. **Set up the nginx installation script** (create `scripts/nginx_installer.sh`):
   ```bash
   #!/bin/bash
   # Your nginx installation script here
   ```

5. **Make the script executable**:
   ```bash
   chmod +x scripts/nginx_installer.sh
   ```

## Usage

### Running the Application

```bash
python main.py
```

### Interactive Machine Creation

The application will prompt you for the following information for each machine:

1. **Machine Name**: A unique identifier for your machine
2. **Operating System**: Choose from:
   - `linux` or `lin`
   - `windows` or `win`
   - `mac`
3. **CPU Requirements**: Number of CPU cores (positive decimal)
4. **RAM Requirements**: Amount of RAM in GB (positive decimal)

### Example Session

```
enter machine name or enter 'done' to exit : web-server-01
enter your preferred operating system (linux / windows / mac): linux
Enter required cpu: 2.5
enter your required ram in GB: 8
would you like to create another machine? yes / no: no
```

## Configuration

### Machine Schema

The application validates machine configurations against the following JSON schema:

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

### Output Files

- **Machine Configurations**: Saved to `configs/instances.json`
- **Logs**: Application logs stored in `logs/provisioning.log`

## Logging

The application provides comprehensive logging with the following levels:

- **INFO**: General application flow and successful operations
- **WARNING**: Non-critical issues that don't prevent execution
- **ERROR**: Errors that may affect functionality

Log format: `%(asctime)s - %(levelname)s - %(message)s`

## Cross-Platform Compatibility

### Linux/macOS
- Uses system bash directly
- Executes scripts with `bash` command

### Windows
- Automatically detects Git Bash installation
- Falls back to system bash if Git Bash is not found
- Requires Git for Windows to be installed

## Error Handling

The application includes robust error handling for:

- Invalid user input
- Schema validation failures
- Script execution errors
- File I/O operations
- Cross-platform compatibility issues

## API Reference

### Main Functions

#### `machine_creation_details()`
Interactive function that collects machine specifications from user input.

**Returns**: List of Machine objects

#### `run_nginx_installer(machine_name, service_name)`
Executes the nginx installation script for a given machine.

**Parameters**:
- `machine_name` (str): Name of the target machine
- `service_name` (str): Name of the service to install

## Development

### Adding New Services

To add support for additional services:

1. Create installation scripts in the `scripts/` directory
2. Modify the service installation logic in the main application
3. Update the validation schema if needed

### Extending Machine Properties

To add new machine properties:

1. Update the `machine_validation` schema
2. Modify the input collection logic
3. Update the Machine class in `src/machine.py`

## Troubleshooting

### Common Issues

1. **"Git Bash not found" on Windows**
   - Install Git for Windows
   - Ensure `bash` is in your system PATH

2. **Permission denied for scripts**
   - Make scripts executable: `chmod +x scripts/*.sh`

3. **Module not found errors**
   - Install required dependencies: `pip install jsonschema`
   - Ensure the `src/` directory contains the `machine.py` file

4. **JSON file corruption**
   - The application will create a new `instances.json` if the existing one is corrupted

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

[Add your license information here]

## Support

For issues and questions, please [create an issue](link-to-issues) in the repository.