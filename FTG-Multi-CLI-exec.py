# Script developed by Security Analyst Leandro Rojo at 24/08/2024.
# DISCLAIMER this script has been coded and finished out of my professional working hours.
# Feel free to modify or add many things as you want.
# You can contact me in https://www.linkedin.com/in/rojoleandro/

import requests
import concurrent.futures
from rich.console import Console
from rich.table import Table
import urllib3
import argparse
import os

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Initial configurationl
fortigate_devices = [
    {"ip": "192.168.1.1", "api_key": "8w40hn4537kdnQmytm3f1fim1NHzHg"},
    {"ip": "192.168.1.2", "api_key": "8w40hn4537kdnQmytm3f1fim1NHzHg"},
    # You can add as much as Firewalls as you want line by line. (API key and IP are ficticial ones, remember to replace it.)
]

console = Console()

def upload_config_script(device, script_path):
    url = f"https://{device['ip']}/api/v2/monitor/system/config-script/upload"
    headers = {
        "Authorization": f"Bearer {device['api_key']}"
    }
    files = {
        'script': ('config_script.txt', open(script_path, 'rb'))
    }

    try:
        response = requests.post(url, headers=headers, files=files, verify=False, timeout=10)
        response.raise_for_status()
        return (device['ip'], "Success", response.json())
    except requests.exceptions.HTTPError as http_err:
        return (device['ip'], "HTTP Error", f"{http_err} - Response: {http_err.response.text}")
    except requests.exceptions.RequestException as req_err:
        return (device['ip'], "Request Error", str(req_err))
    except Exception as err:
        return (device['ip'], "Error", str(err))
    finally:
        files['script'][1].close()

def main(script_path):
    if not os.path.exists(script_path):
        console.print(f"[bold red]El archivo {script_path} no existe.[/bold red]")
        return

    # Execute different threads in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        # upload scriptfile to each device
        upload_futures = {executor.submit(upload_config_script, device, script_path): device for device in fortigate_devices}
        
        # save the data of the upload
        upload_results = []

        # Waits for all uploads to be completed
        for future in concurrent.futures.as_completed(upload_futures):
            device = upload_futures[future]
            try:
                result = future.result()
                upload_results.append(result)
            except Exception as exc:
                upload_results.append((device['ip'], "Error", str(exc)))

    # Makes a table to show all uploads results
    upload_table = Table(title="Resultados de la subida del script de configuraciÃ³n en Fortigate")

    upload_table.add_column("Dispositivo IP", justify="right", style="cyan", no_wrap=True)
    upload_table.add_column("Estado", style="magenta")
    upload_table.add_column("Respuesta", style="green")

    for result in upload_results:
        ip, status, response = result
        upload_table.add_row(ip, status, str(response))

    console.print(upload_table)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload a CLI script to all Fortigate devices registered.)
    parser.add_argument("script_path", help="Ruote to Fortigate CLI script to execute within the FWs")
    args = parser.parse_args()
    main(args.script_path)

