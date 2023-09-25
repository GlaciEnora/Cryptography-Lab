#SubByte Module

def gf_degree(a) :
 res = 0
 a >>= 1
 while (a != 0) :
   a >>= 1
   res += 1
 return res

def gf_invert(a, mod=0x1B) :
 v = mod 
 g1 = 1
 g2 = 0
 j = gf_degree(a) - 8

 while (a != 1) :
   if (j < 0) :
     a, v = v, a
     g1, g2 = g2, g1
     j = -j

   a ^= v << j
   g1 ^= g2 << j

   a %= 256  # Emulating 8-bit overflow
   g1 %= 256 # Emulating 8-bit overflow

   j = gf_degree(a) - gf_degree(v)

 return g1

def truxor(ran):
  ran = bin(ran).replace("0b", "")
  if len(ran) < 8: ran = ("0"*(8-len(ran)))+ran
  s = 0
  for i in range(8):
       s ^= int(ran[-1])
       ran = ran[:-1]
  return s
  
def shift(key):
   if key & 0x01:
      key >>= 1
      key ^= 0x80
      return key
   else:
      return key>>1

def sbox(a):
   b = gf_invert(a)
   k = hex(b)
   if len(k) == 3:
      k = k[:2] + "0" + k[-1]
   y = k[-1]
   x = k[-2]
   b = int(y + x, 16)
   bytebox = 0b10001111
   cons = 0x63
   s = ""
   for i in range(8):
       s = str(truxor(bytebox & b)) + s
       bytebox = shift(bytebox)
   return (int(s[::-1], 2) ^ cons)

def invsbox(b):
  k = hex(b)
  if len(k) == 3:
      k = k[:2] + "0" + k[-1]
  y = k[-1]
  x = k[-2]
  b = int(y + x, 16)
  bytebox = 0b00100101
  cons = 0x05
  s = ""
  for i in range(8):
      s = str(truxor(bytebox & b)) + s
      bytebox = shift(bytebox)
  temp = (int(s[::-1], 2) ^ cons)
  return gf_invert(temp)

print(sbox(0x95), invsbox(0x2A))