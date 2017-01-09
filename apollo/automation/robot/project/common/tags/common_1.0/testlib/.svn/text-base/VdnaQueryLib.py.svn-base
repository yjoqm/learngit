import os
from run_cmd import RunCmd
user_module_path = os.path.dirname(os.path.realpath(__file__))
CI_SCRIPT_ROOT = os.environ.get("CI_SCRIPT_ROOT")


class VdnaQueryLib:
    def __init__(self):
        pass

    def vdna_query(self, host, username, password, media_file):
        media_file = CI_SCRIPT_ROOT + '/' + media_file
        cmd = ["vdna_query", "-s %s" % host, "-u %s" % username, "-w %s" % password, "-Tdna -i %s" % media_file]
        process = RunCmd(" ".join(cmd))
        return_code = process.run()
        return process.stdout
