import os
import re
import math
from collections import Counter

import os

current_dir = os.path.dirname(os.path.abspath(__file__))
folder = os.path.join(current_dir, "articles")
print(folder)

documents = {}

# 读取所有文章
for filename in os.listdir(folder):

    if filename.endswith(".txt"):

        path = os.path.join(folder, filename)

        with open(path, "r", encoding="utf-8") as f:
            text = f.read().lower()

        words = re.findall(r"[a-z]+", text)

        documents[filename] = words

# 文档总数
N = len(documents)

# 统计DF
df = Counter()

for words in documents.values():

    for word in set(words):
        df[word] += 1

# 求每篇文章关键词
for filename, words in documents.items():

    tf = Counter(words)

    total = len(words)

    tfidf = {}

    for word, count in tf.items():

        TF = count / total
        IDF = math.log(N / df[word])

        tfidf[word] = TF * IDF

    keywords = sorted(
        tfidf.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]

    print(f"\n{filename} 的Top10关键词：")

    for word, score in keywords:
        print(f"{word:<15}{score:.6f}")
        '''
        开始
 ↓
读取articles目录
 ↓
遍历所有txt文件
 ↓
读取文件内容
 ↓
提取单词
 ↓
统计词频(TF)
 ↓
统计文档频率(DF)
 ↓
计算TF-IDF
 ↓
排序
 ↓
输出Top10关键词
 ↓
结束
        '''