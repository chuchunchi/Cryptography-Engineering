#!/bin/python

import string
import math
import random

def create_cipher_dict(key):
    cipher_dict = {}
    alphabet_list = list(string.ascii_uppercase)
    for i in range(len(key)):
        cipher_dict[alphabet_list[i]] = key[i]
    #print(cipher_dict)
    return cipher_dict

def encrypt(text, key):
    cipher_dict = create_cipher_dict(key)
    text = list(text)
    newtext = ""
    for elem in text:
        if elem.upper() in cipher_dict:
            newtext += cipher_dict[elem.upper()]
        else:
            newtext += " "
    return newtext

# This function takes input as a path to a long text and creates scoring_params dict which contains the
# number of time each pair of alphabet appears together
# Ex. {'AB':234,'TH':2343,'CD':23 ..}
# Note: Take whitespace into consideration

def create_scoring_params_dict(longtext_path):
    #TODO
    dict={}
    with open(longtext_path,'r',encoding="utf-8") as f:
        cipher_text = f.read()
    cipher_text = cipher_text.upper()
    for ind in range(len(cipher_text)-1):
        if (cipher_text[ind].isalpha() or cipher_text[ind]==" ") and (cipher_text[ind+1].isalpha() or cipher_text[ind+1]==" "):
            bi = cipher_text[ind]+cipher_text[ind+1]
            if bi in dict:
                dict[bi]+=1
            else:
                dict[bi]=1
    #print(dict)
    return dict
    

# This function takes input as a text and creates scoring_params dict which contains the
# number of time each pair of alphabet appears together
# Ex. {'AB':234,'TH':2343,'CD':23 ..}
# Note: Take whitespace into consideration

def score_params_on_cipher(text):
    #TODO
    dict={}
    text = text.upper()
    for ind in range(len(text)-1):
        if (text[ind].isalpha() or text[ind]==" ") and (text[ind+1].isalpha() or text[ind+1]==" "):
            bi = text[ind]+text[ind+1]
            if bi in dict:
                dict[bi]+=1
            else:
                dict[bi]=1
    #print(dict)
    return dict

# This function takes the text to be decrypted and a cipher to score the cipher.
# This function returns the log(score) metric

def get_cipher_score(text,cipher,scoring_params):
    #TODO
    plain_t = encrypt(text, cipher)
    cipher_score = score_params_on_cipher(plain_t)
    score=0
    for bi,num in cipher_score.items():
        if bi in scoring_params:
            score += num*(math.log(scoring_params[bi]))
    return score


# Generate a proposal cipher by swapping letters at two random location
def generate_cipher(cipher):
    #TODO
    ran1=random.randint(0, len(cipher)-1)
    ran2=random.randint(0, len(cipher)-1)
    cipher2 = [i for i in cipher]
    cipher2[ran1]=cipher[ran2]
    cipher2[ran2]=cipher[ran1]
    return cipher2

# Toss a random coin with robability of head p. If coin comes head return true else false.
def random_coin(p):
    #TODO
    temp_p = random.random()
    if temp_p>p :
        return False
    else:
        return True

# Takes input as a text to decrypt and runs a MCMC algorithm for n_iter. Returns the state having maximum score and also
# the last few states
def MCMC_decrypt(n_iter,cipher_text,scoring_params):
    current_cipher = string.ascii_uppercase # Generate a random cipher to start
    best_state = ''
    score = 0
    for i in range(n_iter):
        proposed_cipher = generate_cipher(current_cipher)
        score_current_cipher = get_cipher_score(cipher_text,current_cipher,scoring_params)
        score_proposed_cipher = get_cipher_score(cipher_text,proposed_cipher,scoring_params)
        try:
            acceptance_probability = min(1,math.exp(score_proposed_cipher-score_current_cipher))
        except OverflowError:
            acceptance_probability=1
        if score_current_cipher>score:
            best_state = current_cipher
        if random_coin(acceptance_probability):
            current_cipher = proposed_cipher
        if i%500==0:
            print("iter",i,":",encrypt(cipher_text,current_cipher)[0:99])
    return best_state

def main():
    ## Run the Main Program:
        
    scoring_params = create_scoring_params_dict('war_and_peace.txt')

    with open('ciphertext.txt','r') as f:
        cipher_text = f.read()
    print(cipher_text)

    print("Text To Decode:", cipher_text)
    print("\n")
    best_state = MCMC_decrypt(10000,cipher_text,scoring_params)
    print("\n")
    plain_text = encrypt(cipher_text,best_state)
    print("Decoded Text:",plain_text)
    print("\n")
    print("MCMC KEY FOUND:",best_state)

    with open('plaintext.txt','w+') as f:
        f.write(plain_text)


if __name__ == '__main__':
    main()
