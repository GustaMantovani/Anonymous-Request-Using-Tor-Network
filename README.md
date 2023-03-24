This repository contains a python script that allows you to send anonymous requests through the Tor network.


#What it Does

The script starts by creating a session with the requests library and setting the proxy to a local Tor instance. Then, the user is prompted to input a target URL. The script will then make a request to the target URL through the Tor network and print the response. The script will also print the user's real IP address and the IP address obtained through the Tor network. The script will run indefinitely until the user stops it.


#How it Connects to the Tor Network

The script connects to the Tor network by setting the http and https proxies in the requests session to socks5h://localhost:9050. This means that all requests made through the session will go through the Tor network. The default Tor SocksPort is 9050, so if you have a local Tor instance running on the same machine as the script, it will connect to the Tor network through this SocksPort.


#Usage

To run the script, you need to have a local Tor instance running on the same machine. You can download Tor from torproject.org. Once you have a local Tor instance running, simply run the script and input the target URL when prompted. The script will print the response and the real and Tor IP addresses.


#Installation

Before you can run the script, you need to install the following components:
1. Tor Network: You can download the Tor software from torproject.org. Once you have installed the software, make sure to start the local Tor instance.
2. Obfs4proxy: Obfs4proxy is a tool used to scramble the data sent through the Tor network. You can find more information on how to install obfs4proxy on torproject.org.
3. Requests Library: The script uses the requests library to make HTTP requests. You can install the library by running 'pip install requests'.
4. Socks Library: The script uses the Socks library to connect to the Tor network. You can install the Socks library by running 'pip install PySocks'.

Additionally, here is a tutorial on how to install Tor and Obfs4proxy: https://community.torproject.org/relay/setup/bridge/. The torrc configuration file is also included in this GitHub repository and should be saved in '/etc/tor/'.

To work around systemd hardening, you will also need to set 'NoNewPrivileges=no' in '/usr/lib/systemd/system/tor.service' and then run 'systemctl daemon-reload'. 

Once you have installed all these components, you should be able to run the script and make anonymous requests through the Tor network.

