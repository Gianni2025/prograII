"""
Testing correspondiente a la impresion decorada
"""

import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from beverages import Espresso
from condiments import Caramel, Mocha, Soy, Whip
from pretty_print import pretty_print

# ========== TESTS BÁSICOS DE IMPRESION DECORADA ==========


class TestImpresionDecorada:
    """Tests para distintos combinaciones sin condimentos condimentos repetidos y/o combinados"""

    @pytest.mark.parametrize(
        "condiment_sequence, expected_text",
        [
            ([Whip], "Café Espresso, Crema"),
            ([Whip, Mocha, Mocha], "Café Espresso, Crema, Double Mocha"),
            ([Mocha, Mocha, Whip], "Café Espresso, Double Mocha, Crema"),
            ([Whip, Mocha, Caramel], "Café Espresso, Crema, Mocha, Caramelo"),
            ([Mocha, Mocha, Mocha, Mocha], "Café Espresso, 4x Mocha"),
            ([Soy, Soy, Soy, Soy, Soy], "Café Espresso, 5x Soja"),
            (
                [Mocha, Mocha, Mocha, Mocha, Caramel],
                "Café Espresso, 4x Mocha, Caramelo",
            ),
        ],
    )
    def test_condiment_combinations_should_correct_pretty_print(
        self, condiment_sequence, expected_text
    ):
        """Test parametrizado para diferentes combinaciones de condimentos"""
        espresso = Espresso()
        decorated = espresso
        for condiment_class in condiment_sequence:
            decorated = condiment_class(decorated)
        assert pretty_print(decorated.get_description()) == expected_text
