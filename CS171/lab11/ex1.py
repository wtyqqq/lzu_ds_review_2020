import glob, os


def extension(dic, extention):
    outp = []
    os.chdir("./" + dic)
    for file in glob.glob("*." + extention):
        outp.append(file)
    return outp


if __name__ == '__main__':
    print(extension('test', 'png'))
