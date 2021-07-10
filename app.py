def read_requirements():
    import re
    p = re.compile("(\w*(\-\w*)*)\=\=(\d*\.\d*\.\d*)")
    with open("requirements.txt", 'r') as f:
        reqs = f.readlines()

    res = []
    ver = []
    for req in reqs:
        m = p.match(req)
        res.append(m.group(1))
        ver.append(m.group(3))

    return res, ver


read_requirements()
