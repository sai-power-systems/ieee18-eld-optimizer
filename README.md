<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script> 
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script>
  mermaid.initialize({ startOnLoad: true, theme: 'light' });
</script>



# ⚡ ELD Console Simulator {#mainpage}

Welcome to the documentation for the Economic Load Dispatch (ELD) Java console app.  
This tool models generator cost functions and dispatch logic for power systems.

## Equations

$$
P_i = \frac{lambda - b_i}{2*c_i}
$$

## Class diagram

```mermaid
classDiagram
    class eld_lambda.Generator {
        - int gen_id
        - float min_capacity
        - float max_capacity
        - float a
        - float b
        - float c
        + float validatePower(float power)
        + float getA()
        + void setA(float a)
        + float getB()
        + void setB(float b)
        + float getC()
        + void setC(float c)
    }
    
    class eld_lambda.InputLoader{
        + ArrayList<eld_lambda.Generator> loadFromUser()
    }
    
    class eld_lambda.ELDCalculator {
        - float lambda
        - eld_lambda.Generator[] genArray
        - float tot_demand
        - float tolerance
        - int max_iterations
        + float[] lambdaIteration()
    }

    eld_lambda.Generator <|-- eld_lambda.ELDCalculator : uses
    eld_lambda.Generator <|-- eld_lambda.InputLoader : uses
```


## Documentation
[View code documentation](./docs/javadoc/index.html)


