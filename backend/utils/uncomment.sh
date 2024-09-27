#!/bin/bash

CONFIG_FILE=$1
STEP_LANDMARKS=$2
NEW_FILE="updated_config.yaml"

python -c '
import sys
fileLoc=sys.argv[1]
landmark=sys.argv[2]
newFile=sys.argv[3]

new_file_content = ""

start_landmark="# #{0}_start".format(landmark)
end_landmark="# #{0}_end".format(landmark)

with open(fileLoc, "r") as file:
    uncomment = False
    for line in file:
        if line.startswith(start_landmark):
            uncomment = True 
        if uncomment:
            new_file_content += line[2:]
        else:
            new_file_content += line
        if line.startswith(end_landmark):
            uncomment = False

with open(newFile, "w") as file:
    file.write(new_file_content)

' $CONFIG_FILE $STEP_LANDMARKS $NEW_FILE

rm $CONFIG_FILE
mv $NEW_FILE $CONFIG_FILE
