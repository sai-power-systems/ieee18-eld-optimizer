package eld_lambda;

/**
 * Calculator class for performing Lambda Iteration-based
 * Economic Load Dispatch (ELD).
 *
 * Assumes generator cost function:
 *
 *      F(P) = a + bP + cP²
 *
 * Incremental cost:
 *
 *      dF/dP = b + 2cP
 *
 * At optimum:
 *
 *      λ = b + 2cP
 *
 * Therefore:
 *
 *      P = (λ - b) / (2c)
 */
public class ELDCalculator {

    private float lambda;
    private Generator[] genArray;
    private int numGenerators;
    private float totDemand;
    private float tolerance;
    private int maxIterations;

    /**
     * Constructor
     *
     * @param numGenerators Number of generators
     * @param genArray Array of eld_lambda.Generator objects
     * @param totDemand Total system demand (MW)
     */
    public ELDCalculator(int numGenerators,
                         Generator[] genArray,
                         float totDemand) {

        this.lambda = 0f;
        this.genArray = genArray;
        this.numGenerators = numGenerators;
        this.totDemand = totDemand;

        // Accuracy requirement
        this.tolerance = 0.001f;

        // Maximum number of iterations
        this.maxIterations = 100;
    }

    /**
     * Performs Lambda Iteration using binary search.
     *
     * @return Optimal generator dispatch powers
     */
    public float[] lambdaIteration() {

        float[] P = new float[numGenerators];

        /*
         * Determine lower and upper bounds for lambda
         * from generator characteristics.
         */
        float lambdaMin = Float.MAX_VALUE;
        float lambdaMax = Float.MIN_VALUE;

        for (int i = 0; i < numGenerators; i++) {

            Generator g = genArray[i];

            float minLambda =
                    g.getB()
                            + 2 * g.getC() * g.getMin_capacity();

            float maxLambda =
                    g.getB()
                            + 2 * g.getC() * g.getMax_capacity();

            lambdaMin = Math.min(lambdaMin, minLambda);
            lambdaMax = Math.max(lambdaMax, maxLambda);
        }

        int iteration = 0;

        while (iteration < maxIterations) {

            // Binary-search midpoint
            lambda = (lambdaMin + lambdaMax) / 2.0f;

            float totalPower = 0.0f;

            // Calculate generator outputs
            for (int i = 0; i < numGenerators; i++) {

                float b = genArray[i].getB();
                float c = genArray[i].getC();

                // Economic dispatch formula
                P[i] = (lambda - b) / (2 * c);

                // Enforce generator limits
                P[i] = genArray[i].validatePower(P[i]);

                totalPower += P[i];
            }

            float error = totalPower - totDemand;

            // Convergence test
            if (Math.abs(error) <= tolerance) {

                System.out.println(
                        "\n✅ Economic Load Dispatch Converged");
                System.out.printf(
                        "Lambda = %.5f%n",
                        lambda);

                for (int i = 0; i < numGenerators; i++) {
                    System.out.printf(
                            "eld_lambda.Generator %d Output = %.3f MW%n",
                            genArray[i].getGen_id(),
                            P[i]);
                }

                System.out.printf(
                        "Total Generated Power = %.3f MW%n",
                        totalPower);

                return P;
            }

            /*
             * Binary search update:
             *
             * If generated power is too small,
             * increase lambda.
             *
             * If generated power is too large,
             * decrease lambda.
             */
            if (totalPower < totDemand) {
                lambdaMin = lambda;
            } else {
                lambdaMax = lambda;
            }

            iteration++;
        }

        System.out.println(
                "\n⚠️ Maximum iterations reached.");

        System.out.printf(
                "Last Lambda Value = %.5f%n",
                lambda);

        return P;
    }
}

