# K-General-Kit 🛠️

This project aims to provide a rich set of useful general functions frequently needed and frequent objects.

## Features 💡

* It contains a general library, for general functions on containiers, string, a bit of mathematics
* We also find a search_sort library, with powerful search and sort algorithms going from the sequential search to the exponential search and from the select sort to the merge sort.
* We also have the gen_obj library for frequents objects like math constants with the ability to ameliorate their precisions
* We also have eval_sequence, which gives powerful functions to evaluate recursive functions, bypassing the recursivity.
* Thera are also an interesting set of datas going from prime numbers collections to txt dictionnaries (for words counting functions).

## Examples of use 📝

```python
from k_general_kit.gen_func import all

print(nel(45)) # prints "quarante cinq"

print(words_sentence("Hello, everyone!", 'en')) # prints "['Hello', 'everyone']"


```

```python
import k_general_kit.search_sort as ks

tab = [1, 4, 0, -1, 8, 9]

tab_heap = ks.Heap(tab)

print(tab_heap.elements) # prints [-1, 0, 1, 4, 8, 9]

print(tab_heap) # Heap representation of tab before sorting

""" Result
       1 
     ↙   ↘   
   4       0 
  ↙ ↘     ↙ ↘  
-1   8   9 
"""

tab_heap.sort()

print(tab_heap) # Heap representation of tab after sorting

""" Result
      -1
     ↙   ↘   
   0       1 
  ↙ ↘     ↙ ↘  
 4   8   9 
"""
```

```python
import k_general_kit.search_sort as ks

tab = [1, 4, 0, -1, 8, 9]

ks.merge_sort(tab, start=0, end=-1, ord=1) # We sort tab in the descending order

print(tab) # Result: [9, 8, 4, 1, 0, -1]

ks.quick_sort(tab, start=0, end=-1, ord=0) # We sort tab in the ascending order

print(tab) # Result: [-1, 0, 1, 4, 8, 9]

print(ks.exp_search(0, tab, start=0, end=-1)) # We use exp_search since tab is now sorted, and which is better that dich_search for large tabs

""" Result: 1 """

print(ks.interpol_search(2, tab, start=0, end=-1)) # We use interpol_search since tab is now sorted and which is the best search algorithm for general tabs

""" Result: -1 """
```

For more tests, use in the project directory the command python -m tests.eval_func or the built-in command in .vscode

## Author ✍️

This project was created by KpihX. You can contact me at kapoivha@gmail.com for any questions or suggestions.

## License 📄

This project is licensed under the MIT license - see the LICENSE file for more details.

: https://github.com/KpihX
