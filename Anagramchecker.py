def CheckAnagram():

    a=input("Enter first string")
    a1=input("enter Second string")
    if "".join(sorted(a))=="".join(sorted(a1)):
        print("Two strings are anagram")
    else:
        print("No these are not anagrams")

    a = input('Want to check anagrams')


    if a=='Y':
        CheckAnagram()

CheckAnagram()


