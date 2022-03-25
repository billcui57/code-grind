import argparse
import os
import mdutils
import yaml

# Initialize parser
parser = argparse.ArgumentParser(description="Add template for a new problem")

parser.add_argument('name', metavar='n')

args = parser.parse_args()

problemName = args.name


cwd = os.getcwd()
path = os.path.join(cwd, problemName)

os.mkdir(path)

os.chdir(path)

mdFile = mdutils.MdUtils(file_name='README')

mdFile.new_header(level=1, title=problemName)
mdFile.new_header(level=2, title='Link')
mdFile.new_header(level=2, title='Where')
mdFile.new_header(level=2, title='Difficulty')
mdFile.new_header(level=2, title='Description')
mdFile.new_header(level=2, title='Solution Main Idea')

mdFile.create_md_file()

f = open("solution.py", "a")

f.close()


with open(os.path.join(cwd, "defaults.yaml"), 'r') as yamlfile:
    cur_yaml = yaml.safe_load(yamlfile)  # Note the safe_load
    cur_yaml['input-files'].append("./"+problemName+"/README.md")

if cur_yaml:
    with open(os.path.join(cwd, "defaults.yaml"), 'w') as yamlfile:
        yaml.safe_dump(cur_yaml, yamlfile)  # Also note the safe_dump
