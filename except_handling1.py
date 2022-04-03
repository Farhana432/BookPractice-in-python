import io


filename = "file.txt"
mode = "r"
def div(a,b):

    try:
        return a / b
    except ZeroDivisionError:
        print("Zero can't devided")


print(div(10,0))

print(div(4,2))

print("-" * 30)

try:
    with open(filename, mode) as fp:
        content = fp.read()
        print(content)


except FileNotFoundError:
    print(filename," not found.")


except io.unsupportedOperation:
    print("Are you sure?", filename, " is readable?")

except NameError:
    print("name", filename, "is not defined. Did you mean:", filename, "?",)

except SyntaxError:
    print("invalid syntax")

except AttributeError:
    print("unsupportedOperation. Did you mean:", io, "?")

except Exception as e:
    print(e)