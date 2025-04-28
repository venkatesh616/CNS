import gnupg
gpg = gnupg.GPG()
recipient = 'harsh9@gmail.com'  # Or key fingerprint
message = "Hello, this is a confidential message sent via OpenPGP!"
encrypted_data = gpg.encrypt(message, recipients=[recipient], always_trust=True)
if encrypted_data.ok:
    print("\nEncrypted Message:")
    print(str(encrypted_data))
else:
    print("Encryption failed:", encrypted_data.status)
    exit()
encrypted_message = str(encrypted_data)
decrypted_data = gpg.decrypt(encrypted_message,passphrase='harsh9')
if decrypted_data.ok:
    print("\nDecrypted Message:")
    print(str(decrypted_data))
else:
    print("Decryption failed:", decrypted_data.status)
