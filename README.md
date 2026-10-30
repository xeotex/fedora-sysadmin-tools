# Fedora System Automation & Tooling

**Tech-Stack:** Fedora (RHEL), Python 3.12+

Dieses Repository enthält Python-Skripte für die Automatisierung von Wartungsaufgaben und Netzwerkdiagnostik. Der Fokus liegt auf der Nutzung nativer Systemwerkzeuge (`dnf`) und robuster Fehlerbehandlung.

## Enthaltene Skripte

* **`scripts/system_maintenance.py`**: Automatisierter Workflow für System-Updates, Paketbereinigung und Cache-Management. Implementiert mit modernem Logging, `Pathlib` und Type-Hinting.
* **`scripts/port_check.py`**: CLI-Tool zur TCP-Port-Verifizierung mittels Sockets zur Überprüfung von Netzwerkdiensten (z. B. Datenbanken, Keycloak).

*Status: Auf der Suche nach einem IHK-Abschlussprojekt (Anwendungsentwicklung / Python).*
