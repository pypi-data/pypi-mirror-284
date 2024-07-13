import requests as r
import time
import pandas as pd
from translate import Translator

def get_meaning(word):
    translator= Translator(to_lang="zh")
    translation = translator.translate(word)
    return translation

def en2cn(word):
    df = pd.read_excel('词汇总表.xlsx')
    # 如果总表里有这个词汇
    if word in df['英文'].values:
        # 如果总表里有这个翻译，直接输出
        if pd.notnull(df.loc[df['英文'] == word,'中文'].values[0]):
            return df.loc[df['英文'] == word,'中文'].values[0]
        else:
            # 如果总表里没有这个翻译，则查询后，添加进总表，并输出
            print('总词表中没有你要查询的词，翻译工作会有延时')
            res = get_meaning(word)
            df.loc[df['英文'] == word, '中文'] = res
            df.to_excel('词汇总表.xlsx', index=False) # 保存
            return res
    # 词汇总表里没有该词
    else:
        print('总词表中没有你要查询的词，翻译工作会有延时')
        res = get_meaning(word)
        new = pd.DataFrame({'英文':word,'中文':res},index=[0]) # 创建一个新条目
        df = df.append(new) # 插入老表格
        df.to_excel('词汇总表.xlsx', index=False) # 保存
        return res
