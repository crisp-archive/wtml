# -*- coding: utf-8 -*-
#
#	Word Tutorial Markup Language
#	Module:		wts.py
#	Program:	Crisp(crispgm@gmail.com)
#	Abstract:	generate html by parsing wtml
#	This program is distributed under GNU General Public License, v3.
#	See details in http://gpl.gnu.org/
#
import shutil,codecs
import wtml, conf

class wts:
	# general member vars
	src = None
	manifest = {}
	content = []
	my_conf=None
	f=None
	
	def __init__(self, src):
		self.src = src
		wp = wtml.wtml_parser(self.src)
		(self.manifest,self.content) = wp.parse()
		#read conf
		cfg = conf.wts_config()
		self.my_conf = cfg.getConf()
	
	def _output(self):
		try:
			self.f = codecs.open(self.my_conf['http_temp']+self.src,'w','utf-8')
			print('writing html')
			self._outputHeader()
			self._outputContent()
			self._outputFooter()
			self.f.close()
		except:
			print('Error: Unable to output '+self.src)
			return
	
	def _outputHeader(self):	
		# common headers
		self.f.write('<!DOCTYPE HTML><html><head><meta http-equiv="content-type" content="text/html; charset=utf-8"><script language="JScript" src="/res/object.js"></script>')
		self.f.write('<script type="text/javascript" src="/res/jquery-1.5.min.js"></script>')
		#css
		self.f.write('<link rel="stylesheet" type="text/css" href="')
		self.f.write(self.manifest['cssfile'])
		self.f.write('"></link>')
		#title
		self.f.write('<title>'+self.manifest['title']+'</title>')
		self.f.write('</head>')
		self.f.write('<body>')
		self.f.write('<div id="head">')
		self.f.write('<div id="logo"><img src="'+self.manifest['logo']+'"></div>')
		self.f.write('<div id="navi">')
		self.f.write('<div id="title">'+self.manifest['title']+'</div>')
		self.f.write('<div id="legend">'+self.manifest['legend']+'</div>')
		self.f.write('<div id="menu">')
		self.f.write('<div class="menu_item"><a href="javascript:window.close();">'+u'退出'+'</a></div>')
		self.f.write('<div class="menu_item"><a href="#about">'+u'关于'+'</a></div>')
		self.f.write('<div class="menu_item"><a href="/">'+u'主页'+'</a></div>')
		self.f.write('</div></div></div>')
		self.f.write('<div id="main">')
		self.f.write('<div id="content">')
		
	def _outputFooter(self):
		self.f.write('</div></div>')
		self.f.write('<div id="about">')
		self.f.write('<div id="about_content">')
		self.f.write('Author: '+self.manifest['author']+'<br>')
		self.f.write('License: <a href="')
		self.f.write(self.manifest['licenseLink'])
		self.f.write('">')
		self.f.write(self.manifest['licenseName'])
		self.f.write('</a><br><br>')
		self.f.write('Powered by Word Tutorial System.<br>')
		self.f.write('Copyright &copy; Crisp, 2011')
		self.f.write('</div></div>')
		self.f.write('</body></html>')
		
	def _outputContent(self):
		for chapter in self.content:
			self.f.write('<div class="section_content"><div class="section_title">')
			self.f.write(chapter['title'])
			self.f.write('</div>')
			self.f.write('<div class="section_intro">')
			self.f.write(chapter['abstract'])
			self.f.write('</div>')
			self.f.write('<div class="section_body">')
			for para in chapter['para_list']:
				if(para['type']=='text'):
					self.f.write('<div>'+para['content']+'</div>')
				elif(para['type']=='object'):
					self._outputObject()
				elif(para['type']=='button'):
					self._outputButton(para['content'],para['function'])
				else:
					print('Error: Unexpected paragraph type')
					return
			self.f.write('</div>')
			self.f.write('<div class="section_end">')
			self.f.write(chapter['end'])
			self.f.write('</div>')
			self.f.write('</div>')
			
	def _outputObject(self):
		self.f.write('<input id="obj_show" type="button" value="'+u'显示WORD控件'+'" onclick="javascript:$(\'#object\').show();$(\'#obj_show\').hide();">');
		self.f.write('<div id="object" style="display:none;text-align:center;"><object id="TANGER_OCX" classid="clsid:A39F1330-3322-4a1d-9BF0-0BA2BB90E970" codebase="/res/OfficeControl.cab" width="980px" height="480px">')
		self.f.write('<param name="Caption" value="WTS">')
		self.f.write('</object></div>')
		
	def _outputButton(self,name,function):
		self.f.write('<input type="button" value="'+name+'" onclick="'+function+'">')
	
if __name__ == "__main__":
	print('warning: WTS module must be imported.')
	