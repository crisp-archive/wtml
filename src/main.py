#
#	Word Tutorial Markup Language
#	Module:		main.py
#	Program:	Crisp(crispgm@gmail.com)
#	Abstract:	program shells
#	This program is distributed under GNU General Public License, v3.
#	See details in http://gpl.gnu.org/
#

# import from system
import sys
import os
import BaseHTTPServer
import threading
# import from custom class
from httpd import WebRequestHandler
import conf

def main():
	argc = len(sys.argv)
	cfg = conf.wts_config()
	my_conf = cfg.getConf()
	if( argc == 2 ):
		if( sys.argv[1] == '-v' or sys.argv[1] == '--version'):
			print("Word Tutorial System")
			print("Version 1.0")
			print("Copyright(c)David Zhang @ Southeast University")
			print("All rights reserved.")
		elif( sys.argv[1] == '-h' or sys.argv[1]=='--help'):
			usage()
		elif( sys.argv[1]=='-clear'):
			clear_temp(my_conf['http_temp'])
		elif( sys.argv[1]=='-conf'):
			show_conf(my_conf)
		elif( sys.argv[1] == '-start' ):
			s1 = server(my_conf['http_name'],my_conf['http_ip'],my_conf['http_port'])
			s1.start()
			s2 = server(my_conf['http_name'],'127.0.0.1',my_conf['http_port'])
			s2.start()
		else:
			bad()
	else:
		bad()
	
def usage():
	print("Usage:")
	print("run server:\t-start")
	print("show version:\t-v, --version")
	print("show usage:\t-h, --help")
	print("clear temp:\t-clear")
	print("show conf:\t-conf")

def bad():
	print("bad commands")
	print("type -h to view usage")
	
def clear_temp(temp_path):
	print("clear temp files in "+temp_path)
	for root,dir,files in os.walk(temp_path):
		for f in files:
			try:
				print('removing '+temp_path+f+'...')
				os.remove(temp_path+f)
			except:
				print('Error: Unable to remove '+f)
	print("success.")

def show_conf(conf):
	print('http_name:\t'	+ conf['http_name'])
	print('http_ip:\t'		+ conf['http_ip'])
	print('http_port:\t%d'	% conf['http_port'])
	print('http_root:\t'	+ conf['http_root'])
	print('http_temp:\t'	+ conf['http_temp'])

class server(threading.Thread):
	def __init__(self,name,ip,port):
		threading.Thread.__init__(self)
		self.name=name
		self.ip=ip
		self.port=port
		print("\ncreating "+self.name+"...")
	def run(self):
		print("listening %s:%s."%(self.ip,self.port))
		httpd = BaseHTTPServer.HTTPServer((self.ip,self.port), WebRequestHandler)
		httpd.serve_forever()

if __name__ == "__main__":
	main()
	