def twice(x):
    def square(x):
        return x*x
    return square(x)*square(x)
def quad(x):
    return twice(x)
print(quad(int(input("Enter the number to get the quad value:"))))