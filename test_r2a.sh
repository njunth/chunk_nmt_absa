#!/bin/bash
#PBS -l nodes=1:ppn=24
#PBS -l walltime=24:00:00
#PBS -N session2/models/memory-set_default
#PBS -A course
#PBS -q ShortQ

export THEANO_FLAGS=device=cpu,floatX=float32

#cd $PBS_O_WORKDIR
python ./translate.py -n -p 8 \
        ./model_hal.npz  \
        ./model_hal.npz.pkl  \
	/home/ningth/Data/classification/hms.review.filter.pkl \
	/home/ningth/Data/classification/hms.aspect.filter.chunked.pkl \
	/home/ningth/Data/classification/hms.review_test.filter\
	/home/ningth/Data/classification/result

