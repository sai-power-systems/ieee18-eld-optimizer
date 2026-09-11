class Generator:

    def __init__(self, gen_id, min_cap, max_cap, a, b, c):
        self.gen_id = gen_id
        self.min_cap = min_cap
        self.max_cap = max_cap
        self.a = a
        self.b = b
        self.c = c

    def calculate_cost(self, power):
        return self.a + self.b * power + self.c * power * power

    def validate_power(self, power):
        if power < self.min_cap:
            return self.min_cap
        elif power > self.max_cap:
            return self.max_cap
        return power