class SuperHero:
    def __init__(self, real_name, abilities, alias):
        self.real_name = real_name
        self.abilities = abilities
        self.alias = alias

    def __str__(self):
        return f"Superhero {self.alias} also known as {self.real_name}"