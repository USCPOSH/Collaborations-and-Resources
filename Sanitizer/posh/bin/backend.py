import yaml
import os
from os import system, name


def clear():
	if name == 'nt':
		os.system('cls')
	else:
		os.system('clear')


class SanitizerUI:


	def __init__(self, devicelist):
		self.devices = devicelist

	def find(self, name):
		for device in self.devices["devices"]:
			if(device["name"] == name):
				return device
		return None

	def check(self, name):
		found = False
		for device in self.devices["devices"]:
			#print("Checking " + name + " with " + device["name"])
			if(device["name"] == name):
				found = True
				if(device["checked"] != 1): 
					return [False, device]
				break
		if(found):
			return [True, device]
		return [True, None]

	def swap(self, name, param):
		for device in self.devices["devices"]:
			if(device["name"] == name):
				try:
					#print("trying udp " + param)
					device["udp"].remove(param)
					device["pdp"].append(param)
					return True

				except ValueError:
					try:
						#print("trying pdp " + param)
						device["pdp"].remove(param)
						device["udp"].append(param)
						return True

					except ValueError:
						#print("neither")
						return False
		return False

	def write(self):
		stream = open('master.yaml', 'w')
		yaml.dump(self.devices, stream)
		stream.close()


	def addParam(self, name, uorp, var):
		for device in self.devices["devices"]:
			if(device["name"] == name):
				if uorp == "udp":
					device["udp"].append(var)
					return True
				elif uorp == "pdp":
					device["pdp"].append(var)
					return True
		return False

	def delete(self, name, uorp, var):
		for device in self.devices["devices"]:
			if(device["name"] == name):
				if uorp == "udp":
					device["udp"].remove(var)
					return True
				elif uorp == "pdp":
					device["pdp"].remove(var)
					return True
		return False

	def fix(self, device):
		usr = "foo"
		while usr != "syssave":
			clear()
			print("Please look over the device and ensure that the parameters are all correct and not missing")
			message = device["name"] + "\nUser Defined Parameters:" 
			for param in device["udp"]:
				message += " " + param
			message += " (" + str(len(device["udp"])) + ")"
			message +=  "\nPDK defined Parameters: "
			for param in device["pdp"]:
				message+= " " + param
			message += " (" + str(len(device["pdp"])) + ")"
			print(message)
			print("Please input parameter to swap, or use 'delete udp/pdp variable' to delete a parameter, use 'add udp/pdp var' to add parameter, hit syssave to save, check, and quit")
			while True:
				usr = input()
				if(usr != "syssave"):
					cmd = usr.split(" ")
					if(cmd[0] == "delete"):
						if(len(cmd) == 3 and self.delete(device["name"], cmd[1], cmd[2])):
							break
						else:
							print("Incorrect user command. Variable not found or incorrect format, use 'delete' followed by a space, 'udp' for user defined parameter or 'pdp' for pdk defined parameter, followed by a space and the variable name")
					elif(cmd[0] == "add"):
						print("here")
						if(len(cmd) == 3 and self.addParam(device["name"], cmd[1], cmd[2])):
							break
						else:
							print("Incorrect user command. Incorrect format, use 'add' followed by a space, 'udp' for user defined parameter or 'pdp' for pdk defined parameter, and final space followed by the variable name")
					else:
						done = self.swap( device["name"], cmd[0])
						if(done):
							break
						else:
							print("Variable not found")
				else:
					device["checked"] = 1
					break


	def run(self):
		netlist = yaml.load(open('netlist.yaml', 'r').read(), Loader=yaml.FullLoader)
		dnemessage = "WARNING: Devices not found: "
		masterfind = []
		find = []
		dne = False
		quit = False
		for device in netlist["devices"]:
			checkfind = self.check(device["name"])
			if(not checkfind[0]):
				find.append(checkfind[1])
				masterfind.append(checkfind[1])
			if(checkfind[1] == None):
				dne = True
				dnemessage += "\n" + device["name"]

		if(dne):
			print(dnemessage)
			#TODO: CLEAN UP MESSAGE
			print("Hit enter to continue. WARNING: no data regarding these devices will be saved or changed, please double check the netlist file, type \"quit\" to end process")
			usrcmd = input()
			if(usrcmd == "quit"):
				return[masterfind, True]

		cmd = "foo"
		while (len(find) > 0) and (cmd != 'q'):
			num = 1
			#TODO CLEAN UP MESSAGE
			message = "Devices need manual checking found in netlist:"
			for device in find:
				message += "\n" + str(num) + ": " + device["name"]
				num += 1
			print(message)
			print("Press \"Enter\" to start from the top, or enter what device number you'd like to check. Press q to quit")
			cmd = input()
			try:
				cmdnum = int(cmd)
				self.fix(find[cmdnum - 1])
				find.pop(cmdnum-1)
			except ValueError:
				if cmd == '':
					self.fix(find[0])
					find.pop(0)
				if cmd == 'q':
					quit = True
					break;
				if (cmd != 'q') or (cmd != ''):
					print("Please input a correct value")
			except IndexError:
					print("device number out of range")

			clear()
		self.write()
		return [masterfind, quit]


	def createSKILL(self, netlist):
		script = open('netlist_skill.il', 'w')
		config = open('config.txt', 'w')
		shared_udp = []
		shared_pdp = []
		script.write("procedure( find_EQ()\n \n input = \"config.txt\"\n desanitizer = \"desanitizer.config\"\n sanitizer = \"sanitizer.config\"\n pdk = \"" + self.devices["pdk"] + "\"\n \nwrite_desanitizer = outfile(desanitizer, \"a\")\nwrite_sanitizer = outfile(sanitizer, \"a\")\nunless(read_file=(infile input) (printf(\"***NO FILE FOUND***\\n\")))\n\n;open file stream\nwhen(read_file=(infile input)\nwhile( gets(device_line read_file)\n \n;read line of devices\ndevices = parseString(device_line \" \\n\")\n\n;when not an empty line\nwhen(nequal(length(devices), 0)\n\n;read second line - user defined params\ngets(param_line read_file)\nparam = parseString(param_line \" \\n\")\n\n;read third line - find equations\ngets(eq_line read_file)\neq = parseString(eq_line \" \\n\")\n\n;iterate for all individual device in devices\nfor(device 0 length(devices)-1\n\n    ;instantiate object, print object name to output file\nschHiCreateInst()\nschCreateInstForm->libraryName->value=pdk\nschCreateInstForm->cellName->value=nth(device devices)\nprintf(nth(device devices))\nfprintf(write_desanitizer \"%s, \" nth(device devices))\nfprintf(write_sanitizer \"%s,\" nth(device devices))\n\n;iterate through all input parameters and set them\nparam_num = 0\nwhile(param_num <= length(param)-1\ncase( nth(param_num param)\n")
		for device in netlist:
			line = device["name"] + "\n" 
			for var in device["udp"]:
				line += var + " "
				if(not (var in shared_udp)):
					shared_udp.append(var)
			line += "\n"
			for var in device["pdp"]:
				line += var + " "
				if(not (var in shared_pdp)):
					shared_pdp.append(var)
			line +="\n\n"
			config.write(line)

		for param in shared_udp:
			script.write("(\"" + param + "\" \nerrset(schCreateInstForm->" + param + "->value=\"" + param + "\")\nfprintf(write_desanitizer \"" + param + " \")\nfprintf(write_sanitizer \"" + param + " \")\n)\n\n")
		
		script.write(";variable not found, print to file missing input param definition\n(t\nprintf(\"USER INPUT VARIABLE: %s NOT FOUND\\n\" nth(param_num param))\n)\n);case\nparam_num = param_num + 1\n);while\n\n")
		script.write("fprintf(write_desanitizer \", %d\\n\" length(eq))\nfprintf(write_sanitizer \"\\n\")\n\n;find corresponding equations and print to text file\neq_num = 0\nwhen(boundp('cdfgData)\nlet( ((cdf cdfgData))\nwhile( eq_num <= length(eq)-1\ncase( nth(eq_num eq)\n")
		for param in shared_pdp:
			script.write("(\"" + param + "\"\n" + "fprintf(write_desanitizer \""+ param +" = %s\\n\" cdf~>" + param + "~>value)\n" + ")\n\n")
		script.write("(t\nfprintf(write_desanitizer \"USER INPUT VARIABLE: %s NOT FOUND\\n\" nth(param_num param))\n))\neq_num = eq_num + 1\n);while\n);let\n);when\n);for\n); when\n);while\n);when\n\nclose(write_desanitizer)\nclose(write_sanitizer)\nclose(read_file)\n);end procedure\n")

		script.close()
		config.close()


def txtToYAML():
	if os.path.isfile('master.yaml'):
		return

	lines = open("devices.txt").read().splitlines()
	
	with open("master.yaml", 'w') as stream:
		stream.write("---\n")
		stream.write("pdk: " + lines[0] + "\n")
		stream.write("devices: \n")
		common = lines[1].split()
		for i in range(2, len(lines), 4):
			listudp = []
			listpdp = []
			num = len(lines[i + 2].split())
			if(num != 0):
				linelist = lines[i+1].split()
				for j in range(0,len(linelist)):
					if(linelist[j] in common):
						listudp.append(linelist[j])
					elif(j < num):
						listudp.append(linelist[j])
					else:
						listpdp.append(linelist[j])
			for val in lines[i+3].split():
				if val != "nil" and val[:2] != "\\$" and not (val in listudp):
					listudp.append(val)
			if(len(listudp) != 0 or len(listpdp) != 0):
				stream.write("- name: " + "\""+ lines[i] +"\"" + "\n")
				stream.write("  checked: " + "0" + "\n");
				stream.write("  udp: [");
				
				line = ""
				for param in listudp:
					line +="\""+param +"\", "
				line = line[:-2]
				stream.write(line + "]\n")
				
				stream.write("  pdp: [");
				line = ""
				for param in listpdp:
					line +="\""+param +"\", "
				line = line[:-2]
				stream.write(line + "]\n\n")


def readYAML():
	config = open('master.yaml', 'r').read()
	#print(config);
	return yaml.load(config, Loader=yaml.FullLoader)



if __name__ == '__main__':
	clear()
	'''print("Please enter the PDK you'd like to use")
	usrinput = input()'''
	txtToYAML()
	data = SanitizerUI(readYAML())
	netlist = data.run()
	if(not netlist[1]):
		clear()
		if(len(netlist[0]) != 0):
			print("PDK master config updated!")
			data.createSKILL(netlist[0])
			print("SKILL script Created!")
			print("Please run SKILL script in cadence before running Sanitizer/Desanitizer: check README for additional instructions")
			print("Hit Enter to continue ONLY AFTER THE SKILL SCRIPT HAS BEEN RUN AND THE FILE HAS BEEN MOVED")
			input()
		else:
			print("All Devices found! Sanitizer/Desanitizer will be safely used on this netlist")	
	else:
		print("Program Aborted")