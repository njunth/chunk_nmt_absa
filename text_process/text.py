from dataset import load_dataset, unwrap, build_vocab
import sys  
reload(sys)  
import cPickle as pkl
sys.setdefaultencoding('utf8')  

def main(product):        
    dictionary_chunk = 'hms.en.filter.chunked.chunktag.pkl'
    with open(dictionary_chunk, 'rb') as f:
        chunk_dict = pkl.load(f)
        print chunk_dict

    output_train_r_p = open('hms.aspect.filter.chunked.chunktag.pkl', 'w')
    aspect_chunktag=dict()
    aspect_chunktag['eos']=0
    aspect_chunktag['NULL']=1
    aspect_chunktag['A']=2
    aspect_chunktag['P']=3
    print(aspect_chunktag)
    pkl.dump(aspect_chunktag, output_train_r_p)
    output_train_r_p.close()
    # dictionaries=['hms.review.filter.pkl', 'hms.aspect.filter.chunked.pkl']
    # worddicts = [None] * len(dictionaries)
    # worddicts_r = [None] * len(dictionaries)
    # for ii, dd in enumerate(dictionaries):
    #     with open(dd, 'rb') as f:
    #         worddicts[ii] = pkl.load(f)
    #     worddicts_r[ii] = dict()
    #     for kk, vv in worddicts[ii].iteritems():
    #         print kk, vv
    #         worddicts_r[ii][vv] = kk



    TRAIN_FILE = "data/ABSA-15_{}_Train_Data.xml".format(product)
    training_reviews = load_dataset(TRAIN_FILE)
    training_sentences = unwrap(training_reviews)
    reviews = ""
    review_words=dict()
    review_it=0
    aspect=""
    aspect_words=dict()
    aspect_it=0
    for sentence in training_sentences:
        reviews += sentence.raw_text
        reviews += '\n'
        # print sentence.raw_text
        for word in sentence.words:
            if word not in review_words:
                review_words[word] = review_it
                review_it = review_it+1
        for opinion in sentence.opinions:
            aspect += 'A'
            aspect += '	'
            aspect += opinion.category
            if opinion.category not in aspect_words:
                aspect_words[opinion.category] = aspect_it
                aspect_it = aspect_it+1
                # print aspect_it
            aspect += '\n'
            print (opinion.category)
            aspect += 'P'
            aspect += '	is '
            if opinion.polarity == +1:
                aspect += 'postive'
                aspect += '\n'
            if opinion.polarity == -1:
                aspect += 'negative'
                aspect += '\n'
            if opinion.polarity == 0:
                aspect += 'neutral'
                aspect += '\n'
        aspect += '\n'
    aspect_words['is'] = aspect_it
    aspect_it = aspect_it+1
    aspect_words['postive'] = aspect_it
    aspect_it = aspect_it+1
    aspect_words['negative'] = aspect_it
    aspect_it = aspect_it+1
    aspect_words['neutral'] = aspect_it
    aspect_it = aspect_it+1       

    print(aspect_words)

    output_train_r = open('hms.review.filter', 'w')
    output_train_r.write(reviews)
    output_train_r.close()

    output_train_r_p = open('hms.review.filter.pkl', 'w')
    pkl.dump(review_words, output_train_r_p)
    output_train_r_p.close()

    output_train_a = open('hms.aspect.filter.chunked', 'w')
    output_train_a.write(aspect)
    output_train_a.close()

    output_train_a_p = open('hms.aspect.filter.chunked.pkl', 'w')
    pkl.dump(aspect_words, output_train_a_p)
    output_train_a_p.close()

    # Test 
    TEST_FILE = "data/ABSA15_{}_Test.xml".format(product)
    FILE = TEST_FILE
    testing_reviews = load_dataset(FILE)
    testing_sentences = unwrap(testing_reviews)
    reviews = ""
    reviews=reviews.encode('ascii','ignore')
    aspect=""
    for sentence in testing_sentences:
        reviews += sentence.raw_text
        reviews += '\n'
        print sentence.raw_text
        for opinion in sentence.opinions:
            aspect += 'A'
            aspect += '	'
            aspect += opinion.category
            aspect += '\n'
            print (opinion.category)
            aspect += 'P'
            aspect += '	is '
            if opinion.polarity == +1:
                aspect += 'postive'
                aspect += '\n'
            if opinion.polarity == -1:
                aspect += 'negative'
                aspect += '\n'
            if opinion.polarity == 0:
                aspect += 'neutral'
                aspect += '\n'
        aspect += '\n'

    print(len(testing_sentences))

    output_test_r = open('hms.review_test.filter', 'w')
    output_test_r.write(reviews)
    output_test_r.close()

    output_test_a = open('hms.aspect_test.filter.chunked', 'w')
    output_test_a.write(aspect)
    output_test_a.close()


if __name__ == "__main__":
    # main("Laptops")
    main("Restaurants")
