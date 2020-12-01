def area(a,b):
    return a*b

print(area(2,2)) #non-keyword arguments
print(area(b=5,a=3)) #kewworf arguments

#Functions can have default parameters (e.g. coefficient):

def converter(feet, coefficient = 3.2808):
    meters = feet / coefficient
    return meters

print(converter(10))

#a function that find the mean of any number of arguments
def mean(*args):
    return sum(args)/len(args)
print(mean(1,2,3,4))



#a function with keyword agrumenta the mean of any number of arguments
def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get)

print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))
