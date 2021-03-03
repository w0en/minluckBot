POWERTYPES = ['Arcane', 'Draconic', 'Forgotten', 'Hydro', 'Parental', 'Physical', 'Shadow', 'Tactical', 'Law', 'Rift']


class Mouse:

    def __init__(self, breed, group, power, minlucks, subgroup=None):
        self.breed = breed
        self.group = group
        self.subgroup = subgroup
        self.minlucks = list(map(lambda x: 999999 if x is None else int(x), minlucks))
        self.power = power
        self.minluck = min(self.minlucks)
        self.minluckPowerTypes = [POWERTYPES[index] for index, luck in enumerate(self.minlucks) if luck is not None and luck == self.minluck]

    def __repr__(self):
        return f"{self.breed} (Group: {self.group})"

    def __str__(self):
        return f"Breed: {self.breed}\nGroup: {self.group}\nSubgroup: {self.subgroup}\nPower: {self.power}\n" \
               f"Minluck: {self.minluck}\nMinluck Power Types: {self.minluckPowerTypes}"
