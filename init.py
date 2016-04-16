#!/usr/bin/python
import sys
import thread


def get_class(class_path):
    module_path, class_name = class_path.rsplit(".", 1)

    try:
        module = __import__(module_path, fromlist=[class_name])
    except ImportError:
        raise ValueError("Module '%s' could not be imported" % (module_path,))

    try:
        cls = getattr(module, class_name)
    except AttributeError:
        raise ValueError("Module '%s' has no class '%s'" % (module_path, class_name,))

    return cls

# Define a function for the thread
def registerJob( class_path):
    cls = get_class(class_path)
    cls()

def main():
    mypath = "job"
    # Create two threads as follows
    try:
        from os import listdir
        from os.path import isfile, join
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        print(onlyfiles)
        for file in onlyfiles:
            fp, ext = file.rsplit(".", 1)
            if (ext == "py" and fp != "__init__"):
                finalcp = "job."+fp+"."+fp
                print(finalcp)
                thread.start_new_thread(registerJob, (finalcp,) )
    except:
        e = sys.exc_info()
        print e

    while 1:
        pass


if __name__ == '__main__':
    main()
