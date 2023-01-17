def findPairs(my_numbers, ex_sum):
    my_new = []                     #empty list
    list_size = len(my_numbers)     #check length of list to enable binary search
    for i in range (0, list_size - 1) :  #loop from back to forward
        for n in range (i + 1, list_size):  #loop from forward to back
            if (my_numbers[i] + my_numbers[n] == ex_sum) : #condition is set
            
                my_new.extend((my_numbers[i],my_numbers[n]))
                
                break                                 #if condition is not met, step out of loop
    else:
        print(my_new)
            

#test
my_numbers = [0,2,3,4,5,6]
ex_sum = 12

findPairs(my_numbers,ex_sum)
    
def find_longest_word(words_list):  
    word_len = []  
    for n in words_list:  
        word_len.append((len(n), n))  
    word_len.sort()  
    return word_len[-1][1]  

print(find_longest_word(["hasta ", "lavista", "baby"])) 


def find_longest_word(text):
    longest_word = max(text.split(), key = len)
    return longest_word, len(longest_word)
    
find_longest_word(["hasta ", "lavista", "baby"])