import subprocess

a = subprocess.Popen(args=["mkdir", "test"])
a.terminate()

import subprocess

a = subprocess.Popen(args=["mkdir", "test"], stdout=subprocess.PIPE)
out, err = a.communicate()

print(out)
