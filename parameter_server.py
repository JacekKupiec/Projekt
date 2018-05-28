#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tensorflow as tf
import ClusterSpecification
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--index", 
      default=0,
      help="Index of the worker",
      type=int)
FLAGS, unparsed = parser.parse_known_args()

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
server = tf.train.Server(ClusterSpecification.CLUSTER_SPEC, job_name='ps', task_index=FLAGS.index)
server.join()
