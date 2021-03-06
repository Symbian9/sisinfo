"""
Copyright (c) 2006, Jari Sukanen
All rights reserved.

Redistribution and use in source and binary forms, with or 
without modification, are permitted provided that the following 
conditions are met:
	* Redistributions of source code must retain the above copyright 
	  notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright 
	  notice, this list of conditions and the following disclaimer in 
	  the documentation and/or other materials provided with the 
	  distribution.
    * Names of the contributors may not be used to endorse or promote 
	  products derived from this software without specific prior written 
	  permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED 
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR 
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS 
BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
"""

import struct
import sisfields, sisreader
		
class SISInfo(sisfields.SISField) :
	def __init__(self) :
		sisfields.SISField.__init__(self)
		self.fin = None
		self.fileHeader = sisfields.SISFileHeader()
		
	def parse(self, filename) :
		fin = open(filename, 'rb')
		fileReader = sisreader.SISFileReader(fin)
		self.parseHeader(fileReader)
		self.parseSISFields(fileReader)
		
	def parseHeader(self, fileReader) :
		self.fileHeader.uid1 = fileReader.readBytesAsUint(4)
		self.fileHeader.uid2 = fileReader.readBytesAsUint(4)
		self.fileHeader.uid3 = fileReader.readBytesAsUint(4)
		self.fileHeader.uidChecksum = fileReader.readBytesAsUint(4)
		
	def parseSISFields(self, fileReader) :
		parser = sisreader.SISFieldParser()
		while not fileReader.isEof() :
			self.subFields.append(parser.parseField(fileReader))
