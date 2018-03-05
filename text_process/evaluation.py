from dataset import load_dataset, unwrap, build_vocab
import sys
reload(sys)
from eval import microF1  
import cPickle as pkl
sys.setdefaultencoding('utf8')  

def local_test():
    with open('local_results', 'rb') as f:
        list_of_all_the_lines = f.readlines()
    predict = []
    gold_aspects = []
    for line in list_of_all_the_lines:
        words = line.split(' ')
        if words[0] == 'Truth':
            l = set()
            for word in words:
                if word.find('#') > 0:
                    l.add(word)
            gold_aspects.append(l)
        if words[0] == 'Sample':
            l = set()
            for word in words:
                if word.find('#') > 0:
                    l.add(word)
            predict.append(l)
    print len(predict), len(gold_aspects)
    print microF1(predict, gold_aspects)


def main(product):
    with open('result', 'rb') as f:
        list_of_all_the_lines = f.readlines( )
    aspects = []
    for line in list_of_all_the_lines:
        asp = set()
        words = line.split(' ')
        for word in words:
            if word.find('#') > 0:
               asp.add(word)
        print asp
        aspects.append(asp)   
    print len(aspects)

    with open('hms.aspect_test.filter.chunked','rb') as f:
        list_of_all_the_lines = f.readlines( )
    gold_aspects=[]
    asp = set()
    for line in list_of_all_the_lines:
        if len(line) <=1:
        	print asp
        	temp = set()
        	for l in asp:
        	    temp.add(l)
        	gold_aspects.append(temp)
        	asp.clear()
        	continue
        words = line.split('	')
        for word in words:
            if word.find('#') > 0:
               asp.add(word[:len(word)-1])
    print len(gold_aspects)
    # print gold_aspects
    print microF1(aspects, gold_aspects)



if __name__ == "__main__":
    local_test()
    # main("Restaurants")