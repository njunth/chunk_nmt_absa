import numpy
import os

import numpy
import os

from nmt import train

def main(job_id, params):
    print params
    # validerr = train(saveto=params['model'][0],
    #                  reload_=params['reload'][0],
    #                  dim_word=params['dim_word'][0],
    #                  dim_chunk=params['dim_chunk'][0],
    #                  dim_chunk_hidden=params['dim_chunk_hidden'][0],
    #                  dim=params['dim'][0],
    #                  n_words=params['n-words'][0],
    #                  n_words_src=params['n-words'][0],
    #                  decay_c=params['decay-c'][0],
    #                  clip_c=params['clip-c'][0],
    #                  lrate=params['learning-rate'][0],
    #                  optimizer=params['optimizer'][0],
    #                  patience=10000,
    #                  batch_size=32,
    #                  valid_batch_size=32,
    #                  validFreq=100,
    #                  dispFreq=10,
    #                  saveFreq=1000,
    #                  sampleFreq=100,
    #                  maxlen_chunk_words=50,  # maximum length of the description
    #                  datasets=['/home/ningth/Data/nmt/hms.ch.filter',
    #                            '/home/ningth/Data/nmt/hms.en.filter.chunked'],
    #                  valid_datasets=['/home/ningth/Data/nmt/devntest/MT02/MT02.src',
    #                                  '/home/ningth/Data/nmt/devntest/MT02/reference0.tag.chunked.chunked'],
    #                  dictionaries=['/home/ningth/Data/nmt/hms.ch.filter.pkl',
    #                                '/home/ningth/Data/nmt/hms.en.filter.chunked.pkl'],
    #                  dictionary_chunk='/home/ningth/Data/nmt/hms.en.filter.chunked.chunktag.pkl',
    #                  use_dropout=params['use-dropout'][0],
    #                  overwrite=False)
    validerr = train(saveto=params['model'][0],
                     reload_=params['reload'][0],
                     dim_word=params['dim_word'][0],
                     dim_chunk=params['dim_chunk'][0],
                     dim_chunk_hidden=params['dim_chunk_hidden'][0],
                     dim=params['dim'][0],
                     n_words=params['n-words'][0],
                     n_words_src=params['n-words'][0],
                     decay_c=params['decay-c'][0],
                     clip_c=params['clip-c'][0],
                     lrate=params['learning-rate'][0],
                     optimizer=params['optimizer'][0],
                     patience=10000,
                     batch_size=32,
                     valid_batch_size=32,
                     validFreq=100,
                     dispFreq=10,
                     saveFreq=1000,
                     sampleFreq=100,
                     maxlen_chunk_words=50,  # maximum length of the description
                     datasets=['/home/ningth/Data/classification/hms.review.filter',
                               '/home/ningth/Data/classification/hms.aspect.filter.chunked'],
                     valid_datasets=['/home/ningth/Data/classification/hms.review_test.filter',
                                     '/home/ningth/Data/classification/hms.aspect_test.filter.chunked'],
                     dictionaries=['/home/ningth/Data/classification/hms.review.filter.pkl',
                                   '/home/ningth/Data/classification/hms.aspect.filter.chunked.pkl'],
                     dictionary_chunk='/home/ningth/Data/classification/hms.aspect.filter.chunked.chunktag.pkl',
                     use_dropout=params['use-dropout'][0],
                     overwrite=False)
    return validerr

if __name__ == '__main__':
    main(0, {
        'model': ['model_hal.npz'],
        'dim_word': [600],
        'dim_chunk': [1000],
        'dim': [1000],
        'dim_chunk_hidden': [1000],
        'n-words': [30000],
        'optimizer': ['adadelta'],
        'decay-c': [0.],
        'clip-c': [1.],
        'use-dropout': [True],
        'learning-rate': [0.0001],
        'reload': [True]})
