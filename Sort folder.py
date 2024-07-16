# Importing libraries
from pathlib import Path
import os
import shutil
    
folder_hold = ['docx', 'pdf', 'csv', 'txt', 'xlsx', 'xls', 'wbk', 'zipe', 'vcf', 'pptx', 'Others']
    
# path to folder 
the_file = Path("C:/Phoenix/holder") 

for item in folder_hold:
    os.makedirs(os.path.join(the_file, item), exist_ok=True)

# Formats for different files
csv = (".csv")

pdf = (".pdf")

xlsx = (".xlsx", '.XLXS')

txt = ('.txt')

docx = ('.doc', '.docx')

vcf = ('.vcf')

wbk = ('.wbk')

pptx = ('.pptx')

xls = ('.xls')

zipe = ('.zip')

folder = ('')




# Functions for sorting different files
def is_csv(file):
    return os.path.splitext(file)[1] in csv

def is_pdf(file):
    return os.path.splitext(file)[1] in pdf

def is_txt(file):
    return os.path.splitext(file)[1] in txt

def is_xlsx(file):
    return os.path.splitext(file)[1] in xlsx

def is_zip(file):
    return os.path.splitext(file)[1] in zipe

def is_xls(file):
    return os.path.splitext(file)[1] in xls

def is_folder(file):
    return os.path.splitext(file)[1] in folder

def is_pptx(file):
    return os.path.splitext(file)[1] in pptx

def is_docx(file):
    return os.path.splitext(file)[1] in docx


def is_vcf(file):
    return os.path.splitext(file)[1] in vcf

def is_wbk(file):
    return os.path.splitext(file)[1] in wbk


# Switching to directory being sorted
os.chdir(the_file)

# loop for sorting the files into different folders
for file in os.listdir():
    if is_pptx(file):
        shutil.move(file, f"{the_file}/pptx")
    elif is_docx(file):
        shutil.move(file, f"{the_file}/docx")
    elif is_zip(file):
        shutil.move(file, f"{the_file}/zipe")
    elif is_xlsx(file):
        shutil.move(file, f"{the_file}/xlsx")
    elif is_wbk(file):
        shutil.move(file, f"{the_file}/wbk")
    elif is_txt(file):
        shutil.move(file, f"{the_file}/txt")
    elif is_csv(file):
        shutil.move(file, f"{the_file}/csv")
    elif is_xls(file):
        shutil.move(file, f"{the_file}/xls")
    elif is_pdf(file):
        shutil.move(file, f"{the_file}/pdf")
    elif is_vcf(file):
        shutil.move(file, f"{the_file}/vcf")
    elif is_folder(file):
        print('This is a folder')
    else:
        shutil.move(file, f"{the_file}/Others")
            