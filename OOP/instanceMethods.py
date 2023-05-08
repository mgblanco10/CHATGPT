class Piglet:
    def speak(self):
        print("oink oink")

hamlet = Piglet()
hamlet.speak()

class _Piglet:
    name = 'piglet'
    def speak(self):
        print("oink! I'm {}! Oink!".format(self.name))

hamlet = _Piglet()
hamlet.name = "Hamlet"
hamlet.speak()

petunia = _Piglet()
petunia.name = "Petunia"
petunia.speak()

class Piglet:
    years = 0
    def pig_years(self):
        return self.years * 18

piggy = Piglet()
print(piggy.pig_years())

piggy.years = 2
print(piggy.pig_years())


class Dog:
  years = 0
  def dog_years(self):
    return self.years * 7
    
fido=Dog()
fido.years=3
print(fido.dog_years())
