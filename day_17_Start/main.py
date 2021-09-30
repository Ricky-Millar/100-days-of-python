class user:
    def __init__(self, num_of_legs, height, poopoo_index, name): #this function is ran whenever this class is given to a new variable.
        self.legnum = num_of_legs
        self.height = height          #It is standard to keep the inouts and the atribute with the same name
        self.poodex = poopoo_index    #But it dosnt really matter
        self.favfood = "choccy milk"  #default values can be set here
        self.name = name

    def grow_extra_leg(self): #the self thing, its like if im doing this to user1, user1 will grow a leg, user2, user 2 ect
        self.legnum += 1

    def steal_poopoo_index(self, user): #the self will input our info but the user bit means we can interact with other users
        user.poodex -= 1
        self.poodex += 1
        print(f'{self.name} STEALS DA POOPOO FROM {user.name}')

user1 = user(17, 6, 69, "charls") #creates a user1 from the user class using the initial paramiters
user2 = user(56, 7, 8008, "tangoman")

print(user1.legnum)
user1.grow_extra_leg()
print(user1.legnum)


print(user1.poodex)
print(user2.poodex)
user1.steal_poopoo_index(user2)
print(user1.poodex)
print(user2.poodex)