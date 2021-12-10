# CMPT353-Computational-Data-Science
Everything related to the Computational Data Science course - CMPT353


Commands (macOS) for SFU cluster:\n
1. **Launch**: ssh -p24 <USERID>@cluster.cs.sfu.ca 
2. **Copy**: scp -P 24 [filename] [userid]@cluster.cs.sfu.ca:
3. Show output (local): cat output/* | zless 
4. Show output (cluster): hdfs dfs -cat output/* | zless
