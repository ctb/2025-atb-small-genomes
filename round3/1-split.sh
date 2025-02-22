#! /bin/bash
sort -R ../mf-rows.csv > ../mf-rows.random.csv
split -l 1000 ../mf-rows.random.csv mf-rows.
