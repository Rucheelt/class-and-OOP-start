class parrot:
    def _init_(self,name,age):  #instance attri
        self.name=name
        self.age=age
    
    def sing(self,song):
        print(f" the { self.name} sings {song}")
    def dance(self,music):
        print(f"the dance is for {music}")

p=parrot("abc",10)
p.sing("christmas")
p.dance("jazz")