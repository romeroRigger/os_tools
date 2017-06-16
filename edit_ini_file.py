import pymel.core as pm

# CHANGE THE CHARCOAL EDITOR  PATHS
# BASIC SCRIPT UNDER DEVELOP

path_file = '/Users/mac/Library/Preferences/Autodesk/maya/2016/prefs/charcoalEditor.ini'
char_dirs = {'pDir_1': 'projectDir=/Volumes/proRoboto/projects/scripting \n',
             'pDir_2': 'projectDir=/Volumes/proRoboto/projects \n',
             'pDir_3': 'projectDir=/Users/mac/Library/Preferences/Autodesk/maya/2016/scripts \n'}


def charcoalDirs(new_dir):
    lookup = 'projectDir'
    f = open(path_file, 'rw+')
    message = f.readlines()

    with open(path_file) as myFile:
        for num, line in enumerate(myFile, 1):
            if lookup in line:
                print 'found at line:', num
                message[num-1] = new_dir

    f = open(path_file, 'w')
    f.writelines(l for l in message)
    f.close()

    pm.mel.eval('charcoalEditor;')


charcoalDirs(char_dirs['pDir_2'])