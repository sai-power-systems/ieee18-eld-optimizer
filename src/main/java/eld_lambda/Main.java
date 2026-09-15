/**
 * Main class to test the ELD Logic
 *
 * imports all the other modules and tests the application end to end
 */
package eld_lambda;

import java.util.*;
public class Main {

    public static ArrayList<Float> plot_cost_curve(Generator[] genlist,float[] power){
        ArrayList<Float> cost = new ArrayList<>();
        for (int i = 0; i < genlist.length; i++) {
            cost.add(genlist[i].calculateCost(power[i]));
        }

        

        return cost;
    }

    public static void main(String[] args) {

        // Create generator objects
        Generator[] generators = new Generator[3];

        generators[0] = new Generator(
                1,      // eld_lambda.Generator ID
                50,     // Min capacity
                200,    // Max capacity
                500f,   // a
                5.3f,   // b
                0.004f  // c
        );

        generators[1] = new Generator(
                2,
                50,
                150,
                400f,
                5.5f,
                0.006f
        );
        generators[2] = new Generator(
                3,
                50,
                100,
                200f,
                5.8f,
                0.009f
        );

        // Total system demand (MW)
        float totalDemand = 300f;

        // Create ELD calculator
        ELDCalculator eld =
                new ELDCalculator(generators.length,
                        generators,
                        totalDemand);

        // Run Lambda Iteration
        float[] dispatch = eld.lambdaIteration();

        // Display final dispatch values
        System.out.println("\n--- Final Economic Load Dispatch ---");

        float totalGenerated = 0;

        for (int i = 0; i < dispatch.length; i++) {
            System.out.printf(
                    "eld_lambda.Generator %d Output = %.3f MW%n",
                    generators[i].getGen_id(),
                    dispatch[i]
            );
            totalGenerated += dispatch[i];
        }

        System.out.printf("Total Generated Power = %.3f MW%n",
                totalGenerated);
        System.out.printf("Total Demand = %.3f MW%n",
                totalDemand);


        ArrayList<Float> ff = plot_cost_curve(generators,dispatch);
        for (Float g : ff){
            System.out.println(g);
        }
    }
}