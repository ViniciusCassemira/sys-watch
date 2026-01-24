# Unit files study

This is a study project about _Unit files_ in _Systemd_. The main purpose is understand how the services and process works with systemd. In this case, i created two unit files: 

`.service`: This will run a simple Python script, which writes the current date to a.txt
`.timer`: Configured to run the service mentioned above every x seconds

## How to use

1. clone and access that repository on your machine
```bash
    git clone https://github.com/ViniciusCassemira/sys-watch.git
    cd sys-watch
```

2. Open the file `app.py` and modify: `<your-project-path>` to your current project path

3. Open the file `study.service` and modify: `<your-user>` to your user, and `<your-project-path>` to your current project path

4. Run the config script
```
    chmod +x ./setup-config.sh
    ./setup-config.sh
```

it will:
- Clone `.service` and `.timer` into `/etc/systemd/system/`
- Reload systemd to recognize new service and timer

To run the service, just type in the terminal: `sudo systemctl start study.timer`