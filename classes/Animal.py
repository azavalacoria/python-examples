from abc import ABC, abstractmethod
class Animal(ABC):
	"""docstring for ClassName"""
	@abstractmethod
	def walk(self):
		raise NotImplementedError('Needs to declare wakl method')

class Mamifero(Animal):
	"""docstring for Mamifero"""
	
	def walk(self, lengs):
		print('I walk in ', str(lengs), ' lengs')

class Fish(Animal):
	"""docstring for Pez"""
	
	def walk(self):
		print('Im swim!')

class Bird(Animal):
	"""docstring for Bird"""
	def fly():
		print("I'm flying")
		

dog = Mamifero()
dog.walk(4)

fish = Fish()
fish.walk()

bird = Bird()
bird.fly()