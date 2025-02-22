#! /bin/bash
for i in ../subsets/mf-rows.*
do
   NAME=$(basename $i)
   echo $NAME
   cat ../header.csv $i > $NAME.mf.csv
done
