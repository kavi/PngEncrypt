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
