names = ["Alaa", "Mariam", "Heba", "Mona"]
names.sort()

my_dict = {}

for name in names:
    f_letter = name[0].upper()
    
    if f_letter not in my_dict:
        my_dict[f_letter] = [name]  
    else:
        my_dict[f_letter].append(name) 

print(my_dict)