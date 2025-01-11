def write(data):
    with open(base.txt,"w",encoding="utf-8") as file:
            file.write(data+"/n")
def read():
    with open(base.txt,"r",encoding="utf-8") as f:
               base.txt.append(line.strip())