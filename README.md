# DS SaveGameManager

In order to use DS SaveGameManager, do the following:

# Step 1: Set up a WEP Access Point

Either connect to one, or set it up on the PC. Keep it
as WEP, because the DS Lite does not allow you to connect to
WPA/WPA2 or newer WiFi hotspots.

I use an Android Phone for this, and that phone is
disposable/safe.

Note down the IP of the computer that is going to act
as the FTP server. It should usually be in the
`192.168.43.0/24` subnet. Android has a few FTP servers
already, and you could completely do this on the phone.

# Step 2: Connect the DS to this Network

Use any game with internet connection (Pokemon) to set
up the `Nintento WFC`. Although it won't work a 100% because
the services are down, the TCP connectivity via WiFi will
happen. You should notice a device called `NintendoDS`
being able to connect to the hotspot.

# Step 3: Set up the Dumper on the Flash Cart

This section assumes using the *DSTWO*.

Open the `SGM` folder. Ensure the `SaveGame_Manager.ini`
file resides in the same directoy.

Edit the line which reads and set it to the IP of the FTP server:

```
ftp_ip = 192.168.43.1
```

Set Username/Password to `guest` or as appropriate.

Move the `SGM` folder to `_DSTWOPLUG` folder to the SD Card
used on the DSTWO.

# Step 3: Run a FTP Server

If you are already running a server on Android, skip this step.
Here is how you run the FTP Server on a PC.

```bash
cd SGM-FTP
pip install -r requirements.txt
python ds_ftp.py
```

# Step 4: Run the Dumper from the DS.

Run the dumper and enjoy SaveGame backups.