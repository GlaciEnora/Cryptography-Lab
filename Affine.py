#Affine Cipher
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x
 
def modinv(a, m):
    gcd, x = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
 
 
# affine cipher encryption function
# returns the cipher text
def affine_encrypt(text, key):
    '''
    C = (a*P + b) % 26
    '''
    return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26)
                  + ord('A')) for t in text.upper().replace(' ', '') ])
 
 
# affine cipher decryption function
# returns original text
def affine_decrypt(cipher, key):
    '''
    P = (a^-1 * (C - b)) % 26
    '''
    return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))
                    % 26) + ord('A')) for c in cipher ])
 
 
# Driver Code to test the above functions
def main():
    text = "UBBAHKCAPJKX"
    for a in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
     for i in range(25):
            print(affine_decrypt(text, [a,i]))
            if affine_decrypt(text, [a,i]) == "AFFINECIPHER":
                result, x, y = affine_decrypt(text, [a,i]), a, i
    print("Decrypted text %s found with keys %d %d"%(result, x, y))

if __name__ == '__main__':
    main()
