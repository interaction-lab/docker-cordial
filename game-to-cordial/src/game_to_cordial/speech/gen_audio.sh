#!/bin/bash

mkdir data
rosrun cordial_tts gen_phrases.py Ivy data phrases.yaml script.txt
oggdec data/*.ogg
