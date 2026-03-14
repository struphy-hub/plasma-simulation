from abc import ABCMeta, abstractmethod

class SimulationBase(metaclass=ABCMeta):
    """Abstract base class for simulations."""

    @abstractmethod
    def __init__(self, **kwargs):
        """Initialize the simulation."""
        pass

    @abstractmethod
    def allocate(self, verbose: bool = False):
        """Allocate the simulation variables in memory."""
        pass

    @abstractmethod
    def save_geometry_and_equil_vtk(self, verbose: bool = False):
        """Save geometry and equilibrium in VTK format."""
        pass

    @abstractmethod
    def initialize_data_storage(self, verbose: bool = False):
        """Initialize the simulation data storage."""
        pass

    @abstractmethod
    def run(self, verbose: bool = False):
        """Run the simulation."""
        pass

    @abstractmethod
    def pproc(self, verbose: bool = False):
        """Post-process the simulation results."""
        pass

    @abstractmethod
    def load_plotting_data(self, verbose: bool = False):
        """Load post-processed data for visualization."""
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        """Serialize the simulation configuration to a dictionary."""
        pass

    @abstractmethod
    def from_dict(cls, dct: dict):
        """Deserialize a simulation configuration from a dictionary."""
        pass

    @abstractmethod
    def from_file(cls, file_path: str):
        """Deserialize a simulation configuration from a file."""
        pass
    
    @abstractmethod
    def export(self, file_path: str):
        """Export a simulation configuration to a YAML or JSON file based on the file extension."""
        pass
