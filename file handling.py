try:
    print(a)
except NameError:
    print("a is not defined")
except:
    ("Something is not working")
'''x =5/0
print(x)'''
try:
    a = x/y
except ZeroDivisionError:
    print("denominator ca't be zero")
except:
    print("hello world")
try:
    print(a)
except:
    print("a is not defined")
finally:
    print("No one can stop me")
try:
    f = open("dummy.txt")
    try:
        f.write("Hello Class")
    except:
        print("Error during writting")
    finally:
        f.close()
except:
    print("Error in opening file")
try:
    print("Hello Class")
except:
    print("Error")
else:
    print("Working")
    
f1 = open("cipherschools.jpg","rb")
f2 = open("NEVER GIVE UP.jpg","wb")
for x in f1:
    f2.write(x)
