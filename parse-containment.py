#! /usr/bin/env python
import sys
import argparse
import pandas as pd
import csv


def main():
    p = argparse.ArgumentParser()
    p.add_argument('manysearch_csvs', nargs='+')
    p.add_argument('-o', '--output')
    args = p.parse_args()

    dfs = []
    for filename in args.manysearch_csvs:
        df = pd.read_csv(filename)
        print(f'loaded {len(df)} from {filename}')
        dfs.append(df)

    all_df = pd.concat(dfs)

    all_df = all_df[all_df['max_containment_ani'] >= 0.9]
    all_df = all_df[['query_name', 'containment', 'max_containment_ani', 'match_name']]
    print(len(all_df))

    best_matches = {}
    for row in all_df.itertuples(index=False):
        match_name = row.match_name

        if match_name in best_matches:
            cmp_row = best_matches[match_name]
            if row.containment > cmp_row.containment:
                best_matches[match_name] = row
        else:
            best_matches[match_name] = row

    print(f'{len(best_matches)} matching SRA accessions.')

    for k, v in sorted(best_matches.items(), key=lambda x: -x[1].containment):
        print(v.match_name, v.containment, v.query_name)

    if args.output:
        with open(args.output, 'w', newline='') as outfp:
            w = csv.writer(outfp)
            w.writerow(['query_name', 'containment', 'max_containment_ani', 'match_name'])
            for k, v in sorted(best_matches.items(), key=lambda x: -x[1].containment):
                w.writerow([v.query_name, v.containment, v.max_containment_ani, v.match_name])
        


if __name__ == '__main__':
    sys.exit(main())
