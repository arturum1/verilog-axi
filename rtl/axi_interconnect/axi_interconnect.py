import os

from iob_module import iob_module

class axi_interconnect(iob_module):
    def __init__(self):
        super().__init__()
        self.name = "axi_interconnect"
        self.version = "V0.10"
        self.setup_dir = os.path.dirname(__file__)
