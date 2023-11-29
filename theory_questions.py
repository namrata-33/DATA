Question 0. We don’t expect you to have any cricket knowledge and that is not a requirement to ace this assessment. But we understand that familiarity with cricket may vary from one candidate to the next so we would like to know how you would rate your knowledge of cricket from 1 to 5, where 1 is basically no knowledge (like you had never seen or read anything about the sport until the days before this assessment) and 5 is highly knowledgeable (you watch matches regularly and have a jersey for the Rajasthan Royals in your closet, for example).



  My knowledge of cricket is at a level 1 out of 5. I have some basic awareness of the sport.I might know all the rules and regulation to play cricket.



Question 3. Please provide a brief written answer to the following question. The coding assessment focused on a batch backfilling use case. If the use case was extended to required incrementally loading new match data on a go-forward basis, how would your solution change?


  If the use case were extended to require incrementally loading new match data on a go-forward basis, the solution would need to incorporate real-time data ingestion and update processes. The following changes would be necessary:

  Instead of batch processing, the system would need to subscribe to real-time data streams provided by sources like cricsheet.org or other cricket data providers like logstash,kafka,spark streaming.

  Real-time data may arrive in different formats or structures than batch data. Dynamically set the data reading and flattening the data so cannot get issue whenever data format or structure has been changed.

  Dependencies such as database schema changes, monitoring, and alerting systems should be adapted to accommodate real-time data.

  Ensure low latency,code reusability,need performance optimization, including database indexing and query tuning for real-time use cases.


Question 4. Can you provide an example of when, during a project or analysis, you learned about (or created) a new technique, method, or tool that you hadn’t known about previously? What inspired you to learn about this and how were you able to apply it?


  In project, I learned many new technlogies which has been more useful in real time data handling, data transformation and handling big data issue.

  I have use PySpark,SQL,Hive,Presto to data extraction, data cleaning, data transformation and loading in various databases like MySQL, PostgrSQL, ORACLE.

  I have created CI/CD pipeline to maintain code versions in GitHub using jenkis.

  I have done some work in kafka to extract data from various databases and dump it into again various databases.
