#CUT

from pathlib import Path

import PyPDF2

import sys

import os

 

pdf_dir = Path("./run")

pdf_files = sorted(pdf_dir.glob("*.pdf"))

 

print(pdf_dir.resolve())

 

a = "unknown"

a = input("auto cut(a) or manual cut(m) :")

 

if(a == "a"):

　while True:

　　def split_pdf_pages(src_path, dst_basepath):

　　　src_pdf = PyPDF2.PdfFileReader(src_path)

　　　for i in range(src_pdf.numPages):

　　　　dst_pdf = PyPDF2.PdfFileWriter()

　　　　dst_pdf.addPage(src_pdf.getPage(i))

　　　　with open('{}_{}.pdf'.format(dst_basepath, i), 'wb') as f:

　　　　　dst_pdf.write(f)

 

　　for file in os.listdir("./run"):

　　　print(file)

 

　　if(len(pdf_files) == 1):

　　　pdf_dir = pdf_dir.resolve()

　　　split_pdf_pages(str(pdf_dir), str(pdf_dir))

　　　print("<<success>>")

　　　break

 

　　else :

　　　a = input("auto cut is possible only when there is one file.\ndo you want to try again? (y/n) :")

 

　　　if(a == "y"):

　　　　continue

　　　else :

　　　　print("end")

　　　　break

 

elif(a == "m"):

　def split_pdf_pages(src_path, dst_basepath):

　　src_pdf = PyPDF2.PdfFileReader(src_path)

　　for i in range(src_pdf.numPages):

　　　dst_pdf = PyPDF2.PdfFileWriter()

　　　dst_pdf.addPage(src_pdf.getPage(i))

　　　with open('{}_{}.pdf'.format(dst_basepath[:-4], i+1), 'wb') as f:

　　　　dst_pdf.write(f)

 

　for file in os.listdir("./run"):

　　print(file)

 

　pdf = ""

　pdf = input("input filename:")

 

　if(pdf==""):

　　print("<<error>>")

　　sys.exit()

 

　pdf_iname = "./run/" + pdf + ".pdf"

 

　pdf = ""

　pdf = input("output filename:")

             

　if(pdf==""):

　　print("<<error>>")

　　sys.exit()

             

　pdf_oname = "./result/" + pdf + ".pdf"

             

　split_pdf_pages(pdf_iname, pdf_oname)

　print("<<success>>")

 

else :

　print("end")