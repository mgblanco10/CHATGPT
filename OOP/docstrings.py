#Docstring
def to_seconds(hours, minutes, seconds):
    """Returns the amount of seconds in the given hours, minutes, and seconds."""
    return hours*3600+minutes*60+seconds

# help(to_seconds)

class Person:
  def __init__(self, name):
    self.name = name
  def greeting(self):
    """Outputs a message with the name of the person"""
    print("Hello! My name is {name}.".format(name=self.name)) 

# help(Person.greeting)