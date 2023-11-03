import os
import shutil

# Find python modules
if __name__ == "__main__":
    import sys

    sys.path.append("./scripts")

from iob_module import iob_module

if __name__ == "__main__":
    iob_module.find_modules()

class axi_ram(iob_module):
    @classmethod
    def _init_attributes(cls):
        """Init module attributes"""
        cls.name='axi_ram'
        cls.version='V0.10'
        cls.setup_dir=os.path.dirname(__file__)
