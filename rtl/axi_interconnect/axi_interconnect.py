import os

# Find python modules
if __name__ == "__main__":
    import sys
    sys.path.append("./scripts")
from iob_module import iob_module
if __name__ == "__main__":
    iob_module.find_modules()

from arbiter import arbiter
from priority_encoder import priority_encoder


class axi_interconnect(iob_module):
    name = "axi_interconnect"
    version = "V0.10"
    setup_dir = os.path.dirname(__file__)

    @classmethod
    def _init_attributes(cls):
        """Init module attributes"""
        cls.submodules = [
            arbiter,
            priority_encoder,
        ]


if __name__ == "__main__":
    axi_interconnect.setup_as_top_module()
