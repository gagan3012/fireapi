        dockerfile = "FROM PYTHON 3.8" \
                     "COPY REQUIREMNTS.TXT " \
                     "RUN PIP INSTALL -R REQUIREMENT.TXT" \
                    "COPY PREDICT.PY ./PREDICT.PY"
                    "RUN PYTHON PREDICT.PY"
        f.write(dockerfile)