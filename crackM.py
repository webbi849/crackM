import hashlib

print('''created by webbi

         CCCCC  RRRRR     A      CCCCC   K  K    M     M
         C      R   R    A A     C       K K     M M M M
         CCCCC  RRRRR   A A A    CCCCC   K K     M  M  M
                R  R   A     A           K   K   M     M
                R   R
''')

wlist=input("enter wordlist: ")
hash2crack=input("enter hash: ")

wlistlines=open(wlist, "r").readlines()

for i in range(0, len(wlistlines)):
    hash2comp=hashlib.md5(wlistlines[i].replace("\n","").encode()).hexdigest()
    if hash2crack == hash2comp:
        print("hash cracked: "+wlistlines[i].replace("\n",""))
        exit()
print("hash was not cracked try using another wordlist")
print("exited")
