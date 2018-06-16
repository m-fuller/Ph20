import math
import random

def isPrime(n):
    return (all(n%i!=0 for i in range(2,int(math.sqrt(n))+1)))

def lcm(x,y):
    return int((x*y)/(math.gcd(x,y)))
 
# Calculate the modular multiplicative inverse given e and lambda_n       
def modMultInv(e,lam_n):
    for i in range(1,lam_n):
        if i*e % lam_n == 1:
            return i
        
def generateKey():
    # 64 to 256 -> 6 to 8 bits   
    primes = [i for i in range(64,256) if isPrime(i)] 
    p = random.choice(primes)
    q = random.choice(primes)
    n=p*q
    lam_n=lcm(p-1,q-1)
    # generate a list of possible values of e
    poss_e = [i for i in range(1,lam_n) if math.gcd(i,lam_n)==1]
    e = random.choice(poss_e)
    d = modMultInv(e,lam_n)
    return (n,d,e)

def encryption(m,pubKey):
    (n,e)=pubKey
    c = pow(m,e,n) #(m**e)%n
    return c
   
def decryption(c,privKey):
    (n,d)=privKey
    retreived_m=(c**d)%n
    return retreived_m

# This collision attack calls the encryption function for all possible values
# of m and checks what return values are equivalent to c.   
def collision_attack(m,pubKey):
    (n,e)=pubKey
    poss_m=[]
    c = encryption(m,pubKey)
    # 65536 is the max value for n if p and q are 8 bits or less
    for i in range(65536): 
        if encryption(i,pubKey) == c:
            poss_m.append(i)
    print('Possible values of m are: {}'.format(poss_m))
    
keyGen = generateKey()
privateKey=(keyGen[0],keyGen[2])
publicKey=(keyGen[0],keyGen[1])
m = random.randint(0, keyGen[0])

print('m = {}'.format(m))
print('Public key is: (n,e) = ({},{})'.format(publicKey[0],publicKey[1]))
print('Private key is: (n,d) = ({},{})'.format(privateKey[0],privateKey[1]))
print('c = {}'.format(encryption(m,privateKey)))
print('decrypted m = {}'.format(decryption(encryption(m,privateKey), publicKey)))

collision_attack(m,publicKey)  