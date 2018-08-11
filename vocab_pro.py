import numpy as np
from pypinyin import pinyin, FINALS,FINALS_TONE3

def check_contain_chinese(check_str):
     for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
     return False

def word_fliter(filename): # 词频排序后取前两万个
    ch_vocab = []
    en_vocab = []
    with open(filename,encoding='utf-8-sig') as fin:
        sens = fin.readlines()
        dict = {}
        for sen in sens:
           sen = sen.strip().split()
           for word in sen:
               if check_contain_chinese(word):
                   if word not in dict:
                       dict[word] = 1
                   else:
                       dict[word]+=1
               else:
                   if word not in en_vocab:
                       en_vocab.append(str(word))
        wordslist = sorted(dict.items(), key=lambda item: -item[1])[:20000]
        for item in wordslist:
            ch_vocab.append(item[0])
        print(len(ch_vocab))
        print(ch_vocab)
        print(len(en_vocab))
        print(en_vocab)
        np.save('ch_vocab.npy',ch_vocab)
        np.save('en_vocab.npy',en_vocab)


table = [['i'],
         ['u'],
         ['v'],
         ['a','ia','ua'],
         ['o','uo','io'],
         ['e','ie','ve','ue'],
         ['ai','uai'],
         ['ei','uei'],
         ['ao','iao'],
         ['ou','iou'],
         ['an','ian','uan','van'],
         ['en','uen','n'],
         ['in'],
         ['un'],
         ['vn'],
         ['ang','iang','uang'],
         ['ing'],
         ['eng','ueng'],
         ['ong','iong'],
         ['er']
         ]
def table_dic():
    rhyme_dic={}
    rhyme_dic2 = {}
    i = 0
    for items in table:
        for item in items:
            rhyme_dic[item] =i
            rhyme_dic2[item] = []
        i+=1
    return rhyme_dic,rhyme_dic2

def ryhme_voc(vocab_rhy):

    vocab = np.load('ch_vocab.npy')
    for word in vocab:
        pin = pinyin(word,FINALS)[-1][0]
        try:
            vocab_rhy[pin].append(word)
        except:
            print("error",word,"  ",pin)
            vocab_rhy['i'].append('鸟事')
    np.save('ryh_word.npy',vocab_rhy)
    return vocab_rhy

def w2idx_ord(vocab_rhy,ryh_words): #
    i=0
    j =0

    print(ryh_words)
    vocab = []
    for key in ryh_words:
        length = 0
        length = len(ryh_words[key])
        j+=length
        vocab_rhy[key] =[i,j-1]
        i = j
        vocab+=ryh_words[key]
    print(vocab)
    print(vocab_rhy)
    np.save('vocab_ord.npy',vocab)
    print(len(vocab))
    np.save('rhyme_range.npy',vocab_rhy)





if __name__ =="__main__":
    # 中英文分离 并取中文词频高的前两万
    # filename='x.txt'
    # word_fliter(filename)


    # 中文词 按韵脚排序
    # vocab_rhy1 = table_dic()[1]  # {key:[]}
    # ryh_words = ryhme_voc(vocab_rhy1)  # {key:}
    #
    # vocab_rhy0 = table_dic()[0]  # {key:int}
    # w2idx_ord(vocab_rhy0, ryh_words)

    #合并 按韵脚排序后的中文词 与原来的英文词
    # vocab_ord = np.load("vocab_ord.npy")
    # en_vocab = np.load("en_vocab.npy")
    # vocab_ord_all = np.hstack((vocab_ord,en_vocab))
    # np.save('vocab_ord_all.npy',vocab_ord_all)
    # print(vocab_ord_all)
    # print(len(vocab_ord_all))

    #把押韵的范围合并
    # ryhme_range = np.load('rhyme_range.npy').item()
    # str = []
    # index = []
    # dict = {}
    # for item in table:
    #     for r in item:
    #         str.append(r)
    #         index += ryhme_range[r]
    #     print(str)
    #     for r in str:
    #         dict[r]=[index[0],index[-1]]
    #     str = []
    #     index=[]
    # print(dict)
    # np.save('rhyme_range3.npy',dict)

    # 给词一个index
    # vocab = np.load('vocab_ord_all.npy')
    # vocab_dict ={}
    # for i,item in enumerate(vocab):
    #     vocab_dict[item] =i
    # np.save('vocab_dict.npy',vocab_dict)

    # ryhme_range = np.load('rhyme_range3.npy')
    # vocab_dict = np.load('vocab_dict.npy')
    # print(ryhme_range)
    # print(vocab_dict)
    pin = pinyin("鸟的事",style=FINALS)
    print(pin)































