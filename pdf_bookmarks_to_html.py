#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
from PyPDF2 import PdfFileReader, pdf

global page_num_library

def build_nav(outline,tab,_result=None):
	if _result is None:
		_result = []

	for obj in outline:	
		if isinstance(obj, pdf.Destination):
			#print ( obj.page.idnum )
			_result.append( (tab * " ") + obj.title.replace(u'\u2013', '-').replace(u'\u2014', '-') + "(" +  str(page_num_library[obj.page.idnum]+1) + "," + str(obj.top) + ")")
		elif isinstance(obj, list):
			build_nav(obj,tab+1, _result)
	return _result

# receives the PDFFIleReader object and returns a library or page.idnums : page numbers
def setup_page_id_to_num(inputFile, pages=None, _result=None, _num_pages=None):
    if _result is None:
        _result = {}
    if pages is None:
        _num_pages = []
        pages = inputFile.trailer["/Root"].getObject()["/Pages"].getObject()
    t = pages["/Type"]

    if t == "/Pages":
        for page in pages["/Kids"]:
            _result[page.idnum] = len(_num_pages)
            setup_page_id_to_num(inputFile,page.getObject(), _result, _num_pages)
    elif t == "/Page":
        _num_pages.append(1)
    return _result


inputFile = PdfFileReader(open("pdf/EACF_AIR.pdf", "rb"))
page_num_library = setup_page_id_to_num(inputFile)

docInfo = inputFile.getDocumentInfo().title
docOutline = inputFile.getOutlines()

output = build_nav(docOutline,0)

f = open("output.txt", "w")

for x in output:
	f.write(x.encode('utf-8') + "\n")

f.close()

print ("Success!")