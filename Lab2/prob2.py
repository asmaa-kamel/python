string= input("Enter a string :")
char= input("Enter a letter :")


for i in range(len(string)):
    if string[i]==char:
        print(f"The lettee is at index : {i}")
        break
else :
    print("The string does not contain the letter.")
    