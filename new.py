class Parrot:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sing(self,song):
        return f"{self.name} is singing a song called {song} "

    def dance(self):
        return f"{self.name} is dancing"


blu=Parrot('blu',10)
red=Parrot('red',15)

print(blu.sing('happy'))
print(red.dance())