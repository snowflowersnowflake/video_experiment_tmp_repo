import os

def h264ToMp4(sourcePath, tagPath):
    cmd = 'ffmpeg -f h264 -i ' + sourcePath + ' -vcodec copy ' + './' +tagPath
    print(">>cmd:\n %s" % (cmd))
    result = os.popen(cmd).read().strip()
    print(">>result :", result)

for i in os.listdir("./"):
    re=i.split(".")[0]+".mp4"
    source=os.path.join("./",i)
    print(source,re)
    h264ToMp4(source,re)