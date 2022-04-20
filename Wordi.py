#!/usr/bin/env python
# coding: utf-8

# In[40]:


from tqdm.notebook import tqdm 


# In[54]:


word_list = 'wlist_match11.txt' 
# word_list = 'wordlist.txt'
# word_list = 'words_alpha.txt'
# word_list = 'words.txt'


# In[55]:


with open(word_list) as file :
# with open('words_alpha.txt') as file :
    words = file.read()
words = words.lower().splitlines()
letters = [set(w) for w in words]


# In[56]:


letter_set = set(input("Enter your letters with a space : \n").split())
for letter in letter_set:
    assert len(letter) == 1
    
print("you're letters are:\n", letter_set)


# In[57]:


lengths = input("Enter the word lengths with a space : \n").split()
for num in lengths:
    assert num.isdigit()
lengths = [int(num) for num in lengths]
print("you're lengths are:\n", lengths)


# In[58]:


found_words = []
for word, let in tqdm(zip(words,letters)):
    if let.issubset(letter_set) and len(word) in lengths:
        found_words.append(word)


# In[59]:


message = ''
for l in lengths:
    message += f'\n\nWords with length {l} :\n'
    for w in found_words:
        if len(w)==l:
            message +=  w + ' ' 
print (message)


# In[ ]:




