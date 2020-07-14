# PIHOLE + PIVPN
Just follow the steps and all the things will be setup

## INSTALLATION GUIDE
> Step 1
- `bash Mitigation.sh`
> Step 2
- Executing above command  and choose 01 option.
- 01 for Installation of PI-HOLE (for your own DNS)
> Step 3
- whick asks for a static IP address.
- If a static IP is not set, use the following set of commands to set the static IP as we need this static IP in order to set Pi-Hole as a DNS server later on.
- A dynamic IP would be cumbersome because then we would have to change our DNS server IP every time Pi-Hole gets a new IP by the router’s DHCP server.
- We use nano to edit the DHCP client configuration file:
`sudo nano /etc/dhcpcd.conf`
- Scroll to the end of the file and change the following lines according to your network setup for a static IP.
- Example static IP configuration:
- `interface eth0`
- `static ip_address=192.168.2.2/24`
- `static ip6_address=fd51:42f8:caae:d92e::ff/64`
- `static routers=192.168.2.1`
- `static domain_name_servers=192.168.2.1`
adjust the hostname at the top of the configuration fileraspi-config to
- “pihole” manually as follows: Inform the DHCP server of our hostname for DDNS.
> Step 4 
- Here it is asking you which DNS server Pi-hole should use to resolve IPs/domains. Google is aadequeate choice.
> Step 5
- Pi-hole relies on lists with unwanted ad domains, we have to use some repositories from third parties that maintain these lists. By default, all repositories are activated or add any list manually after installation.
> Step 6
- For blocking unwanted ads regardless of the IP protocol version, we shall leave it to both protocols activated by default and continue the installation
> Step 7 
- The Gateway is usually the IP of your router.The IP address should be the static one you configured before for the Raspberry Pi.
- Simply read the caution message and continue installation.
> Step 8
- Now install the web admin interface asit allows usage of interactive Dashboard later on.
> Step 9 
- Install the web server as it allows admin page to be hosted locally on the machine for the purpose of using the Dashboard.
> Step 10
- Logging queries shall be set to “On” as it allows us to inspect the logsif something goes wrong.
> Step 11
- Use the default option because we want to see everything that Pi-Hole blocks inside the Dashboard.
> Step 12
- The screen indicates that the installation has started with preferences that are set above.
> Step 13
- This screen also contains the password that we need later on to log into the Dashboard.

We are now ready to go over to our freshly installed Pi-hole Dashboard.
You can access it inside your browser by typing “http://192.168.0.103/admin” or “http://pi.hole/admin”. Change the IP address according to your setup.

## INSTALLATION GUIDE for PI-VPN
> Step 1
- `bash Mitigation.sh`
> Step 2
- Executing above command  and choose 02 option.
- 02 for Installation of PI-VPN (for your own VPN)
> Step 3
- Then select yes to use your current address as your static address
> Step 4 
- confirm your Ip address and Gateway
> Step 5 
- follow installation to confirm Pi and UDP
> Step 6 
- enter your port and ip
> Step 7 
- Then select the encryption level you want(use 256-bit)
> Step 8
- Then select Use public DNS
> Step 9 
- Then enter the name of the public dns server and select yes.
> Step 10 
- Then select the DNS provider as Pihole or it will autodetect the pihole settings on your pi 
> Step 11 
- and lastly reboot your system.

### References
- i. “Network-wide ad blocking via your own Linux hardware” [Online]-
https://github.com/pi-hole/pi-hole
[Accessed on- 20/06/2020]
- ii. “Installing OpenVpn on Raspbian”[Online]-
https://www.ovpn.com/en/guides/raspberry-pi-raspbian
[Accessed on- 29/06/2020]

