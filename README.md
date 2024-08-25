# Fortigate Multi-CLI Script Executor

This script allows you to execute a CLI script on multiple Fortigate firewall devices simultaneously. It is designed to simplify the management and configuration of multiple Fortigate devices by automating the script upload process.

## Features

- Execute CLI scripts on multiple Fortigate devices at once.
- Utilizes multi-threading to perform uploads concurrently, significantly reducing execution time.
- Displays a detailed table of results for each device, showing success or error messages.
- Easy to extend and customize with additional features or device configurations.

## Prerequisites

- Python 3.x
- The following Python libraries (install using `pip install -r requirements.txt`):
  - `requests`
  - `concurrent.futures` (part of Python standard library)
  - `rich`
  - `urllib3`
  - `argparse` (part of Python standard library)

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/LeandroR0J0/FTG-Multi-CLI-exec.git
    ```

2. Navigate to the project directory:

    ```bash
    cd FTG-Multi-CLI-exec
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use this script, you need to have a CLI script file ready to be uploaded to your Fortigate devices. Update the `fortigate_devices` list within the script to include the IP addresses and API keys of your Fortigate devices.

Run the script using the following command:

```bash
python FTG-Multi-CLI-exec.py CLI_Script_to_Upload.txt
```

This will upload the `CLI_Script_to_Upload.txt` content to all Fortigate devices listed in the fortigate_devices array and display the result of each upload in a table.

## Disclaimer

This script was developed by Security Analyst Leandro Rojo on 24/08/2024, outside of professional working hours. Feel free to modify or add features as needed.

DISCLAIMER: The author is not responsible for any issues caused by using this script. Use it at your own risk.

## Contact

For questions or feedback, you can contact me on Linkedin

## License

This project is licensed under the MIT License - see the LICENSE file for details.
