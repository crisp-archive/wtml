# -*- coding: utf-8 -*-
#
#	Word Tutorial Markup Language
#	Module:		wtml.py
#	Program:	Crisp(crispgm@gmail.com)
#	Abstract:	wtml parser
#	This program is distributed under GNU General Public License, v3.
#	See details in http://gpl.gnu.org/
#
import xml.dom.minidom
import conf

class wtml_parser:
	# general member vars
	src = None
	dom = None
	manifest={}
	content=[]
	
	def __init__(self, src):
		c=conf.wts_config()
		my_conf=c.getConf()
		self.src = my_conf['http_root']+src
		
	def parse(self):
		self._open()
		self._parseManifestSection()
		self._parseContentSection()
		return [self.manifest,self.content]
		
	def _open(self):
		handle = open(self.src)
		self.dom = xml.dom.minidom.parse(handle)
			
	def _getText(self, nodelist):
		rc = []
		for node in nodelist:
			if(node.nodeType == node.TEXT_NODE or node.nodeType==node.CDATA_SECTION_NODE):
				rc.append(node.data)
		return ''.join(rc)
		
	def _parseManifestSection(self):
		systemDom	= self.dom.getElementsByTagName('manifest')[0]
		title	= self._getText( systemDom.getElementsByTagName('title')[0].childNodes )
		legend	= self._getText( systemDom.getElementsByTagName('legend')[0].childNodes )
		author	= self._getText( systemDom.getElementsByTagName('author')[0].childNodes )
		version= self._getText( systemDom.getElementsByTagName('version')[0].childNodes )
		logo	= self._getText( systemDom.getElementsByTagName('logo')[0].childNodes )
		licenseName = self._getText( systemDom.getElementsByTagName('copyright')[0].childNodes )
		licenseLink = systemDom.getElementsByTagName('copyright')[0].getAttribute('link')
		cssfile= self._getText( systemDom.getElementsByTagName('style')[0].childNodes )
		
		self.manifest = {'title':title, 'legend':legend, 'author':author, 'version':version, 'logo':logo, 'licenseName':licenseName,
		'licenseLink':licenseLink, 'cssfile':cssfile}
		
	def _parseContentSection(self):
		systemDom	= self.dom.getElementsByTagName('content')[0]
		chapterDom = systemDom.getElementsByTagName('chapter')
		chapter_dict={}
		del self.content[:]
		for chapter in chapterDom:
			title	= self._getText(chapter.getElementsByTagName('title')[0].childNodes)
			abstract= self._getText(chapter.getElementsByTagName('abstract')[0].childNodes)
			end		= self._getText(chapter.getElementsByTagName('end')[0].childNodes)
			paraDom	= chapter.getElementsByTagName('paragraph')
			para_list=[]
			for para in paraDom:
				para_dict={'type':para.getAttribute('type'),'content':self._getText(para.childNodes),'function':para.getAttribute('function')}
				para_list.append(para_dict)
			chapter_dict={'title':title,'abstract':abstract,'end':end,'para_list':para_list}
			self.content.append(chapter_dict)

if __name__=='__main__':
	print('warning: WTS module must be imported.')