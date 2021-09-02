# Step 2 - Docker coding quiz

# This script is meant to create a Dockerfile for the prediction script completed in step 1 (predict.py).

# Please complete the script below (refer to sections marked "TO DO" for parts to be completed)

# TO DO: Import missing modules/packages (if any)


def writeDockerfile(dockerPath):
    with open(dockerPath,'w') as f:

        # TO DO: Complete this script to create a Dockerfile for the prediction script completed in step 1 (predict.py).
        dockerfile = "FROM PYTHON 3.8" \
                     "COPY REQUIREMNTS.TXT " \
                     "RUN PIP INSTALL -R REQUIREMENT.TXT" \
                    "COPY PREDICT.PY ./PREDICT.PY"
                    "RUN PYTHON PREDICT.PY"
        f.write(dockerfile)