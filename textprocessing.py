# -*- coding: utf-8 -*-
import codecs
import jieba

#去除txt中的空行
def STRIP(title):
    with open('/Users/amoism/Documents/Data/News_CrawlData/'+title+'.txt', 'r') as file:
        lines = file.readlines()
    with codecs.open('/Users/amoism/Documents/Data/News_Processing/'+title+'.txt', 'w') as f:
        for line in lines:
            if line != '***********************************************\n':
                try:
                    #去除空行和换行符
                    line = line.strip()
                    f.writelines(line)
                except:
                    print 'wrong'
            else:
                f.writelines(line + '\n')

#分词 筛选
def Processing(title):
    lists = []
    with codecs.open('/Users/amoism/Documents/Data/News_Processing/' + title + '.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            seg_list = jieba.cut(line,cut_all=False)
            for seg in seg_list:
                if seg == u'大学' or seg == u'大学生' or seg == u'高校':
                    lists.append(line)
                    break
    with codecs.open('/Users/amoism/Documents/Data/News_Processing/' + title + '_processing.txt', 'w') as f:
        f.writelines(lists)

def LDA():
    pass

if __name__ == '__main__':
    Title = raw_input('想要处理的文件：')
    #STRIP(Title)
    Processing(Title)
