import sys
from pyspark.sql import SparkSession, functions, types, Row
import re
from pprint import pprint

spark = SparkSession.builder.appName('correlate logs').getOrCreate()
spark.sparkContext.setLogLevel('WARN')

assert sys.version_info >= (3, 5) # make sure we have Python 3.5+
assert spark.version >= '2.3' # make sure we have Spark 2.3+

line_re = re.compile(r"^(\S+) - - \[\S+ [+-]\d+\] \"[A-Z]+ \S+ HTTP/\d\.\d\" \d+ (\d+)$")


def line_to_row(line):
    """
    Take a logfile line and return a Row object with hostname and bytes transferred. Return None if regex doesn't match.
    """
    m = line_re.match(line)
    if m:
        arr_split = []
        arr_split = line.split()
        hostname = arr_split[0]
        bytes = arr_split[len(arr_split) - 1] #returning last element

        return Row(hostname=str(hostname), bytes=int(bytes))
    else:
        return None


def not_none(row):
    """
    Is this None? Hint: .filter() with it.
    """
    return row is not None


def create_row_rdd(in_directory):
    log_lines = spark.sparkContext.textFile(in_directory)
    rows = log_lines.map(line_to_row).filter(not_none)

    return rows


def main(in_directory):
    logs = spark.createDataFrame(create_row_rdd(in_directory))
    # logs.show()

    hostname_group = logs.groupBy(logs['hostname'])

    hostname_group = hostname_group.agg(
        functions.count(logs['hostname']).alias("sum(x)"),
        functions.pow(functions.count(logs['hostname']), 2).alias("squared(sum(x))"),
        functions.sum(logs['bytes']).alias("sum(y)"),
        functions.pow(functions.sum(logs['bytes']), 2).alias("squared(sum(y))")
    )

    values = hostname_group.select(
        hostname_group["sum(x)"],
        hostname_group["squared(sum(x))"],
        hostname_group["sum(y)"],
        hostname_group["squared(sum(y))"],
        hostname_group["sum(x)"] * hostname_group["sum(y)"]
    )

    values = values.withColumn("1", functions.lit(1))
    values.show()
    # TODO: calculate r.
    six_sums = values.groupBy()
    six_sums = six_sums.agg(
        functions.first()
    )
    df = six_sums.select(
        six_sums['sum(x)']
    )

    sf.show()

    r = 0 # TODO: it isn't zero.
    print("r = %g\nr^2 = %g" % (r, r**2))


if __name__=='__main__':
    in_directory = sys.argv[1]
    main(in_directory)
