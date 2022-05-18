Using  the Python  programming  language,  and  starting  with  the  completed  solution  to  the  M7 exercise 
„Practice with pandas module“, make the following modification and additions. 
− Add the column „Pass“ that indicates if the user passed the exam, based on the minimum score. 
The exam is passed if the user has at least 15 points in the minimum score column. 
− Add the column „Grade“ that indicates the grade of the user based on the average score. Grade 
can be A, B, C, D or F. Define the points range for every grade. The user that failed the exam 
(column „Pass“ has a value False) must have a grade F. 
− Draw a plot showing how the grade depends on the user’s gender. 
− Filter the table to show all negative minimum scores and count the number of negative 
minimum grades. 
− Represent all grades as a numpy array. Using the numpy module, sort the scores. 
− Using the Counter collection, count the number of each grade. 
− Calculate the average maximum and average minimum for each grade. 
− Using the final modified table, create a class that represents a User containing all the fields 
represented in the table. 
o A constructor should load the table from the given .csv file. 
o Write appropriate getter and setter methods. 
o Overload the len operator to get the total count of users. 
o Overload the indexing operator to get access to a particular user based on its key. 
o Overload the __str__ method to print the User’s characteristics - Sex, average score, 
grade and indication if the user has passed the exam.  
− Write a test class that tests all methods from the User class. 
