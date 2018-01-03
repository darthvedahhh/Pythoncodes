#Python prgram to find first recurring string in python


str=' '
for i in  range(len(str)):
    x = str[i]

    if x in str[i+1:]:
        print(x)
        print(str[i])
        break
    else:
        x=str[i]



