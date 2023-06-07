import os
import shutil

from iob_module import iob_module


class axi_interconnect(iob_module):
    name = "axi_interconnect"
    version = "V0.10"
    setup_dir = os.path.dirname(__file__)

    @classmethod
    def _run_setup(cls):
        super()._run_setup()

        # Setup dependencies

    # Copy sources of this module to the build directory
    @classmethod
    def _copy_srcs(cls):
        out_dir = cls.get_purpose_dir(cls._setup_purpose[-1])
        # Copy sources to build directory
        shutil.copyfile(
            os.path.join(cls.setup_dir, "axi_interconnect.v"),
            os.path.join(cls.build_dir, out_dir, "axi_interconnect.v"),
        )
        shutil.copyfile(
            os.path.join(cls.setup_dir, "arbiter.v"),
            os.path.join(cls.build_dir, out_dir, "arbiter.v"),
        )
        shutil.copyfile(
            os.path.join(cls.setup_dir, "priority_encoder.v"),
            os.path.join(cls.build_dir, out_dir, "priority_encoder.v"),
        )

        # Ensure sources of other purposes are deleted (except software)
        # Check that latest purpose is hardware
        if cls._setup_purpose[-1]=='hardware' and len(cls._setup_purpose)>1:
            # Purposes that have been setup previously
            for purpose in [x for x in cls._setup_purpose[:-1] if x!="software"]:
                # Delete sources for this purpose
                os.remove(os.path.join(cls.build_dir, cls.PURPOSE_DIRS[purpose], "axi_interconnect.v"))
                os.remove(os.path.join(cls.build_dir, cls.PURPOSE_DIRS[purpose], "arbiter.v"))
                os.remove(os.path.join(cls.build_dir, cls.PURPOSE_DIRS[purpose], "priority_encoder.v"))
