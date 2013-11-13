import glob, os
from PyPDF2 import PdfFileReader, pdf

#stores a dictionary of PageID : PageNumber pairs.
global page_num_library
global file_name

# receives a PDffileReader.getOutlines() object and converts it into a list of title
def build_nav(outline):
	output = ""
	for obj in outline:
		if isinstance(obj, pdf.Destination):
			chap_title = obj.title.replace(u'\u2013', '-').replace(u'\u2014', '-')
			page_num = page_num_library[obj.page.idnum]+1
			page_top = obj.top
			link = "<a href='" + file_name + "#page=" + str(page_num) + "&pagemode=none'>"
			output += "<li>" + link + chap_title + "</a></li>"

		elif isinstance(obj, list):
			output += "<ul>" + build_nav(obj)
	
	return output + "</ul>"


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

# delete output if it already exists
try:
    os.remove("output.html")
except OSError:
    pass

# loop over pdf folder
for fileName in glob.glob("pdf/*.pdf"):
	
	file_name = fileName
	inputFile = PdfFileReader(open(file_name, "rb"))
	page_num_library = setup_page_id_to_num(inputFile)

	docInfo = inputFile.getDocumentInfo().title
	docOutline = inputFile.getOutlines()

	output = build_nav(docOutline)

	f = open("output.html", "a")

	#for x in output:
	#	f.write(x.encode('utf-8') + "\n")
	f.write(output.encode('utf-8'))

	f.close()

print ("Success!")