# PDF Bookmarks to HTML

## Description
Program pulls the bookmarks from all the PDFs contained in a folder.  The boomkarks are formatted into a nested unordered list with Bootstrap class hooks.

[The program is heavily based off this Stack Overflow question.](http://stackoverflow.com/questions/7602639/pypdf-merge-and-write-issue)

## Requirements
*Python 2.7
*PyPDF2 (or PyPDF)

## Usage
Create a PDF folder and run the script from one folder below that.

You'll receive a output.html file with all the pdf bookmarks stored in an unordered list linking back to the source PDF and page number.

## Purpose
I needed a way to create a HTML Table of Contents for a series of PDFs.
The PDF would sit in an iFrame would be controlled by the HTML ToC.

The [Parameters Opening PDF Files](http://www.adobe.com/content/dam/Adobe/en/devnet/acrobat/pdfs/pdf_open_parameters.pdf) was very helpful.



