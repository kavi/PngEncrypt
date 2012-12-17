#!/usr/bin/python
from bitstring import BitArray, BitStream
import hashlib
import Image
import sys
from util import getKey, getImageData


def getText(file):
  text = open(file, "rb").read()
  return text

def loadImage(input, output, text, key):
  img = Image.open(input)

  # TODO - assert RGB/RGBA
  print img.mode

  #text = "Hello World!"
  bits = BitArray(bytes=text)
  lbits = BitArray(hex(bits.len))
  lbits.prepend(32 - lbits.len)
  print text
  print bits.bin
  print lbits.bin
#  print bits[1] & 1
  data = img.getdata()
#  print len(data)

  counter = 0
  newdata = []
  for i in data:
    c = counter - lbits.len
    p = counter % len(key)
    if (counter < lbits.len):
      q = (key[p] ^ (lbits[counter] & 1))
      newdata.append((i[0] ^ q,i[1],i[2],255))
    elif (c < bits.len):
      q = (key[p] ^ (bits[c] & 1))
#      print "q:" + str(q) + " ,i:" + str(i[0]) + " ,i ^ q:" + str(i[0] ^ q)
      newdata.append((i[0] ^ q,i[1],i[2],255))
    else:
      newdata.append((i[0],i[1],i[2],255))
    counter += 1

#  for i in newdata:
#    print i
  img.putdata(newdata)
  img.save(output)
 
def main(argv):
  pw  = argv[0]
  txtfile = argv[1]
  inputImage = argv[2]
  outputImage = argv[3]

  key = getKey(pw)  
  text = getText(txtfile)

  print "Input img: " + inputImage
  print "Output img: " + outputImage
  print "Text: " + text
  print "pass: " + pw
  print "Key: " + key.hex

  loadImage(inputImage,outputImage,text,key)

if __name__ == "__main__":
   main(sys.argv[1:])  
