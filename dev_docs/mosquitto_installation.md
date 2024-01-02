# Install Mosquitto on Remote System
Install Mosquitto on a remote Ubuntu system 
```bash
sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
sudo apt-get update
sudo apt-get install mosquitto
sudo apt-get install mosquitto-clients
```
# Allow remote access to broker 
1. Create a password file at `/etc/mosquitto/` direcoty named `pw_file.conf`.
    ```bash
    sudo nano /etc/mosquitto/pw_file.conf
    ```
2. Define lister port (1883) and allow unauthorised access.
    ```bash
    listener 1883
    allow_anonymous true
    ```
3. Restart Mosquitto service 
    ```bash 
    sudo systemctl stop mosquitto
    sudo systemctl start mosquitto
    ```
        
# Start broker with password file
start broker in verbose mode (`-v`) with path to config file (`-c`)
```bash
mosquitto -v -c /etc/mosquitto/pw_file.conf
```
should show the follwoing output:
```bash
1704211444: mosquitto version 2.0.11 starting
1704211444: Config loaded from /etc/mosquitto/pw_file.conf.
1704211444: Opening ipv4 listen socket on port 1883.
1704211444: Opening ipv6 listen socket on port 1883.
1704211444: mosquitto version 2.0.11 running
```