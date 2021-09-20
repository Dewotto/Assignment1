#Phonebook Module Script

print()

import Module_Data

#New Variables for List

contact1 = Module_Data.a
contact2 = Module_Data.b
contact3 = Module_Data.c
contact4 = Module_Data.d
contact5 = Module_Data.e

#Input

Search1 = (input("Who are you searching for today?"))

#Output

if Search1 == "contact1":
    print("Contact:" , contact1)

elif Search1 == "contact2":
    print("Contact:", contact2)

elif Search1 == "contact3":
    print("Contact:", contact3)

elif Search1 == "contact4":
    print("Contact:", contact4)

elif Search1 == "contact5":
    print("Contact:", contact5)

else:
    print("Contact does not exist")

print ("have a great day! :)")

