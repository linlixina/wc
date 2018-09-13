import sys
import os
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-l", "--line",
                  dest="lines",
                  action="store_true",
                  default=False,
                  help="count lines")
parser.add_option("-w", "--word",
                  dest="words",
                  action="store_true",
                  default=False,
                  help="count words")
parser.add_option("-c", "--char",
                  dest="chars",
                  action="store_true",
                  default=False,
                  help="count chars")
parser.add_option("-a", "--aaa",
                  dest="aaas",
                  action="store_true",
                  default=False,
                  help="count aaas")
parser.add_option("-s", "--subject",
                  dest="subjects",
                  action="store_true",
                  default=False,)
options, args = parser.parse_args()


"""根据指定不同选项显示不同的值"""


def wc_print(lines, words, chars, codelines , emptylines ,commentlines):
    if options.lines:
        print('行数：' + str(lines)),
    if options.words:
        print('词数：' + str(words)),
    if options.chars:
        print('字符数：' + str(chars)),
    if options.aaas:
        print('代码行/空行/注释行：' + str(codelines) + '/' + str(emptylines) + '/' + str(commentlines)),
    if options.subjects:
        print('行数：' + str(lines)),
        print('词数：' + str(words)),
        print('字符数：' + str(chars)),
        print('代码行/空行/注释行：' + str(codelines) + '/' + str(emptylines) + '/' + str(commentlines)),



def judge(data):
    if not os.path.exists(data):
        sys.stderr.write("%s No such file or directory\n" % data)
        return False
    return True


def read_message(_files):
    for file in _files:
        f = judge(file)
        if f:
            with open(file, encoding="ISO-8859-1") as files:
                cs = files.read()
                chars = len(cs)
                words = len(cs.split())
                files.close()
            with open(file, encoding="ISO-8859-1") as files:
                ls = files.readlines()
                lines = len(ls)
                files.close()
            with open(file, encoding="ISO-8859-1") as files:
                l_ines = files.readlines()
                codelines, emptylines, commentlines = [], [], []  # 将满足条件的特殊行加入对应的列表中
                for line in l_ines:
                    tmpline = line.replace(' ', '')
                    tmpline = tmpline.replace('\t', '')
                    tmpline = tmpline.replace('\n', '')
                    if len(tmpline) == 1 or len(tmpline) == 0:  # 判断是否为空行
                        emptylines.append(line)
                    elif tmpline.startswith('//'):  # 判断是否为注释行
                        commentlines.append(line)
                    else:
                        codelines.append(line)
                codelines = len(codelines)  # 通过列表长度判断特殊行行数
                emptylines = len(emptylines)
                commentlines = len(commentlines)
                wc_print(lines, words, chars, codelines, emptylines, commentlines)
                print(file)
        else:
            continue


def list_all_files(rootdir):  # 遍历文件夹
    _files = []
    list = os.listdir(rootdir)  # 路径下的文件列表
    for i in range(0, len(list)):  # 生成子目录
        path = os.path.join(rootdir, list[i])
        if os.path.isdir(path):  # 如果是目录，采用递归操作
            _files.extend(list_all_files(path))
        if os.path.isfile(path):
            _files.append(path)
    print(_files)
    return _files


if __name__ == '__main__':
    try:
        _files = list_all_files(args[-1])
        read_message(_files)
    except:
        read_message([args[-1]])