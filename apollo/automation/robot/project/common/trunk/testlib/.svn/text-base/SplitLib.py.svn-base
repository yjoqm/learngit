import os
from run_cmd import RunCmd
user_module_path = os.path.dirname(os.path.realpath(__file__))
CI_SCRIPT_ROOT = os.environ.get("CI_SCRIPT_ROOT")


class SplitLib:
    def __init__(self):
        pass

    def far_split(self, far_file, dir_far):
        far_file = CI_SCRIPT_ROOT + '/' + far_file
        dir_far = CI_SCRIPT_ROOT + '/' + dir_far
        cmd = ["far_split", "-i %s" % far_file, "-d %s" % dir_far]
        process = RunCmd(" ".join(cmd))
        return_code = process.run()
        return process.stdout