def read_requirements():
    with open("requirements.txt", 'r') as f:
        reqs = f.readlines()

    for req in reqs:
        req = req[:-1]


