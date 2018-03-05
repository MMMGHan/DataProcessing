# -*- coding:utf8 -*-
# coding=utf-8
import os
import sys

import jieba
import numpy as np
import matplotlib
import scipy
import numpy as np
import lda.datasets
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer


if __name__ == "__main__":

    n = 5; #每个主题输出的关键字个数
    article_num = 15; #文章数目
    Topic_num = 2;

# 存储读取语料 一行语料为一个文档
    corpus = []
    for line in open('/Users/amoism/Documents/Data/News_Processing/zican_processing.txt', 'r').readlines():
        #seg_list = jieba.cut(line, cut_all=False)
        corpus.append(line)

# 将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
    vectorizer = CountVectorizer()
# 该类会统计每个词语的tf-idf权值
    transformer = TfidfTransformer()
# 第一个fit_transform是计算tf-idf 第二个fit_transform是将文本转为词频矩阵
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))

# fit_transform是将文本转为词频矩阵
    X = vectorizer.fit_transform(corpus)

# 获取词袋模型中的所有词语
    word = vectorizer.get_feature_names()
    analyze = vectorizer.build_analyzer()
    weight = X.toarray()

# 打印特征向量文本内容
    print 'Features length: ' + str(len(word))
    for j in range(len(word)):
        print word[j]

# 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
    # for i in range(len(weight)):
    #     for j in range(len(word)):
    #         print weight[i][j],
    #     print '\n'

# LDA算法
    print 'LDA:'
    model = lda.LDA(n_topics=Topic_num, n_iter=500, random_state=1)
    model.fit(np.asarray(weight))  # model.fit_transform(X) is also available
    topic_word = model.topic_word_  # model.components_ also works

# 输出主题中的TopN关键词
    word = vectorizer.get_feature_names()
    # for w in word:
    #     print w
    # print topic_word[:, :3]
    for i, topic_dist in enumerate(topic_word):
        topic_words = np.array(word)[np.argsort(topic_dist)][:-(n + 1):-1]
        print(u'*Topic {}\n- {}'.format(i, ' '.join(topic_words)))

# 文档-主题（Document-Topic）分布
    doc_topic = model.doc_topic_
    print("type(doc_topic): {}".format(type(doc_topic)))
    print("shape: {}".format(doc_topic.shape))

# 输出前 article_num 篇文章最可能的Topic
    label = []
    for n in range(article_num):
        topic_most_pr = doc_topic[n].argmax()
        label.append(topic_most_pr)
        print("doc: {} topic: {}".format(n, topic_most_pr))
