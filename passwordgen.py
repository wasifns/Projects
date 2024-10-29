#Password Generator Project
import random
let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sym = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#this is the data for generating passwords 

print("This is PyPassword Generator!")
nr_let= int(input("How many letters would you like in your password?\n")) 
nr_sym= int(input(f"How many symbols would you like?\n"))
nr_num= int(input(f"How many numbers would you like?\n"))

list_rand_let=[]
list_rand_sym=[]
list_rand_num=[]
list_rand=[list_rand_let, list_rand_sym, list_rand_num]

#for random letters
for letters in let:
    list_rand_let.append(random.choice(let))
    if len(list_rand_let)==nr_let:
        break

#for random symbols
for symbol in sym:
    list_rand_sym.append(random.choice(sym))
    if len(list_rand_sym)==nr_sym:
         break
    
#for random numbers
for numbers in num:
    list_rand_num.append(random.choice(num))
    if len(list_rand_num)==nr_num:
        break

list_pass=list_rand_let+list_rand_sym+list_rand_num

# randomize password order 
random.shuffle(list_pass)

# covert list into string
def listostr(list_pass):
    # initialise empty string
    str=""
    # traverse in the string
    for ele in list_pass:
        str+=ele
    # return string
    return str

password=listostr(list_pass)
print(password)
