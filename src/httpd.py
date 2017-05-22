#
#	Word Tutorial Markup Language
#	Module:		httpd.py
#	Program:	Crisp(crispgm@gmail.com)
#	Abstract:	http server daemon
#	This program is distributed under GNU General Public License, v3.
#	See details in http://gpl.gnu.org/
#
import BaseHTTPServer, os
import wts, conf

class WebRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_GET(self):
		self._gotoPath()
		
	def _gotoPath(self):
		cfg = conf.wts_config()
		my_conf = cfg.getConf()
		is_process = 0
		#request index
		if(self.path=='/'):
			is_process = 1
			print('requesting index page')
			print('requesting '+my_conf['http_index'])
			self._showHTML(my_conf['http_root'],my_conf['http_index'])
		#request wtml
		if(self.path.endswith(".wtml")):
			is_process = 1
			fn = self.path[1:len(self.path)]
			print('requesting wtml: '+self.path)
			w = wts.wts(fn)
			w._output()
			self._showHTML(my_conf['http_temp'],fn)
		#request html
		if(self.path.endswith(".html") or self.path.endswith(".htm")):
			is_process = 1
			print('requesting text/html: '+self.path)
			self._showHTML(my_conf['http_root'],self.path)
		#request xml
		if(self.path.endswith(".xml")):
			is_process = 1
			print('requesting text/xml: '+self.path)
			self._showHTML(my_conf['http_root'],self.path)
		#request images
		if(self.path.endswith(".jpg") or self.path.endswith(".jpeg")):
			is_process = 1
			print('requesting image/jpeg: '+self.path)
			self._showJPG(my_conf['http_root'],self.path)
		if(self.path.endswith(".gif")):
			is_process = 1
			print('requesting image/gif: '+self.path)
			self._showGIF(my_conf['http_root'],self.path)
		if(self.path.endswith(".bmp")):
			is_process = 1
			print('requesting image/bmp: '+self.path)
			self._showGIF(my_conf['http_root'],self.path)
		if(self.path.endswith(".png")):
			is_process = 1
			print('requesting image/x-png: '+self.path)
			self._showPNG(my_conf['http_root'],self.path)
		#request css
		if(self.path.endswith(".css")):
			is_process = 1
			print('requesting text/css: '+self.path)
			self._showCSS(my_conf['http_root'],self.path)
		#request text
		if(self.path.endswith(".txt") or self.path.endswith(".c") or self.path.endswith(".h") or self.path.endswith(".cpp") or self.path.endswith(".java")):
			is_process = 1
			print('requesting text/plain: '+self.path)
			self._showTEXT(my_conf['http_root'],self.path)
		#request js
		if(self.path.endswith(".js")):
			is_process = 1
			print('requesting text/javascript: '+self.path)
			self._showTEXT(my_conf['http_root'],self.path)
		if(self.path.endswith(".json")):
			is_process = 1
			print('requesting application/json: '+self.path)
			self._showJSON(my_conf['http_root'],self.path)
		#request cab
		if(self.path.endswith(".cab") or self.path.endswith(".exe")):
			is_process = 1
			print('requesting application/octet-stream: '+self.path)
			self._showCAB(my_conf['http_root'],self.path)
		#request midi
		if(self.path.endswith(".mid") or self.path.endswith(".midi")):
			is_process = 1
			print('requesting x-music/midi: '+self.path)
			self._showMIDI(my_conf['http_root'],self.path)
		#request wave
		if(self.path.endswith(".wav")):
			is_process = 1
			print('requesting audio/x-wav: '+self.path)
			self._showWAV(my_conf['http_root'],self.path)
		#request mpeg
		if(self.path.endswith(".mpg") or self.path.endswith(".mpeg")):
			is_process = 1
			print('requesting video/mpeg: '+self.path)
			self._showMPEG(my_conf['http_root'],self.path)
		#request mov
		if(self.path.endswith(".qt") or self.path.endswith(".mov")):
			is_process = 1
			print('requesting video/quicktime: '+self.path)
			self._showMOV(my_conf['http_root'],self.path)
		#request avi
		if(self.path.endswith(".avi")):
			is_process = 1
			print('requesting video/x-msvideo: '+self.path)
			self._showAVI(my_conf['http_root'],self.path)
		#request midi
		if(self.path.endswith(".zip")):
			is_process = 1
			print('requesting application/zip: '+self.path)
			self._showZIP(my_conf['http_root'],self.path)
		#request doc
		if(self.path.endswith(".doc") or self.path.endswith(".docx") or self.path.endswith(".wps")):
			is_process = 1
			print('requesting application/msword: '+self.path)
			self._showDOC(my_conf['http_root'],self.path)
		#except:
		if(is_process==0):
			print('warning: unknown request')
			self.send_response(404)
			
	def _readFile(self,dir,fn):
		try:
			f = open(dir+fn,'rb')
			c = f.read()
			self.wfile.write(c)
			f.close()
		except:
			print("error: "+dir+fn+" not found.")
			
	def _sendHeader(self,dir,fn,content_type):
		self.send_response(200)
		self.send_header('Content-type',content_type)
		self.send_header('Server','Crisp WTS Server/Python')
		self.end_headers()
			
	def _showHTML(self,dir,fn):
		self._sendHeader(dir,fn,'text/html')
		self.end_headers()
		self._readFile(dir,fn)
			
	def _showJPG(self,dir,fn):
		self._sendHeader(dir,fn,'image/jpeg')
		self._readFile(dir,fn)
			
	def _showGIF(self,dir,fn):
		self._sendHeader(dir,fn,'image/gif')
		self._readFile(dir,fn)
			
	def _showBMP(self,dir,fn):
		self._sendHeader(dir,fn,'image/bmp')
		self._readFile(dir,fn)
		
	def _showPNG(self,dir,fn):
		self._sendHeader(dir,fn,'image/x-png')
		self._readFile(dir,fn)
		
	def _showTEXT(self,dir,fn):
		self._sendHeader(dir,fn,'text/plain')
		self._readFile(dir,fn)
	
	def _showCSS(self,dir,fn):
		self._sendHeader(dir,fn,'text/css')
		self._readFile(dir,fn)
	
	def _showJS(self,dir,fn):
		self._sendHeader(dir,fn,'text/plain')
		self._readFile(dir,fn)
		
	def _showJSON(self,dir,fn):
		self._sendHeader(dir,fn,'application/json')
		self._readFile(dir,fn)
		
	def _showCAB(self,dir,fn):
		self._sendHeader(dir,fn,'application/octet-stream')
		self._readFile(dir,fn)
		
	def _showDOC(self,dir,fn):
		self._sendHeader(dir,fn,'application/msword')
		self._readFile(dir,fn)
		
	def _showXML(self,dir,fn):
		self._sendHeader(dir,fn,'text/xml')
		self._readFile(dir,fn)
		
	def _showMIDI(self,dir,fn):
		self._sendHeader(dir,fn,'x-music/midi')
		self._readFile(dir,fn)

	def _showWAV(self,dir,fn):
		self._sendHeader(dir,fn,'audio/x-wav')
		self._readFile(dir,fn)
	def _showMPEG(self,dir,fn):
		self._sendHeader(dir,fn,'video/mpeg')
		self._readFile(dir,fn)
	def _showMOV(self,dir,fn):
		self._sendHeader(dir,fn,'video/quicktime')
		self._readFile(dir,fn)
	def _showAVI(self,dir,fn):
		self._sendHeader(dir,fn,'video/x-msvideo')
		self._readFile(dir,fn)
	def _showZIP(self,dir,fn):
		self._sendHeader(dir,fn,'application/zip')
		self._readFile(dir,fn)
		
			
if __name__=='__main__':
	print('warning: HTTPD module must be imported.')
