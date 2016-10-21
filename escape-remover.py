import sys
import re

def str_dump(str):
  for sc in str:
    print '0x{:x}'.format(ord(sc))


C_ESC = "\x1b"
C_CRLF= "\r\n"
C_CR  = "\r"

CSI_SEQ = C_ESC + "["
OSC_SEQ = C_ESC + "]"
re_CSI_SEC0 = re.compile(CSI_SEQ+"[0-9]+[@A-GI-Z`a-eg-q\|\}\~]")
re_CSI_SEC1 = re.compile(CSI_SEQ+"[0-9]+\;[0-9]+[Hfsr]")
re_CSI_SEC2 = re.compile(CSI_SEQ+"[su]")
re_CSI_SEC3 = re.compile(CSI_SEQ+"\<[rs]")
re_CSI_SEC4 = re.compile(CSI_SEQ+"[\=\>][0-9]+[ts]")
re_CSI_SEC5 = re.compile(CSI_SEQ+"\>3\;[0-9]+\;[0-9]+\;[0-9]+\;[0-9]+J")
re_CSI_SEC6 = re.compile(CSI_SEQ+"\>3\;[0-9]+\;[0-9]+K")
re_CSI_SEC7 = re.compile(CSI_SEQ+"\>5\;[0-9]+K")
re_CSI_SEC8 = re.compile(CSI_SEQ+"\?[0-9]+[JKhiln]")
re_CSI_SEC9 = re.compile(CSI_SEQ+"[0-9]+ q")
re_CSI_SEC10= re.compile(CSI_SEQ+"[0-9]+\;[0-9]+\"p")
re_CSI_SEC11= re.compile(CSI_SEQ+"[0-9]+\"q")
re_OSC_SEC0 = re.compile(OSC_SEQ+"[0-9]+\;\S")
re_OSC_SEC1 = re.compile(OSC_SEQ+"[0-9]+\;\~")


#str_dump(CSI_SEQ)
#print '{} {}'.format(CSI_SEC, "test")

for line in sys.stdin:
   temp_str = re.sub(re_CSI_SEC0,'',line)
   temp_str = re.sub(re_CSI_SEC1,'',temp_str)
   temp_str = re.sub(re_CSI_SEC2,'',temp_str)
   temp_str = re.sub(re_CSI_SEC3,'',temp_str)
   temp_str = re.sub(re_CSI_SEC4,'',temp_str)
   temp_str = re.sub(re_CSI_SEC5,'',temp_str)
   temp_str = re.sub(re_CSI_SEC6,'',temp_str)
   temp_str = re.sub(re_CSI_SEC7,'',temp_str)
   temp_str = re.sub(re_CSI_SEC8,'',temp_str)
   temp_str = re.sub(re_CSI_SEC9,'',temp_str)
   temp_str = re.sub(re_CSI_SEC10,'',temp_str)
   temp_str = re.sub(re_CSI_SEC11,'',temp_str)
   temp_str = re.sub(re_OSC_SEC0,'',temp_str)
   temp_str = re.sub(re_OSC_SEC1,'',temp_str)
   temp_str = re.sub(C_CRLF,'\n',temp_str)
   temp_str = re.sub(C_CR,'\n',temp_str)
   print temp_str,

