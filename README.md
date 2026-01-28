# Sys watch

This is a study project about _Unit files_ in _Systemd_. The main purpose is understand how the services and process works with systemd. In this case, i created two unit files:

`.service`: Esse service irá rodar um script python, que irá monitorar os recursos da máquina hospedeira(cpu, memoria, processos) e armazenar em arquivos de texto simples
`.timer`: Configured to run the service mentioned above every x seconds

## Requirements
- Python >= 3.8
- pip (Python package manager)
- systemd (Linux systems only)

## Dependencies
The project uses the following Python packages (listed in requirements.txt):

- psutil - for system and process monitoring
- python-dotenv - for environment variable management

## How to use
---
1. clone and access that repository on your machine
```bash
    git clone https://github.com/ViniciusCassemira/sys-watch.git
    cd sys-watch
```
---
2. Rename the `.env.example` file to `.env` and change the following variables as needed:
- `USER` = User who will run the process
- `WORKING_DIRECTORY` = Cloned Project Path on Your Computer
- `ON_UNIT_ACTIVE_SEC` = Time interval between one execution and another
- `ON_BOOT_SEC` = How long should the script wait to start after the system boots
- `EXEC_START` = Command to execute (usually the path to your Python interpreter and script)
---
3. Run this command inside project folder:
```python
python ./functions/create_unit_files.py
```
This python file will create the `sys_watch.service` and `sys_watch.timer` files based on the values you entered in the `.env` file, so configure these values carefully so that everything works out

---
4. Run the config script
```
    ./setup-config.sh
```

it will:
- Clone `.service` and `.timer` files into `/etc/systemd/system/`
- Reload systemd to recognize new service and timer
---
To run the service, just type in the terminal: `sudo systemctl start sys_watch.timer`

## Another alternative
If you want to run the project locally only to collect metrics from your machine (without using systemd unit files), create and activate a virtual environment, install the dependencies from `requirements.txt`, and run:
```python
python app.py
```