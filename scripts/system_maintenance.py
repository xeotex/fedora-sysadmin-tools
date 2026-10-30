import subprocess
import logging
import sys
from datetime import datetime
from pathlib import Path

#Setup Logging
log_dir = Path.home() / "logs"
log_dir.mkdir(exist_ok=True)
timestamp = datetime.now().strftime("%Y-%m-%d")
log_file = log_dir / f"maintenance_{timestamp}.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)

def run_command(cmd: list[str], description: str) -> None:
    logging.info(f"Starte: {description}")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        logging.info(f"Erfolgreich: {description}")
        logging.debug(result.stdout)
    except subprocess.CalledProcessError as e:
        logging.error(f"Fehler bei {description}:\n{e.stderr}")

def main() -> None:
    logging.info("--- Starte Fedora System Maintenance ---")
    
    #1.System update
    run_command(["sudo", "dnf", "upgrade", "-y"], "System Update (dnf upgrade)")
    
    #2.Remove unused packages
    run_command(["sudo", "dnf", "autoremove", "-y"], "Entfernen ungenutzter Pakete")
    
    #3.Clear cache
    run_command(["sudo", "dnf", "clean", "all"], "Paket-Cache bereinigen")
    
    logging.info(f"--- Maintenance abgeschlossen. Log unter: {log_file} ---")

if __name__ == "__main__":
    main()
