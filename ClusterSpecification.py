#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tensorflow as tf

PS_HOSTS = ['192.168.1.10:2222', '192.168.1.12:2222']
WORKER_HOSTS = ['192.168.1.10:2223', '192.168.1.12:2223']
CLUSTER_SPEC = tf.train.ClusterSpec({'ps': PS_HOSTS, 'worker': WORKER_HOSTS})
