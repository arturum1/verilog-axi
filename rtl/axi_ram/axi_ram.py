from dataclasses import dataclass

from iob_module import iob_module


@dataclass
class axi_ram(iob_module):
    version = "V0.10"
