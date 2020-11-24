!apt-get -y install openjdk-8-jre-headless
!pip install pyspark

# the pyaddfile only look into the jars file, so we need to put the file inside the jars file, both in pyspark and in full spark
# Note: I don't know why I need two file in these two place LOL
!curl -L -o "/usr/local/lib/python3.6/dist-packages/pyspark/jars/graphframes-0.8.1-spark3.0-s_2.12.jar" \
http://dl.bintray.com/spark-packages/maven/graphframes/graphframes/0.8.1-spark3.0-s_2.12/graphframes-0.8.1-spark3.0-s_2.12.jar
!wget http://dl.bintray.com/spark-packages/maven/graphframes/graphframes/0.8.1-spark3.0-s_2.12/graphframes-0.8.1-spark3.0-s_2.12.jar

from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
spark = SparkSession.builder.master("local").getOrCreate()
sc = SparkContext.getOrCreate()


sc.addPyFile('./graphframes-0.8.1-spark3.0-s_2.12.jar')


from graphframes import *
from pyspark.sql.functions import *