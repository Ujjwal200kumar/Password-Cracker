import hashlib
#https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/Ashley-Madison.txt
pass_filename = "C:/xampp/htdocs/myapp/training/Program.java/cyber/Ashley-Madison.txt"


#password = "bomer"
##password = "yomama"

##password = "2BNE(tm<"
password = "kjajaj"


enc_password = password.encode("utf-8")
password_hash = hashlib.md5(enc_password.strip()).hexdigest()
##print(password_hash)


pass_file = open(pass_filename, "r")

for word in pass_file:
    enc_word = word.encode("utf-8")
    enc_hash = hashlib.md5(enc_word.strip()).hexdigest()
    
    if password_hash == enc_hash:
        print("this three-letter agency has been hacked. The password was " + word)
        quit()
    
   
else:
    print("The three-letter agency has a strong password. ")    