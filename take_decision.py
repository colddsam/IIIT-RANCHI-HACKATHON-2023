import collect_image as ci
char=input("enter the character to update the dataset : ")
if not len(char)==1:
    print("enter one single character")
else:
    ci.update__dataset(char)