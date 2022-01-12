class publisher:
    def __init__(self,name):
        self.name=name
    def display1(self):
        print("Publisher:",self.name)
        
class book(publisher):
    def TA(self,title,author):
        self.title=title
        self.author=author
        
    def display1(self):
        print("Title:",self.title)
        print("Author:",self.author)
        
class python(book):
    def __init__(self,price,no_of_page,name):
        self.price=price
        self.no_of_page=no_of_page
        super().__init__(name)
    def display(self):
        print("Price:",self.price)
        print("No Of Pages:",self.no_of_page)

        
obj=python(1000,500,"Van Bossom")
obj.TA("Python","Van Bossom")
obj.display1()
obj.display()
    
