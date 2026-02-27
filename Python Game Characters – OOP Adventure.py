class GameCharacter :
    def __init__(self, name ,health):
        self.name=name
        self.health=health
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} took {damage} damage and has {self.health} health left.")
    def heal(self, amount):
        self.health+= amount
        print(f"{self.name} healed {amount} health and now has {self.health} health.")
    def show(self):
            print(f'{self.name} has {self.health} health.')
class Warrior(GameCharacter)  :
     def attack(self):
      print(f"{self.name} attacks with a sword!")  
class mage(GameCharacter) :
        def cast_spell(self):
            print(f"{self.name} casts a powerful spell!")

w1 = Warrior("Aragorn", 100)
m1  = mage("Gandalf", 80)
w1.show()
w1.attack()
m1.show()
m1.cast_spell()
          


