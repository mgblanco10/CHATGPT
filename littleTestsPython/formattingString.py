# formatting strings example
name = "Manny"
number = len(name)*3
print("Hello {}, your lucky number is {}".format(name,number))

# ##Otra forma
print("Your lucky number is {number}, {name}".format(name=name, number=len(name)*3))

#  #### antes
greeting = "Hello " + name + ", your lucky number is " + str(number)
print(greeting)

# example
price= 7.5
                ### tasa impositiva del 9%
with_tax = price * 1.09 
print(price, with_tax)
               ### dos decimales (2 números flotantes)
print("Base price: ${:.2f}. With tax: ${:.2f}.".format(price, with_tax))

### otro example
def to_celsius(x):
    return (x-32)*5/9

for x in range (0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))

