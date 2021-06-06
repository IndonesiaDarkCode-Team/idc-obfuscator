import base64
import os
import sys
print ("contoh file.php")
code = ""
try:
		file = raw_input("Nama File yang mau di Obfuscate : ")
		code = open(file,"r").read()
except I0Error :
	print ("[!] FILE TIDAK ADA!!!")
	sys.exit()
rep = str(code).replace ("<?php","").replace ("?>","")
enc = base64.b64encode(rep)
data = """<?php
//   Coded by: cyruxxsec -  OBFUSCATED BY IndonesiaDarkCode
// site: idc-team.com 
eval(base64_decode('%s'));
?>"""%(enc)
out = raw_input("OUT : ")
open(out,"w").write(data)
