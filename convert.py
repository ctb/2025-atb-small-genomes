import polars as pl

atb_samples = pl.scan_csv("https://osf.io/vrekj/download", separator="\t").select(
    "Sample"
)

sra_metadata = pl.scan_parquet(
    "s3://sra-pub-metadata-us-east-1/sra/metadata/",
    storage_options={"skip_signature": "true"},
).select(["acc", "biosample"])

atb_samples.join(sra_metadata, left_on="Sample", right_on="biosample").sink_csv(
    "converted.tsv", separator="\t"
)
