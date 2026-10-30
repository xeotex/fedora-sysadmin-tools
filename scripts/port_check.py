import socket
import argparse
import sys

def check_port(host: str, port: int, timeout: float = 2.0) -> bool:
    """Prüft, ob ein Port auf einem Host erreichbar ist."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((host, port))
            return result == 0
    except socket.gaierror:
        print(f"Fehler: Hostname '{host}' konnte nicht aufgelöst werden.")
        sys.exit(1)
    except socket.error as e:
        print(f"Netzwerkfehler: {e}")
        return False

def main() -> None:
    parser = argparse.ArgumentParser(description="Ein simpler TCP Port Scanner.")
    parser.add_argument("host", help="Die IP-Adresse oder der Hostname")
    parser.add_argument("port", type=int, help="Der zu prüfende Port")
    
    args = parser.parse_args()
    
    if check_port(args.host, args.port):
        print(f"[+] Port {args.port} auf {args.host} ist OFFEN.")
        sys.exit(0)
    else:
        print(f"[-] Port {args.port} auf {args.host} ist GESCHLOSSEN oder gefiltert.")
        sys.exit(1)

if __name__ == "__main__":
    main()
