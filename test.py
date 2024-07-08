class Monster:
    def __init__(self, name="Mike", number_of_teeth=0, color="blue"):
        self.name = name
        self.number_of_teeth = number_of_teeth
        self.color = color

    def __str__(self):
        return f"{self.name} ({self.number_of_teeth}) {self.color}"

    def is_scary(self):
        return self.number_of_teeth > 16 or self.color == "red"

    @staticmethod
    def define_scary_monsters(monsters):
        scary_monsters = []
        for monster in monsters:
            if monster.is_scary():
                scary_monsters.append(monster)
        return scary_monsters

# Example usage:
# monster1 = Monster("Mike", 20, "blue")
# monster2 = Monster("Sulley", 10, "red")
# monsters = [monster1, monster2]
# scary_monsters = Monster.define_scary_monsters(monsters)
# for monster in scary_monsters:
#     print(monster)
