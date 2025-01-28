


print(r"hello world \t something")

str1='hello'
str2=' world'
str3=str1+str2
print(str3)

print("length of string: ",len(str3))
print('1st character ',str3[0])
print('last character ',str3[-1])
print('from to end ',str3[0:6])
print('Remove every other ',str3[0:-1:2])
str3=str3.replace('hello','Hello')


print(str3)
print("Hello" in str3 )
print("Aell" not in str3 )
print('o index',str3.find('o'))

#strip
print("    long live  ".strip())
print("     long live".lstrip())
print("long live    ".rstrip())

print(",".join(["words","speak","talk"]))
print('long time no see'.split(' '))

int1=int2=5
str4=f"{int1} + {int2} = {int1+int2}"
print(str4)
print(f"{int1} + {int2} = {int1+int2}")

print("hello".upper())
print("HELLO".lower())
print("hello".capitalize())

#checking string or number digit
print('A number has 123'.isalnum())
print("helloe".isalpha())
print('2454a'.isdigit())
