#!/usr/bin/env python3

import argparse

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, collect_set, count, countDistinct, explode, size, struct, when, min


def distinct_mappings(df):
    print('\n### Total number of distinct label to keyword mappings')
    print(
        df
        .groupby('type')
        .agg(size(collect_set(struct('label', 'keywordId'))))
        .toPandas()
        .to_markdown()
    )


def app_synonyms(df):
    print('\n### ')


parser = argparse.ArgumentParser()
parser.add_argument('--matches', help='Path to the `matches` dataset')
args = parser.parse_args()

spark = SparkSession.builder.appName('epmc_ambiguity').getOrCreate()
matches = spark.read.parquet(args.matches)
matches_mapped = matches.filter(col('isMapped') == True)

matches_filtered = (
    matches_mapped
    # .filter(col('type') == 'GP')

    # For each label (original text), see how many keywords it maps to within the context of the article.
    # When a label maps to only one keyword, it is considered unambiguous.
    .groupby('pmid', 'pmcid', 'type', 'label')
    .agg(
        collect_set('keywordId').alias('distinctKeywordIds'),
        countDistinct('keywordId').alias('distinctKeywordIdCountForLabel')
    )
    .withColumn('keywordId', explode('distinctKeywordIds'))
    .drop('distinctKeywordIds')

    # For each keyword (mapped ID), see if at least one unambiguous label maps to it.
    .groupby('pmid', 'pmcid', 'type', 'keywordId')
    .agg(
        min('distinctKeywordIdCountForLabel').alias('minLabelMappingsForKeyword'),
        collect_set('label').alias('distinctLabels')
    )
    .filter(col('minLabelMappingsForKeyword') == 1)
    .withColumn('label', explode('distinctLabels'))
    .drop('distinctLabels', 'minLabelMappingsForKeyword')
)

print('# Filtering run results')
for df, desc in ((matches_mapped, 'Before filtering'), (matches_filtered, 'After filtering')):
    print(f'\n## {desc}')
    distinct_mappings(df)
    app_synonyms(df)
