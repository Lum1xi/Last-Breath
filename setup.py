from config import keysBind
verticalBind = []
horizontalBind = []

def setup():
    for bind in keysBind["vertical"]:
            for i in keysBind["vertical"][bind]:
                verticalBind.append(i)
    for bind in keysBind["horizontal"]:
        for i in keysBind["horizontal"][bind]:
            horizontalBind.append(i)