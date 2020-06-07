f = open("/Users/sean/Documents/MyProjects/Python/爬虫/mafengwo/Proxies/manfengwo.txt")
fw = open("/Users/sean/Documents/MyProjects/Python/爬虫/mafengwo/Proxies/new_mfw.txt","w")
line = f.readline()

while line:
    # print(line[7:])
    # new_line=line[7:]
    new_line=line[:len(line)-2]
    # print(new_line)
    fw.write( "    '"+new_line+"',\n")
    line = f.readline()


f.close()
fw.close()