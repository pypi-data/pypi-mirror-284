#!/usr/bin/env python3
# -*-coding:UTF-8 -*

from math import*
import k_general_kit.gen_func
from k_general_kit.gen_func import*
import k_general_kit.gen_obj
from k_general_kit.gen_obj import*
import k_general_kit.search_sort.search_sort
from k_general_kit.search_sort.search_sort import*
import k_general_kit.eval_sequence
from k_general_kit.eval_sequence import*

print("Welcome! This program aims to eval easily some expressions using objets of the modules : 0-math, 1-gen_func, 2-search_sort, 3-gen_obj 4-eval_sequence.")
Modules = ('math', 'k_general_kit.gen_func', 'k_general_kit.search_sort', 'k_general_kit.gen_obj', 'k_general_kit.eval_sequence')

Helps = input("\nIf you want help on at least one of these modules, enter the corresponding number(s) by separating them with a comma. Ex: 0,1 : ")

if Helps.strip() != '':
	Helps = Helps.split(',')
	try:
		for i in Helps:
			print('')
			print(help(Modules[int(i)]))
	except:

		
		print("Invalid input!")
		
while True:
	expression = input("\nEnter the expression to eval (Ex: nel(2)) (An empty input stop the entry process) : ")
	if expression.strip() == '':
		break
	print('')
	answer = eval(expression)
	if answer != None:
		print(f"{expression} = {answer}.")
	bool = input("\nAgain ? (y or n) : ").lower()
	if bool != 'y':
		break
	
input("Glad to have served you! Press 'Enter' to quit.")
