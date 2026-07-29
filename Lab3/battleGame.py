
class character:
    def __init__(self,name,health):
        self.name=name
        self.health=health
        
    def attack(self,enemy):
        damage = 12
        enemy.take_damage(damage)
        return f"{self.name} attacks! {enemy.name} health -{damage} 💥💥"
        
    def take_damage(self,damage):
        self.damage=damage 
        self.health=self.health-damage  
        
    def is_alive(self):
        if self.health >0:
            return True
        else :
            return False
        
    
    
class warrior(character):
    def __init__(self,name,health,speed):
        super().__init__(name,health)
        self.speed=speed
        
    def attack(self, enemy):
        damage = 12
        enemy.take_damage(damage)
        return f"{self.name} attacks! {enemy.name} health -{damage} 💥💥"
    
class wizard(character):
    def __init__(self,name,health,spell):
        super().__init__(name,health)
        self.spell=spell
        
    def attack(self, enemy):
        damage = 15
        enemy.take_damage(damage)
        return f"{self.name} attacks! {enemy.name} health -{damage} 💥💥"
    
class archer(character):
    def __init__(self,name,health,accuracy):
        super().__init__(name,health)
        self.accuracy=accuracy
        
    def attack(self, enemy):
        damage = 13
        enemy.take_damage(damage)
        return f"{self.name} attacks! {enemy.name} health -{damage} 💥💥"
           
        
             
        
def battle(p1,p2):
    while p1.is_alive() and p2.is_alive():
        print(p1.attack(p2))
        print(f"{p2.name} health : {p2.health}")
        if p2.is_alive()==False:
            break
        print(p2.attack(p1))
        print(f"{p1.name} health : {p1.health}")
    if p1.is_alive() == False:
        print(f"""{p1.name} is dead ☠️ ☠️
        {p2.name} Wins The Game 🏆🏆
        """)
    else:
        print(f"""{p1.name} is dead ☠️ ☠️
            {p2.name} Wins The Match 🏆🏆
            """)   
           
characters = [
    warrior("Lee", 100, 20),
    wizard("Naruto", 90, "Rasingan"),
    archer("Coan", 85, 95)
]
          
battle(characters[0],characters[1])  

for i in characters:
    print(i.attack(characters[0]))          

