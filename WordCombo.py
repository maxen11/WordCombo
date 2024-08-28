from itertools import permutations

from english_words import get_english_words_set
web2lowerset = get_english_words_set(['web2'], lower=True)
inp=input("Enter characters:\n").lower()#"ergni"
print("\nWords:")

word_set=set()
for i in range(4,len(inp)):
    if i > len(inp):
        break
    for p in list(permutations(inp,i)):
        word="".join(p)
        if word in web2lowerset and word not in word_set:
            print("".join(p)," ", end='') # Multiple words per line
            #print(word) # One word per line
            word_set.add(word)
