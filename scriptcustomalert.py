from __future__ import print_function
import os
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] != "--execute":
        print("FATAL Unsupported execution mode (expected --execute flag)", file=sys.stderr)
        sys.exit(1)
    else:
        file = "/opt/splunk/var/run/splunk/csv/test.csv"
        try:
            os.chmod(file, 0o640)
            print("Permission of file: %s changed." % file)
        except Exception as e:
            print("ERROR Unable to chnage permission of file: %s. Error: %s" % (file, e), file=sys.stderr)
            sys.exit(2)
