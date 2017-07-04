from email_hunter import EmailHunterClient
import json
import sys,getopt
try:
	opts, args = getopt.getopt(sys.argv[1:],"hd:v",["help","domain="])
except getopt.GetoptError:
	print('EmailHunter.py -d <domain>')
	sys.exit(2)
for opt, arg in opts:
	if opt == '-h':
		print('EmailHunter.py -d <domain>')
		sys.exit()
	elif opt in ("-d", "--domain"):
		client = EmailHunterClient(<API key>)
		result=client.search(arg)
		for each in result:
			if(client.exist(each['value'])[0]):
				print("%s is exist" % (each['value'])) 