class Animal:
    def __init__(self, sound):
        self.sound = sound

    def identity(self):
        print(f'Inside Animal class, your voice is {self.sound}')

class Dog(Animal):
    def __init__(self, sound):
        super().__init__(sound)
        self.dog_sound = sound

    def make_sound(self):
        print(f'Dog sounds like {self.dog_sound}')

class Cat(Animal):
    def __init__(self, sound):
        super().__init__(sound)
        self.cat_sound = sound

    def make_sound(self):
        print(f'Cat sounds like {self.cat_sound}') 

if __name__ == '__main__':
    cat_obj = Cat('Meow...!')
    cat_obj.identity()
    cat_obj.make_sound()
