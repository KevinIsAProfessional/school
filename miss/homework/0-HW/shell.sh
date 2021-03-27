#!/bin/bash

filelist=$( ls -R | grep .py$ )
for x in $filelist; do
  grep -n def
done
