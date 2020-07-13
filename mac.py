import subprocess
import optparse
import re
import os


def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface",
	                  help="Interface to change its MAC address")
	parser.add_option("-m", "--mac", dest="new_mac", help="new mac adress")
	(option, arguments) = parser.parse_args()
	if not option.interface:
		parser.error("Please specify an interface, use -h for more info")
	elif not option.new_mac:
		parser.error("Please specify a new mac, use -h for more info")
	return option


def change_mac(interface, new_mac):
	subprocess.call(['ifconfig', interface, 'down'])
	subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
	subprocess.call(['ifconfig', interface, 'up'])

options = get_arguments()

change_mac(options.interface, options.new_mac)
ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
# print(ifconfig_result)

mac_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
print(mac_search.group(0))

# os.system('cat /sys/class/net/eth0/address')
