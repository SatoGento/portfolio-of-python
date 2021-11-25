#MERGE

from pathlib import Path

import PyPDF2

import sys

 

merger = PyPDF2.PdfFileMerger()

 

pdf_dir = Path("./run")

pdf_files = sorted(pdf_dir.glob("*.pdf"))

 

a = "unknown"

a = input("all merge(a) or select maerge(s) :")

 

if (a == "a"):

pdf_writer = PyPDF2.PdfFileWriter()

 

for pdf_file in pdf_files:

  pdf_reader = PyPDF2.PdfFileReader(str(pdf_file))

 

  for i in range(pdf_reader.getNumPages()):

   pdf_writer.addPage(pdf_reader.getPage(i))

 

merged_file = "./result/" + pdf_files[0].stem + "-" + pdf_files[-1].stem + ".pdf"

 

with open(merged_file, "wb") as f:

  pdf_writer.write(f)

 

elif (a == "s") :

print(pdf_files)

 

while (a != "end"):

  a = input("file name? :")

 

  if(a == "end"):

   break

 

  merger.append('./run/{}.pdf'.format(a))

 

merger.write('./merge.pdf')

merger.close()

 

else :

print("end")