import os
APP_FOLDER = os.getcwd()
counter = 0
for file in os.listdir(APP_FOLDER):
    if 'venv' in file or '.git' in file or 'paradigms' in file:
        continue
    d = os.path.join(APP_FOLDER, file)
    if os.path.isdir(d):
        counter += 1

print(counter)
