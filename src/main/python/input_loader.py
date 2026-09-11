from generator import Generator


class InputLoader:

    @staticmethod
    def sample_generators():

        generators = [

            Generator(
                gen_id=1,
                min_cap=50,
                max_cap=200,
                a=500,
                b=5.3,
                c=0.004
            ),

            Generator(
                gen_id=2,
                min_cap=50,
                max_cap=150,
                a=400,
                b=5.5,
                c=0.006
            ),

            Generator(
                gen_id=3,
                min_cap=50,
                max_cap=100,
                a=200,
                b=5.8,
                c=0.009
            )
        ]

        return generators