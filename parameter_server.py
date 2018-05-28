#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tensorflow as tf
import ClusterSpecification

server = tf.train.Server(ClusterSpecification.CLUSTER_SPEC, job_name='ps', task_index=0)
server.join()
