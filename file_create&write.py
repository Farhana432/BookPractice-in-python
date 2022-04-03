fp = open("text.txt", "w")
fp.write("hello  .I am Farhana!")
fp.close()
fp.write("hello again") #when close fp then get error if you execute a method or write
with open("test,txt", "w") as f:
    f.write("hello, python\n")
f
f.write("hello, python\n")
with open("test.txt", "w") as f:
    f.write("hello, python\n")

fp.write("this is a file")
fp.close()
type(fp)
fp