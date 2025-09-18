class Cat:
    def __init__(self, color, trait, gender_type):
        self.color = color
        self.trait = trait
        self.gender_type = gender_type

    def describe_cat(self):
        return f"{self.color} Cat, {self.trait}, {self.gender_type}"

first_cat = Cat("black", "needy", "female")

print(first_cat.color)
print(first_cat.trait)
print(first_cat.gender_type)