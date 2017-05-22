#
#	Word Tutorial Markup Language
#	Module:		conf.py
#	Program:	Crisp(crispgm@gmail.com)
#	Abstract:	conf.ini parser
#	This program is distributed under GNU General Public License, v3.
#	See details in http://gpl.gnu.org/
#
import ConfigParser

class wts_config:
	http_name	= "WTS Server"
	http_ip		= "127.0.0.1"
	http_port	= "8080"
	http_index	= "index.wtml"
	http_root	= "d:\\wtml\\www"
	http_temp	= "d:\\wtml\\temp"
	handle		= None
	def __init__(self):
		self.handle = ConfigParser.ConfigParser()
		try:
			self.handle.read("conf/conf.ini")
		except:
			print("error: cannot open config file.")
			exit()
			
	def getConf(self):
		#0
		self.http_name	= self.handle.get('http','name')
		#1
		self.http_ip	= self.handle.get('http','ip')
		#2
		self.http_port	= self.handle.getint('http','port')
		#3
		self.http_index	= self.handle.get('http','index')
		#4
		self.http_root	= self.handle.get('http','root')
		#5
		self.http_temp	= self.handle.get('http','temp')
		
		conf = {'http_name':self.http_name, 'http_ip':self.http_ip, 'http_port':self.http_port, 'http_index':self.http_index, 
		'http_root':self.http_root, 'http_temp':self.http_temp}
		return conf
