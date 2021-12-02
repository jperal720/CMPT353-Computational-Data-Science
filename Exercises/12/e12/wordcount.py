import sys
from pyspark.sql import SparkSession, functions, types
from pprint import pprint
import string, re

spark = SparkSession.builder.appName('reddit relative scores').getOrCreate()
spark.sparkContext.setLogLevel('WARN')

assert sys.version_info >= (3, 5) # make sure we have Python 3.5+
assert spark.version >= '2.3' # make sure we have Spark 2.3+


def main(in_directory, out_directory):
    wordbreak = r'[%s\s]+' % (re.escape(string.punctuation),)
    text = spark.read.text(in_directory)
    text = text.select(
        functions.lower(text['value']).alias('value'),
        functions.split(text['value'], wordbreak).alias("split"),
    )
    text = text.select(
        functions.explode(text['split']).alias("words")
    )
    group = text.groupBy(text['words'])
    group = group.agg(
        functions.ltrim(text['words']),
        functions.rtrim(text['words']),
        functions.count(text['words']).alias("count(words)"),
    )
    text = group.select(
        group['words'],
        group['count(words)']
    )

    text = text.sort(text['count(words)'].desc())
    text = text.filter(text.words != "") #Filters out spaces out of words column
    text.write.csv(out_directory, compression=None, mode='overwrite')

if __name__ == '__main__':
    in_directory = sys.argv[1]
    out_directory = sys.argv[2]
    main(in_directory, out_directory)