
class Dog():
  """Uma classe para modelar um cachorro"""

  def __init__(self, name, age):
    """Inicializa os atributos (variáveis)"""
    self.name = name
    self.age = age

  def sit(self):
    """Simula o comportamento de sentar"""
    print(self.name.title() + " is now sitting")

  def roll(self):
    print(self.name.title() + " is now rolled over")

my_dog = Dog('Simba', 3)

my_dog.sit()
my_dog.roll()
