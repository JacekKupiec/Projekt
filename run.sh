#!/bin/bash

./parameter_server.py &
./main.py &
./main.py --index 1 &