import sys
import re
import pandas as pd
from datetime import datetime
from pyspark.sql import SparkSession, functions, types

spark = SparkSession.builder.appName('reddit averages').getOrCreate()
spark.sparkContext.setLogLevel('WARN')

assert sys.version_info >= (3, 5) # make sure we have Python 3.5+
assert spark.version >= '2.3' # make sure we have Spark 2.3+

comments_schema = types.StructType([
    types.StructField('language', types.StringType()),
    types.StructField('Name', types.StringType()),
    types.StructField('request', types.IntegerType()),
    types.StructField('bytes', types.LongType()),
])

def main(in_directory, out_directory):
    pagesDF = spark.read.csv(in_directory, schema=comments_schema, sep=' ').withColumn('filename', functions.input_file_name())

    pagesDF = pagesDF.withColumn("NewFilename", udf(pagesDF['filename']))
    pagesDF = pagesDF.drop(pagesDF["filename"])
    pagesDF = pagesDF.cache()
    groups = pagesDF.sort(pagesDF['request'].desc())   #Sorting in descending order
    groups = groups.filter(groups.language.eqNullSafe('en'))

    groups

def path_to_hour(input):
    input = input[-18: -7]
    # input = input.replace('-', ' ')
    # input = input + ':'
    # input = input[0:4] + "/" + input[4:6] + "/" + input[6:]
    # input = datetime.strptime(input, '%y/%m/%d %H:')

    return input

udf = functions.udf(path_to_hour, returnType=types.StringType())

if __name__=='__main__':
    in_directory = sys.argv[1]
    out_directory = sys.argv[2]
    main(in_directory, out_directory)