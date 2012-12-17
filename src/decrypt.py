#!/usr/bin/python
from bitstring import BitArray, BitStream
import Image
import sys
import hashlib


def getKey(pw):
  sha = hashlib.sha1()
  sha.update(pw)
  key = BitArray(bytes=sha.digest())
  return key

def getImageData(image):
  img = Image.open(image)
  data = img.getdata()
  #print len(data)
  return data

def decrypt(data, key):
  # TODO - assert RGB/RGBA
  #print img.mode
  bits = BitArray()
  lbits = BitArray(32)

  counter = 0
  # Begin for
  for i in data:
    c = counter - lbits.len
    p = counter % len(key)
    q = key[p] ^ (i[0] & 1)
    # Begin if
    if counter < lbits.len:
      lbits[counter] = q
      # print "Decrypted: " + str(q) + ". Image: " + str(i[0])
    elif counter < lbits.int + 32:
      bits.append(1)
      bits[c] = q
    # end if
    counter += 1
  # end for
  #  print lbits.bin + " - " + str(lbits.int)
  return bits.bytes
# end def

def main(argv):
  pw = argv[0]
  inputfile = argv[1]
# print "Password: " + pw
#  print "Input image: " + inputfile

  key = getKey(pw)
#  print "Key: " + key.hex
  data = getImageData(inputfile)
  bytes = decrypt(data, key)
  print bytes

if __name__ == "__main__":
   main(sys.argv[1:])
