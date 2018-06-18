#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tensorflow as tf

"""PS_HOSTS = ['10.0.2.15:2222']
WORKER_HOSTS = ['10.0.2.8:2222', '10.0.2.9:2222']"""

PS_HOSTS = ['localhost:2222']
WORKER_HOSTS = ['localhost:2223', 'localhost:2224']

CLUSTER_SPEC = tf.train.ClusterSpec({'ps': PS_HOSTS, 'worker': WORKER_HOSTS})

