from generator import Generator


class ELDCalculator:

    def __init__(self, generators, total_demand):
        self.generators = generators
        self.total_demand = total_demand
        self.tolerance = 0.001
        self.max_iterations = 100
        self.lambda_value = 0
        self.lambda_history = []
        self.power_history = []

    def lambda_iteration(self):

        n = len(self.generators)
        power = [0.0] * n

        lambda_min = float("inf")
        lambda_max = float("-inf")

        for g in self.generators:

            min_lambda = g.b + 2 * g.c * g.min_cap
            max_lambda = g.b + 2 * g.c * g.max_cap

            lambda_min = min(lambda_min, min_lambda)
            lambda_max = max(lambda_max, max_lambda)

        iteration = 0

        while iteration < self.max_iterations:

            self.lambda_value = (lambda_min + lambda_max) / 2

            total_power = 0

            for i, g in enumerate(self.generators):

                power[i] = (self.lambda_value - g.b) / (2 * g.c)

                power[i] = g.validate_power(power[i])

                total_power += power[i]

            self.lambda_history.append(self.lambda_value)
            self.power_history.append(total_power)

            error = total_power - self.total_demand

            print(
                f"Iter {iteration:3d} | "
                f"Lambda={self.lambda_value:.5f} | "
                f"Power={total_power:.3f}"
            )

            if abs(error) <= self.tolerance:

                print("\n✅ Economic Load Dispatch Converged")
                print(f"Lambda = {self.lambda_value:.5f}")

                for i, g in enumerate(self.generators):
                    print(
                        f"eld_lambda.Generator {g.gen_id} Output = "
                        f"Power {power} MW"
                    )

                print(
                    f"Total Generated Power = "
                    f"{total_power:.3f} MW"
                )

                return power

            if total_power < self.total_demand:
                lambda_min = self.lambda_value
            else:
                lambda_max = self.lambda_value

            iteration += 1

        print("⚠️ Maximum iterations reached")
        return power