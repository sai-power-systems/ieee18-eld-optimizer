import matplotlib.pyplot as plt

from input_loader import InputLoader
from eld_calculator import ELDCalculator
from src.main.python import generator

inputL = InputLoader()
total_demand = 300
generators = inputL.sample_generators()   # <- need ()
eld = ELDCalculator(generators, 300)      # <- needs arguments

dispatch = eld.lambda_iteration()         # <

def plot_power_distribution(generators, dispatch):

    names = [f"G{g.gen_id}" for g in generators]

    plt.figure(figsize=(8, 5))

    plt.bar(
        names,
        dispatch,
        color="steelblue"
    )

    plt.title("Economic Load Dispatch")
    plt.xlabel("eld_lambda.Generator")
    plt.ylabel("Power Output (MW)")
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.savefig("./data/power_output.jpg")
    plt.show()


def plot_cost_distribution(generators, dispatch):

    costs = [
        generators[i].calculate_cost(dispatch[i])
        for i in range(len(generators))
    ]

    names = [f"G{g.gen_id}" for g in generators]

    plt.figure(figsize=(8, 5))

    plt.bar(
        names,
        costs,
        color="orange"
    )

    plt.title("eld_lambda.Generator Operating Cost")
    plt.xlabel("eld_lambda.Generator")
    plt.ylabel("Cost")

    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.savefig("./data/cost_distribution.jpg")
    plt.show()


def plot_cost_curves(generators):

    plt.figure(figsize=(10, 6))

    for g in generators:

        power_range = range(
            g.min_cap,
            g.max_cap + 1,
            5
        )

        costs = [
            g.calculate_cost(p)
            for p in power_range
        ]

        plt.plot(
            power_range,
            costs,
            label=f"G{g.gen_id}"
        )

    plt.title("eld_lambda.Generator Cost Curves")
    plt.xlabel("Power Output (MW)")
    plt.ylabel("Operating Cost")
    plt.grid(True)
    plt.legend()
    plt.savefig("./data/cost_curve.jpg")
    plt.show()




def plot_convergence(eld3, demand):

    iterations = list(range(len(eld3.power_history)))

    plt.figure(figsize=(10, 6))

    plt.plot(
        iterations,
        eld.power_history,
        marker='o',
        linewidth=2,
        label='Generated Power'
    )

    plt.axhline(
        y=demand,
        color='red',
        linestyle='--',
        label=f'Demand = {demand} MW'
    )

    plt.title("Lambda Iteration Convergence")
    plt.xlabel("Iteration")
    plt.ylabel("Total Generated Power (MW)")
    plt.grid(True)
    plt.legend()

    plt.savefig(
        "./data/convergence_power.jpg",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

def plot_lambda_convergence(eld4):

    iterations = list(range(len(eld4.lambda_history)))

    plt.figure(figsize=(10, 6))

    plt.plot(
        iterations,
        eld.lambda_history,
        marker='s',
        color='green',
        linewidth=2
    )

    plt.title("Lambda Convergence")
    plt.xlabel("Iteration")
    plt.ylabel("Lambda")
    plt.grid(True)

    plt.savefig(
        "./data/lambda_convergence.jpg",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


plot_power_distribution(generators, dispatch)
plot_cost_distribution(generators, dispatch)
plot_cost_curves(generators)
plot_convergence(eld, total_demand)
plot_lambda_convergence(eld)