#TURN

from pathlib import Path

import sys

import PyPDF2

import glob

import os

 

pdf_dir = Path("./run/")

pdf_files = sorted(pdf_dir.glob("*.pdf"))

 

print(pdf_files)

 

p_file = input("file name? :")

 

p_angle = input("roll angle? (90,180,270) :")

p_angle = int(p_angle)

 

if(p_angle == 90):

　angle_num = 1

 

elif(p_angle == 180):

　angle_num = 2

 

elif(p_angle == 270):

　angle_num = 3

 

#p_angle = 90

 

file = PyPDF2.PdfFileReader(open('./run/' + p_file + '.pdf', 'rb'))

file_output = PyPDF2.PdfFileWriter()

for page_num in range(file.numPages):

　page = file.getPage(page_num)

 

　for i in range(angle_num):

　　page.rotateClockwise(90)

 

　file_output.addPage(page)

with open('./result/' + p_file +  '_roll.pdf', 'wb') as f:

　file_output.write(f)

 

print("<<success>>")