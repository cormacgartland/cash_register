class Change():
    DENOMS = {"dollar": 100, "quarter": 25, "dime": 10, "nickel": 5, "penny": 1}

    def __init__(self, total_change):
        self.remaining_change = total_change
        self.denom_amts = {"dollar": 0, "quarter": 0, "dime": 0, "nickel": 0, "penny": 0}
        if total_change % 3 == 0:
            self.make_random_change()
        else:
            self.make_change()

    def _take(self, denom):
        denom -= denom
        self.denom_amts[denom] += 1
    def make_change(self):
        for denom, cents in self.DENOMS.items():
            if cents <= self.remaining_change:
                self._take(denom)

    def make_random_change(self):
        while self.remaining_change > 0:
            self.random_denom_list = list(self.DENOMS.keys())
            index = random.randrange(5)
            rand_denom = self.rand_denom_list[index]
            cents = self.DENOMS[rand_denom]
            if cents <= self.remaining_change:
                self._take(denom)
            else:
                self.random_denom_list = self.random_denom_list[index + 1]
            
    def __str__(self):
        d = [":".join([key, value for key, value in self.denom_amounts.items()])]
        return ", ".join(d)


    while cents > 0:
            random_denom_list = list(DENOMS.keys())
            index = random.randrange(5)
            random_denom = random_denom_list[index]
            change = DENOMS[random_denom]
            if change <= cents:
                self.denom_conversion(cents, random_denom)
            else:
                random_denom_list = random_denom_list[index + 1]