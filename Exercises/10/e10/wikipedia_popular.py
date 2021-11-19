import sys
from pyspark.sql import SparkSession, functions, types

spark = SparkSession.builder.appName('reddit averages').getOrCreate()
spark.sparkContext.setLogLevel('WARN')

assert sys.version_info >= (3, 5) # make sure we have Python 3.5+
assert spark.version >= '2.3' # make sure we have Spark 2.3+

def transform_filename(input):

    print(type(input))
    return input


def main(in_directory, out_directory):
    pages = spark.read.csv(in_directory, inferSchema=True).withColumn('filename', functions.input_file_name())

    pages = pages.select(
        pages['_c0'].alias('Name'),
        pages['filename'].alias('Filename')
    )
    pages.withColumn("Filename", transform_filename("Filename"))

if __name__=='__main__':
    in_directory = sys.argv[1]
    out_directory = sys.argv[2]
    main(in_directory, out_directory)