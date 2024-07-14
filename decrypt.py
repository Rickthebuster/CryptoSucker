for file in os.listdir():
    if file == 'Crypto$ucker.py' or file == 'thekey.key' or file == 'decrypt.py':
        continue
    if os.path.isfile(file):
        files.append(file)
key = Fernet.generate_key()
with open("thekey.key","rb") as key:
    decryptkey = key.read()
    for file in files:
    with open(file,"rb") as thefile:
        contents = thefile.read()
    decrypted_content = Fernet(decryptkey).decrypt(contents)

    with open(file, 'wb') as thefile:
        thefile.write(decrypted_content)
