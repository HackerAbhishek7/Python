# A tutorial on classes

class Planet:

    def __init__(self,name,radius,gravity,galaxy):
        self.name = name
        self.radius = radius
        self.Gravity = gravity
        self.Galaxy = galaxy

galaxy = Planet("Naboo",20000,6.2,'Hoth System')

print(galaxy.name)
print(galaxy.radius)
print(galaxy.Gravity)
