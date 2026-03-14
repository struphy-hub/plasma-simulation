import pytest

from plasma_simulation import SimulationBase


def test_import_app():
    # Import check and API surface check.
    assert SimulationBase is not None


def test_simulation_base_is_abstract():
    with pytest.raises(TypeError, match="abstract class SimulationBase"):
        SimulationBase()


if __name__ == "__main__":
    test_import_app()
    test_simulation_base_is_abstract()
