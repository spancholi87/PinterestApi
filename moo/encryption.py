
#install it:
#pip install passlib

def set_password(raw_password):
    from passlib.hash import sha256_crypt
    print raw_password
    hash = sha256_crypt.encrypt(raw_password)
    return hash

def check_password(raw_password, hash):
    #print raw_password
    from passlib.hash import sha256_crypt
    value = sha256_crypt.verify(raw_password, hash)
    print value
    return value
	
if __name__ == '__main__':
    main()
