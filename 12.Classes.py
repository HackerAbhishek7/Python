# A tutorial on classes

class Planet:

    def __init__(self):
        self.name = "Earth"
        self.radius = 20000
        self.Gravity = 9.8
        self.Galaxy = 'Milky-Way'

galaxy = Planet()

print(galaxy.name)
print(galaxy.radius)
print(galaxy.Gravity)
