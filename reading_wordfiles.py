import docx2txt
import os
dir_path="C://Users//Ravi yadav//Desktop//"
os.chdir(dir_path)
result=docx2txt.process("timetable.docx")
print(result)