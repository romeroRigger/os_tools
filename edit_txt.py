import os

# CURRENT WORKING DIRECTORY
cwd = os.getcwd()
print cwd


# OPEN, EDIT AND READ FILE IN THE SAME FOLDER
f = open('try_a.txt', 'w')
f.write('hello Mars!')
f.close()


f = open('try_a.txt', 'r')
message = f.read()
print(message)
f.close()


# OPEN AND EDIT FILE IN OTHER FOLDER
f = open('test_folder/try_b.txt', 'w')
f.write('hello Pluto!')
f.close()


# OTHER WAY TO EDIT AND PUT MORE INFO INSIDE OF THE FILE
f = open('test_folder/try_c.txt', 'w')
lines_of_text = ['One line of text here', 'and another line here',
                 'and yet another here', 'and so on and so forth']
f.writelines("%s\n" % l for l in lines_of_text)
f.close()


# READ A FILE IN OTHER FOLDER
f = open('test_folder/try_c.txt', 'rw+')
message = f.readlines()
print(message)
f.close()

for each in message:
    print each


# READ ini FILE
# f = open('/Users/mac/Library/Preferences/Autodesk/maya/2016/prefs/charcoalEditor.ini', 'r')
# message = f.read()
# print(message)
# f.close()
