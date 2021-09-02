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