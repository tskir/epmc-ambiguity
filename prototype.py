#!/usr/bin/env python3

import argparse

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, collect_set, count, countDistinct, explode, size, struct, when, min


def distinct_mappings(dfs):
    print('# Total number of distinct label to keyword mappings')
    for df, df_desc in dfs:
        print(f'\n## {df_desc}')
        print(
            df
            .groupby('type')
            .agg(size(collect_set(struct('label', 'keywordId'))))
            .toPandas()
            .to_markdown()
        )


def p55_stats(dfs):
    print('\n\n\n# p55 mapping counts')
    for df, df_desc in dfs:
        print(f'\n## {df_desc}')

        total_distinct_pmids = (
            df
            .filter(col('type') == 'GP')
            .filter(col('label') == 'p55')
            .select('pmid')
            .distinct()
            .count()
        )
        print(f'Total number of distinct PMIDs containing at least one p55 mapping: **{total_distinct_pmids}.**\n')

        print(
            df
            .filter(col('type') == 'GP')
            .filter(col('label') == 'p55')
            .groupby('keywordId')
            .agg(size(collect_set('pmid')))
            .toPandas()
            .to_markdown()
        )


def app_synonyms(dfs):
    print('\n\n\n# Global list of APP gene synonyms (ENSG00000142192)')
    for df, df_desc in dfs:
        print(f'\n## {df_desc}')
        print(
            df
            .filter(col('type') == 'GP')
            .filter(col('keywordId') == 'ENSG00000142192')
            .select('label')
            .distinct()
            .toPandas()
            .to_markdown()
        )


parser = argparse.ArgumentParser()
parser.add_argument('--matches', help='Path to the `matches` dataset')
parser.add_argument('--filtered-output', help='Output directory path where the filtered matches will be saved to')
args = parser.parse_args()

spark = (
    SparkSession
    .builder
    .appName('epmc_ambiguity')
    .config("spark.executor.memory", '200G')
    .config("spark.driver.memory", '200G')
    .getOrCreate()
)
matches = spark.read.parquet(args.matches)
matches_mapped = matches.filter(col('isMapped') == True)

matches_filtered = (
    matches_mapped

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
    .drop('distinctLabels', 'minLabelMappingsForKeyword', 'distinctKeywordIdCountForLabel')
    .distinct()
)

# Output the filtered matches dataset.
(
    matches_mapped
    .join(matches_filtered, how='inner', on=['pmid', 'pmcid', 'type', 'label', 'keywordId'])
    .write.format('parquet').save(args.filtered_output)
)

dfs = (
    (matches_mapped, 'Before filtering'),
    (matches_filtered, 'After filtering'),
)
distinct_mappings(dfs)
p55_stats(dfs)
app_synonyms(dfs)
