from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import os
import ntpath

PATH_ENC = "encrypted/"
PATH_DEC = "decrypted/"

if not os.path.exists(PATH_ENC):
	os.makedirs(PATH_ENC)

if not os.path.exists(PATH_DEC):
	os.makedirs(PATH_DEC)

def pad(s):
	return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def encryptFiles(files, password, ui):
	for f in files:
		key = SHA256.new(password.encode()).digest()
		iv = Random.new().read(AES.block_size)
		cipher = AES.new(key, AES.MODE_CBC, iv)
		with open(f, 'rb') as f_read:
			content = f_read.read()
		with open(PATH_ENC + ntpath.basename(f) + '.cry', 'wb+') as f_write:
			ciphertext = cipher.encrypt(pad(content))
			f_write.write(iv + ciphertext)

	ui.resetButtonEnc()
	ui.files_encrpyt.clear()
	ui.selected_files_enc = []

def decryptFiles(files, password, ui):
	for f in files:
		if f.endswith(".cry"):
			key = SHA256.new(password.encode()).digest()
			with open(f, 'rb') as f_read:
				content = f_read.read()
				iv = content[:16]

			cipher = AES.new(key, AES.MODE_CBC, iv)
			with open(PATH_DEC + os.path.splitext(ntpath.basename(f))[0], 'wb+') as f_write:
				plainttext = cipher.decrypt(content[16:])
				f_write.write(plainttext.rstrip(b"\0"))

	ui.resetButtonDec()
	ui.files_decrpyt.clear()
	ui.selected_files_dec = []