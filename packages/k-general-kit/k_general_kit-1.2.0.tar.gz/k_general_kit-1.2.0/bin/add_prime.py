#!/usr/bin/env python3
# -*-coding:UTF-8 -*

from k_general_kit.gen_func import paw
        
if paw("1234") == True:
    
    from pickle import Pickler, Unpickler

    with open("datas/prime/prime_numbers", "rb") as f:
        p = Unpickler(f)
        T = p.load()

    try:
        print("Welcome! This program aims to enrich the datas/prime/prime_numbers file")
        p = int(input("Précision : "))
    except:
        p = 0
        
    t = T[len(T)-1] + 1
    i = 0

    if p == 0:
        i = 1
    while i < p:
        j = t
        k = 2
        
        while k <= t/k:
            if t - (t//k)*k == 0:
                t += 1
                break
            k += 1
        
        if j == t:
            T.append(t)
            t += 1
            i += 1

    print(" [" + str(T[0]) + "..." + str(T[len(T)-1]) + "]")
    print(" Taille : " + str(len(T)))
      
    with open("datas/prime/prime_numbers", "wb") as f:
        p = Pickler(f)
        p.dump(T)

input("Glad to have served you! Press 'Enter' to quit.")
