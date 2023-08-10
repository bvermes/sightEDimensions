# sight-E Dimensions
This was initially an interview assigment.  The assignment did not require creating an application initially.
I just had to answer some of the questions, but I did not had the necessary skills to do so. Therefore, I decided to create a test script to learn.
So in the documentation I  will include a seperate chapter answering them.
# Skills learned
I learned a lot about PostgreSQL, basic python scripting, making RESTful APIs and handling XML and JSON data in Python.
# Overview
The given part of the project was to write a program with the given parameters:
* Source: XML API endpoint.
* Storing: PostgreSQL database.
* Frequency:Every hour, data is available after 15 minutes, with possible delay (up to 30 minutes).
* Data: 4 columns containing dimensions, 1 column containing the intersection values of dimensions.
* Data retrieval can scale relatively quickly, with even 1-200 similar requests possible per hour within 2 months.
* The framework may expand later with JSON-based REST APIs and CSV data sources.
* Changes in data retrieval can occur, e.g., modifications to the data schema.

Goals:
* Scalability
* Trackability
* Cost optimalization

# Questions
What possible solutions were considered?

How did you evaluate them based on specific criteria?

Regarding these criteria, how did each alternative solution perform?

Why did you choose the solution you chose?

Would your solution change if web-scraped input data also needed to be utilized? If yes, how?


# Note
Given that I had only one day to complete the project, there might be errors.

Prior programming I had a learning day, where I mostly watched the following useful udemy course: https://www.udemy.com/course/complete-python-postgresql-database-course/

Most likely many of the 'ACID' properties does not function as it should be, and due to time constraints,I didn't take extra care to solve all the specified goals.

Sources: 
https://www.psycopg.org/docs/usage.html#with-statement
https://www.udemy.com/course/complete-python-postgresql-database-course/
postgre-server: https://api.elephantsql.com/
https://roytuts.com/how-to-return-different-response-formats-json-xml-in-flask-rest-api/
https://stackoverflow.com/questions/50121539/run-function-at-a-specific-time-in-python
