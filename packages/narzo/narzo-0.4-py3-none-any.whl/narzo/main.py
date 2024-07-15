import argparse

def hello():
    print("Hello, World! i am testing")

def pro7():
    print("pip install pyspark\n")
    print("import pyspark \n from pyspark.sql import SparkSession \n spark=SparkSession.builder.appName('housing_price_model').getOrCreate()\n df=spark.read.csv('7th_prog_dataset.csv',inferSchema=True,header=True)\ndf.show(10)\n")
    print("\n")
    print("from pyspark.ml.feature import StringIndexer \n indexer=StringIndexer(inputCol='Cruise_line',outputCol='cruise_cat')\n indexed=indexer.fit(df).transform(df)\n for item in indexed.head(5):\n   print(item)\n   print('\ n')\n")
    print("\n")
    print("from pyspark.ml.linalg import Vectors\nfrom pyspark.ml.feature import VectorAssembler\nassembler=VectorAssembler(inputCols=['Age','Tonnage','passengers','length','cabins','passenger_density','cruise_cat'],outputCol='features')\noutput=assembler.transform(indexed)\noutput.select('features','crew').show(5)\n")
    print("\n")
    print("final_data=output.select('features','crew')\ntrain_data,test_data=final_data.randomSplit([0.7,0.3])\ntrain_data.describe().show()\n")
    print("\n")
    print("test_data.describe().show()\n")
    print("\n")
    print("from pyspark.ml.regression import LinearRegression\nship_lr=LinearRegression(featuresCol='features',labelCol='crew')\ntrained_ship_model=ship_lr.fit(train_data)\nship_results=trained_ship_model.evaluate(train_data)\nprint('Rsquared Error :',ship_results.r2)\n")
    print("\n")
    print("unlabeled_data=test_data.select('features')\nunlabeled_data.show(5)\n")
    print("\n")
    print("predictions=trained_ship_model.transform(unlabeled_data)\npredictions.show()\n")

def pro2():
    print("import java.io.IOException;\nimport org.apache.hadoop.io.IntWritable;\nimport org.apache.hadoop.io.LongWritable;\nimport org.apache.hadoop.io.Text;\nimport org.apache.hadoop.mapred.*;\npublic class WCMapper extends MapReduceBase implements Mapper<LongWritable, Text , Text, IntWritable>{\npublic void map(LongWritable key, Text value, OutputCollector<Text  ,IntWritable> output , Reporter rep)throws IOException{\nString line = value.toString();\nfor(String word:line.split(" ")){\nif(word.length() > 0){\noutput.collect(new Text(word) ,new IntWritable(1));\n}}}}")
    print("\n")
    print("import java.io.*;\nimport java.util.*;\nimport org.apache.hadoop.io.*;\nimport org.apache.hadoop.mapred.*;\npublic class WCReducer extends MapReduceBase implements Reducer<Text, IntWritable, Text, IntWritable>{\npublic void reduce(Text key, Iterator<IntWritable> value, OutputCollector<Text, IntWritable> output, Reporter rep) throws IOException{\nint count = 0;\nwhile (value.hasNext()){\nIntWritable i = value.next();\ncount += i.get(); }\noutput.collect(key, new IntWritable(count)); }}")
    print("\n")
    print("import java.io.IOException;\nimport org.apache.hadoop.conf.Configured;\nimport org.apache.hadoop.fs.Path;\nimport org.apache.hadoop.io.IntWritable;\nimport org.apache.hadoop.io.Text;\nimport org.apache.hadoop.mapred.FileInputFormat;\nimport org.apache.hadoop.mapred.FileOutputFormat;\nimport org.apache.hadoop.mapred.JobClient;\nimport org.apache.hadoop.mapred.JobConf;\nimport org.apache.hadoop.util.Tool;\nimport org.apache.hadoop.util.ToolRunner;\npublic class WCDriver extends Configured implements Tool {\npublic int run(String args[]) throws IOException{\nJobConf conf = new JobConf(WCDriver.class); 		\nFileInputFormat.setInputPaths(conf, new Path(args[0])); 		\nFileOutputFormat.setOutputPath(conf, new Path(args[1])); 	\nconf.setMapperClass(WCMapper.class); \nconf.setReducerClass(WCReducer.class); \nconf.setMapOutputKeyClass(Text.class); \nconf.setMapOutputValueClass(IntWritable.class); \nconf.setOutputKeyClass(Text.class); \nconf.setOutputValueClass(IntWritable.class);\nJobClient.runJob(conf);\nreturn 0;}\npublic static void main(String args[]) throws Exception{\nint exitCode = ToolRunner.run(new WCDriver(), args);\nSystem.out.println(exitCode);}}")

def pro3():
    print("import java.io.IOException;\nimport org.apache.hadoop.io.LongWritable;\nimport org.apache.hadoop.io.Text;\nimport org.apache.hadoop.io.IntWritable;\nimport org.apache.hadoop.mapreduce.Mapper;\npublic class MaxTempMapper extends Mapper<LongWritable, Text, Text, IntWritable>{\npublic void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException{\nString line=value.toString();\nString year=line.substring(15,19);\nint airtemp;\nif(line.charAt(87)== '+'){\nairtemp=Integer.parseInt(line.substring(88,92));\n}else\nairtemp=Integer.parseInt(line.substring(87,92));\nString q=line.substring(92,93);\nif(airtemp!=9999&&q.matches(quotes[01459]quotes)){\ncontext.write(new Text(year),new IntWritable(airtemp));}}}")  # Add closing parenthesis here
    print("\n")
    print("import java.io.IOException;\nimport org.apache.hadoop.io.Text;\nimport org.apache.hadoop.io.IntWritable;\nimport org.apache.hadoop.mapreduce.Reducer;\npublic class MaxTempReducer extends Reducer<Text, IntWritable, Text, IntWritable>{\npublic void reduce(Text key, Iterable<IntWritable> values, Context context)throws IOException, InterruptedException{\nint maxvalue=Integer.MIN_VALUE;\nfor (IntWritable value : values) {\nmaxvalue=Math.max(maxvalue, value.get());}\ncontext.write(key, new IntWritable(maxvalue));\n}}")
    print("\n")
    print("import org.apache.hadoop.conf.Configuration;\nimport org.apache.hadoop.fs.Path;\nimport org.apache.hadoop.io.IntWritable;\nimport org.apache.hadoop.io.Text;\nimport org.apache.hadoop.mapreduce.Job;\nimport org.apache.hadoop.mapreduce.lib.input.FileInputFormat;\nimport org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;\npublic class maxtemperature {\npublic static void main(String[] args) throws Exception {\nConfiguration conf = new Configuration();\nJob job = Job.getInstance(conf, quotes maxtemperature quotes);\njob.setJarByClass(maxtemperature.class);\njob.setMapperClass(MaxTempMapper.class);\njob.setReducerClass(MaxTempReducer.class);\njob.setOutputKeyClass(Text.class);\njob.setOutputValueClass(IntWritable.class);\nFileInputFormat.setInputPaths(job, new Path(args[0]));\nFileOutputFormat.setOutputPath(job, new Path(args[1]));\nif (!job.waitForCompletion(true))\nreturn;}}")

def pro5():
    print("hadoop fs -put movies.csv 226.csv\nhive\ncreate table if not exists ratings(userid string, movieid string, rating string, 'timestamp' string) row format delimited fields terminated by ',';\ncreate table if not exists movies(id int, name string, genre string) row format delimited fields terminated by ',';\nload data local inpath 'ratings.csv' into table ratings;\nload data local inpath 'movies.csv' into table movies;\n#a select movie_id, avg(rating) as avg_rating from ratings group by movie_id order by avg_rating desc limit 1;\n#b select user_id, count(*) as num_ratings from ratings group by user_id order by num_ratings desc limit 10;\n#c assuming a positive rating is 4 or 5: select movie_id, count(*) as positive_ratings from ratings where rating >= 4 group by movie_id order by positive_ratings desc limit 10;\n")

def pro6():
    print("pip install pyspark\n")
    print("from pyspark.sql import SparkSession\nspark = SparkSession.builder.appName(QUOTESMovieRatingsAnalysisQUOTES).getOrCreate()\nmovies_df = spark.read.csv(QUOTES/Users/amithpradhaan/Desktop/ml-latest-small/movies.csvQUOTES, header=True, inferSchema=True)\nratings_df = spark.read.csv(QUOTES/Users/amithpradhaan/Desktop/ml-latest-small/ratings.csvQUOTES, header=True, inferSchema=True)\nmovies_rdd = movies_df.rdd\nratings_rdd = ratings_df.rdd\n\n")
    print("avg_ratings_rdd = ratings_rdd.map(lambda x: (x['movieId'], (x['rating'], 1))) \ \n    .reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1])) \ \n    .mapValues(lambda x: x[0] / x[1])\nlowest_avg_rating = avg_ratings_rdd.sortBy(lambda x: x[1]).first()\nprint(fQUOTESMovie with the lowest average rating: {lowest_avg_rating}QUOTES)\n\n")
    print("user_ratings_count = ratings_rdd.map(lambda x: (x['userId'], 1)) \ \n    .reduceByKey(lambda x, y: x + y) \ \n    .sortBy(lambda x: x[1], ascending=False)\ntop_users = user_ratings_count.take(10)\nprint(fQUOTESTop users by number of ratings: {top_users}QUOTES\n\n")
    print("from pyspark.sql.functions import from_unixtime, year, month\nratings_df = ratings_df.withColumn(QUOTESyearQUOTES, year(from_unixtime(ratings_df['timestamp']))) \ \n                       .withColumn(QUOTESmonthQUOTES, month(from_unixtime(ratings_df['timestamp'])))\nratings_over_time = ratings_df.groupBy(QUOTESyearQUOTES, QUOTESmonthQUPTES).count().orderBy(QUOTESyearQUOTES, QUOTESmonthQUOTES)\nratings_over_time.show()\n\n")
    print("movie_ratings_stats = ratings_rdd.map(lambda x: (x['movieId'], (x['rating'], 1))) \ \n    .reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1])) \ \n    .mapValues(lambda x: (x[0] / x[1], x[1]))  # (avg_rating, count)\nmin_ratings = 100\nqualified_movies = movie_ratings_stats.filter(lambda x: x[1][1] >= min_ratings)\nhighest_rated_movies = qualified_movies.sortBy(lambda x: x[1][0], ascending=False).take(10)\nprint(fQUOTESHighest-rated movies with at least {min_ratings} ratings: {highest_rated_movies}QUOTES)\n\n")

def main():
    parser = argparse.ArgumentParser(description='My Library Command Line Tool')
    parser.add_argument('--prog2', type=str, help='A foo argument')
    parser.add_argument('--prog3', type=str, help='A bar argument')
    args = parser.parse_args()

    if args.prog2:
        pro2()
    if args.prog3:
        pro3()

