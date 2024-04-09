The Process-


To make the website and database run sucessfully, in your windows system, make sure you have installed Pymongo, mongoDB as well as mongoDB compass in cmd. After extracting the files, type cd and go to the directory in which all the files are stored in,setting that as your path. Then type 'mongod' in cmd and then subsequently type 'python attendance_server1.py'. Make sure the .py file is copy pasted to the expected directory( in case of an error in finding file directory after the 'python attendance_server1.py' command). Don't close the cmd until the entire process is over. Run the 'index1.html' file in live server and open the website, which allows for inner pages( clicking on 'attendance' under Michael's profile or 'Mark attendance' in each of the employees info under the employee database) to open up an attendance form where EMP ID can be seen. Filling in that attribute will result in changes in 'attendance_db' and 'attendance_records' which are created and can be seen in mongodb compass. To access that, open mongodb compass and connect with the local host which has the url "mongodb://localhost:27017" and then you can view the database as well as the attendance submitted by the employees in real time. The attendance records can be viewed on the website as well once you click on submit button after giving in the employee id.

Credits:
Template Name: Bethany
Template URL: https://bootstrapmade.com/bethany-free-onepage-bootstrap-theme/
Author: BootstrapMade.com
License: https://bootstrapmade.com/license/