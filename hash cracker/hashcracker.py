# CREATED BY: webbigamer
# DISCORD: https://discord:gg/sdDBjkzjFY
# GITHUB: https://github.com/webbigamer
# YOUTUBE: https://www.youtube.com/channel/UCBY_L4LY2xQHNWSO1wzWJSA
# !DISCLAIMER! this will find the suspects password and if they know you might get aressted for it!

print ("""hashcracker v1
created by: webbigamer
please wait...
""")

import hashlib

flag = 0
counter = 0

pass_hash = input("enter md5 hash: ")

wordlist = input("wordlist file name: ")

try:
    pass_file = open (wordlist, "r")
except:
    print("no file found")
    quit()

for word in pass_file:
    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    #print(word) #if you want to see the progress remove the "#" from "print(word)"
    #print(digest) #if you want to see the progress remove the "#" from "print(digest)"
    #print(pass_hash) #if you want to see the progress remove the "#" from "print(pass_hash)"
    counter += 1

    if digest == pass_hash
       print("hash craked")
       print("cracked password: " + word)
       print("you can now close the window")
       flag = 1
       break
    if flag == 0:
        print("hash could not be craked (the password was not in the wordlist)")
        print("you can now close the window")
        print("""######  #
                 # g  #  #
                 ######  #
                      #  #####
                 #    #  # b #
                 ######  #####""")
