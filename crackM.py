import hashlib

print('''created by webbi
                      _    __  __ 
                     | |  |  \/  |
   ___ _ __ __ _  ___| | _| \  / |
  / __| '__/ _` |/ __| |/ / |\/| |
 | (__| | | (_| | (__|   <| |  | |
  \___|_|  \__,_|\___|_|\_\_|  |_|
                                  
                                  
''')

wlist=input("enter wordlist directory: ")
hash2crack=input("enter hash [MD5]: ")

wlistlines=open(wlist, "r").readlines()

for i in range(0, len(wlistlines)):
    hash2comp=hashlib.md5(wlistlines[i].replace("\n","").encode()).hexdigest()
    if hash2crack == hash2comp:
        print("hash cracked: "+wlistlines[i].replace("\n",""))
        exit()
print("hash was not cracked try using another wordlist")
print("2/3 tries")

print('''created by webbi
                      _    __  __ 
                     | |  |  \/  |
   ___ _ __ __ _  ___| | _| \  / |
  / __| '__/ _` |/ __| |/ / |\/| |
 | (__| | | (_| | (__|   <| |  | |
  \___|_|  \__,_|\___|_|\_\_|  |_|
                                  
                                  
''')

wlist=input("enter wordlist directory: ")
hash2crack=input("enter hash [MD5]: ")

wlistlines=open(wlist, "r").readlines()

for i in range(0, len(wlistlines)):
    hash2comp=hashlib.md5(wlistlines[i].replace("\n","").encode()).hexdigest()
    if hash2crack == hash2comp:
        print("hash cracked: "+wlistlines[i].replace("\n",""))
        exit()
print("hash was not cracked try using another wordlist")
print("1/3 tries")

print('''created by webbi
                      _    __  __ 
                     | |  |  \/  |
   ___ _ __ __ _  ___| | _| \  / |
  / __| '__/ _` |/ __| |/ / |\/| |
 | (__| | | (_| | (__|   <| |  | |
  \___|_|  \__,_|\___|_|\_\_|  |_|
                                  
                                  
''')

wlist=input("enter wordlist directory: ")
hash2crack=input("enter hash [MD5]: ")

wlistlines=open(wlist, "r").readlines()

for i in range(0, len(wlistlines)):
    hash2comp=hashlib.md5(wlistlines[i].replace("\n","").encode()).hexdigest()
    if hash2crack == hash2comp:
        print("hash cracked: "+wlistlines[i].replace("\n",""))
        exit()
print("hash was not cracked try using another wordlist")
print("failed 3 times try restarting the script")
exit()
