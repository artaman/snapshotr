__hash__ = None

import nuke
import hashlib
import os
import time
from sys import path
snapr_path = os.getenv("HOME") + "/.nuke/snapshotr"
path.append(snapr_path)

# TODO: Add update_DATETIME.log

known_modules = {"__init__.py":"d0be737ae58694404a019d52eef22a2c249e9671a8fad41ea7e4eb475aeda2d3",
"snapshotr_panel.py":"6497cebfb4393db55b93865489c58865b89d70c1adb02936f62a32c3362b7d4c",
"snapshotr_update.py":"2c25db6b2aabcaacbdd2d4a4624976a21a552432de87f0166e9274fed27c2732",
"snapshotr_webView.py":"e5cfbe8547bb7767cc7665e6e01da74cb4a6a73c48d1c252d09de79339965dd1",
"snapshotr_common.py":"95b3c0c25bacb2c5f106083a410e5db20647fa0265128e93e76a7e19edc485b2",
"test_init.py":"e9441574ec8df74423805a208a57c652d879ead7110aa10cc8ba5f5d8e863a33",
"markup.py":"757e192986642f72cc06f9239711754ac2be1211b3849a12e2438ed58cc77db4",
"scandir.py":"8b449ac6173f02643761a2d618dfaa928cbbf29f3e679e03fb149e6c047c2562"}

def update_message():
    if nuke.ask('New version of "Snapshotr" found. Would you like to update?'):
        return True

def check_modules_exist():
    found_modules = []
    for filex in os.listdir(snapr_path):
        if filex in known_modules:
            found_modules.append(filex)
    if len(known_modules) == len(found_modules):
        print "\n~ Starting update, found " + str(len(found_modules)) + " known modules"
        return True

def check_hashes():
    for filex in known_modules:
        filex_fullpath = snapr_path + "/" + filex
        if known_modules[filex] == hashlib.sha256(open(filex_fullpath, 'rb').read()).hexdigest():
            print "* " + filex + " is OK"
        else:
            print "! " + filex + " is modified"

def backup_ss():
    """
    :return: 0 if everything went fine
    """
    timestamp = time.strftime("%d-%m-%Y") + '_' + time.strftime("%H-%M")
    backup_folder = os.path.expanduser("~/.nuke/snapshotr_backup")
    backup_command = "zip -r " + backup_folder + "/backup_" + timestamp + ".zip "\
                     + os.path.expanduser("~/.nuke/snapshotr/")
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
    return os.system(backup_command)
