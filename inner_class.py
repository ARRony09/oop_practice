class Color:
    def __init__(self):
        self.name='Green'
        self.lg=self.Lightgreen()
    
    def show(self):
        return f"Name is, {self.name}"

    class Lightgreen:
        def __init__(self):
            self.name="Light Green"
            self.code="024avc"
        
        def display(self):
            print("Name",self.name)
            print("Code",self.code)

outer=Color()
print(outer.show())

lg=outer.lg
lg.display()

