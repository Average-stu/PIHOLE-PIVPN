# MITM Attack

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger) [![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

Man-in-the-middle (MITM) attacks occur when the attacker manages to position themselves between the legitimate parties to a conversation. The attacker spoofs the opposite legitimate party so that all parties believe they are actually talking to the expected other, legitimate parties. In layman’s terms, MITM attack can be described as eavesdropping.

# Its Mitigation
One safe approach from this is to use a VPN client as it encrypts Internet traffic via AES. With this encryption, data is encrypted and decrypted again. For an internet criminal it is very difficult to hack the encryption because it consists of a very long number and it takes too much time to try all combinations of numbers. When user is equipped with their own bundle which helps them keep in check of their live logs, blacklisting the suspected domains, wildcard clocks domains – blocking of a site and its sub domains and along with that provides the VPN service encrypts and transmits data while it travels from one place to another on the internet.

## Installing Dependencies
`pip install -r requirements.txt`
* Flip your machine into forwarding mode (as root):
`sudo sysctl -w net.ipv4.ip_forward=1`

## Working

1. CHANGING MAC ADDRESS
`sudo python mac.py -i eth0 -m 12:22:33:44:55:66`
2. Scanning IPs in Network
`sudo python scanner2.py -t 192.168.43.1/24`
3. Capturing traffic
`sudo python arp.py -t 192.168.43.73 -d 192.168.43.1`
4. Sniffing HTTP Traffic
`sudo python psniffer.py -i eth0`
5. Capturing HTTPs Taffic
 - Using Mitmproxy
`iptables -t nat -A PREROUTING -p TCP - -destination-port 443 -j REDIRECT --to-port 8080`
`sudo mitmproxy -T --host -e`
 - Using Sslstrip
 `iptables -t nat -A PREROUTING -p TCP - -destination-port 443 -j REDIRECT --to-port 8080`
`sslstrip -l 8080`
- or by script 
`sudo python https.py`

### Tech
* MItmproxy - Mitmproxy is a swiss-army knife for debugging, testing, privacy measurements, and penetration testing. It can be used to intercept, inspect, modify and replay web traffic such as HTTP/1, HTTP/2, WebSockets, or any other SSL/TLS- protected protocols. One can prettify and decode a variety of message types ranging from HTML to Protobuf, intercept specific messages on-the-fly, modify them before they reach their destination, and replay them to a client or server later on. For more info refer this- https://docs.mitmproxy.org/stable/concepts-howmitmproxyworks/
* sslstrip - Sslstrip is a tool that transparently hijacks HTTP traffic on a network, watches for HTTPS links and redirects, and then map those links into look-alike HTTP links or homograph-similar HTTPS links. It also supports modes for supplying a favicon which looks like a lock icon, selective logging, and session denial. For more info refer this- https://pypi.org/project/sslstrip/


## COUNTER MEASURES
These attacks are highly complicated in nature. One needs to have some serious skills and must be aided by right tools in order to prevent such attacks.

### Our Solution
PI-Hole - The Pi-hole is a DNS sinkhole that protects devices from unwanted content, without installing any client- side software. Pi-Hole is a network wide ad-blocking tool, which sets up a Domain Name System (DNS) server and handles all DNS requests generated from our home network. Pi-Hole will deny all requests from ad- servers and thereby prevent the loading of advertisements.  Pi-Hole does not modify the website or application’s request to download any third-party scripts. The advantage over other ad-blocking alternatives is, that Pi-Hole blocks ads on network level, which also allows for ad-blocking on non traditional devices such as Smartphones or TVs. Pi-Hole works using filter lists. These lists are publicly available and crowd-sourced. Users are able to add additional filter list or block single ad- domains. They prevent advertisement from actually being loaded by denying the request made from these ad-servers. VPN Blockers do also work with filter lists. Unlike Pi- Hole, it is not possible for the end-user to add additional filter lists, since the configuration is made by the VPN operator. VPN - The OpenVPN Access Server consists of a set of installation and configuration tools which allow for simple and rapid deployment of VPN remote access solutions using the OpenVPN open source project. The Access Server software builds upon the usability and popularity of OpenVPN, while easing VPN configuration and deployment by providing the following features:
- Simplified server configuration
- Support for external user authentication database
- Easy intuitive Web-Based client access
- Compatibility with a large base of OpenVPN
clients PI VPN is a lightweight OpenVPN server designed to run on Raspberry Pi 2 or 3. It gives you access to our home network through a secure connection over the internet. By plugging a Raspberry Pi into your router, it acts somewhat like a bridge between mobile devices and your network.

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



## Conclusion 
Blocking of a Man In the Middle attack needs several practices to be used. It is the acknowledging the prevention tactics and the mitigation application that will help one build up strong enough against these attacks.
From user side :- Avoiding the use of public WiFi as they stand high chance being intercepted by the malicious minds. Paying attention to identify the websites that can be possibly a phishing page and insecure. Logging out of a secure application so that the credentials aren’t available anymore for anyone’s
access.
From a developer side :- The web operators should include TLS and HTTPS protocols for secure connections and encryption of data in transfer. This activity helps in blocking the decryption of sensitive data. Also, it is widely accepted method to make use of SSL/TLS for securing pages so that the in between hijacking of session cookies does not happen. One cannot compromise with their confidentiality and keep risk of losing the information integrity and cyber threats loom over the victims so the best start might be to acknowledge its adversity and to act with precautions. It is important to understand the Man In the Middle attack so thus the frame-work is designed that helped us to cover its major concerns. Our proposed solution acts for the user side making sure of the fact that they would not have to rely on a 3 rd party server, to use the VPN service, with the risk of their logs and activities being monitored.


### Todos

- Integrate all into a Package 

License
----
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

MIT

### Contributor
- [Mayank kumar](https://github.com/Mk-ism)
- [Meenakshi Kharel](https://github.com/MEraKi4)
- [Aman Kumar](https://github.com/Average-stu)
- [Arathi S](https://github.com/Arathi-S124)
- [Paritosh Kumar Yadav](https://github.com)
- [Kinchit Saxena](https://github.com)
- [Mayank Chahal](https://github.com)
### References
- i. “Network-wide ad blocking via your own Linux hardware” [Online]-
https://github.com/pi-hole/pi-hole
[Accessed on- 20/06/2020]
- ii. “VPN can prevent a MITM attack” [Online]-
https://www.professionalsecurity.co.uk/news/press-releases/vpn-can-prevent-a-man-in-the-middle-attack/
[Accessed on- 20/06/2020]
- iii. “Setting up an OpenVPN server with DD-WRT and Viscosity” [Online]-
https://www.sparklabs.com/support/kb/article/setting-up-an-openvpn-server-with-dd-wrt-and-viscosity/
[Accessed on- 22/06/2020]
- iv. “How to access a fake access point” [Online]-
https://zsecurity.org/how-to-start-a-fake-access-point-fake-wifi/
[Accessed on-28/06/2020]
- v. “Installing OpenVpn on Raspbian”[Online]-
https://www.ovpn.com/en/guides/raspberry-pi-raspbian
[Accessed on- 29/06/2020]
- vi. “How to setup openvpn on Debian” [Online] -
https://wiki.debian.org/OpenVPN
https://averagelinuxuser.com/linux-vpn-server/
[Accessed on- 01/07/2020]
- vii. Documentation [Online]-
- http://site.iugaza.edu.ps/nour/files/lab4-MITM1.pdf
- https://www.thesslstore.com/blog/man-in-the-middle-attack-2/
- https://www.thesslstore.com/blog/man-in-the-middle-attack/
- https://www.adtran.com/images/tech_team/presentations/030618/Protect.pdf
- https://files.ifi.uzh.ch/CSG/staff/franco/extern/theses/BA-Lawand-Muhamad.pdf
- https://openvpn.net/images/pdf/OpenVPN_Access_Server_Sysadmin_Guide_Rev.pdf
- https://www.comparitech.com/blog/vpn-privacy/raspberry-pi-vpn/
- sslstrip - https://pypi.org/project/sslstrip/
- mitmproxy - https://docs.mitmproxy.org/stable/concepts-howmitmproxyworks/



