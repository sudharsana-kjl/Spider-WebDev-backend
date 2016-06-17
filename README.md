# Spider-WebDev-backend
First I created a modelForm where i can create and save the form.Then i created a searchform where i can search through the table and display the data with the same roll no.And there is a edit option in the display page where the user can edit the data found after entering the correct passcode.

list of server routes
(it runs on port 8000)
127.0.0.1:8000/admin - displays admin page
127.0.0.1:8000/task -- displays the form and on clicking save it'll display thankks.html if data is valid and it'll be saved
127.0.0.1:8000/task/search -- displays a searchform where u should enter the roll no and if it exists the results are displayed,if the number doesnt exist,it'l display not available
Onclicking edit in the search results page, u'll be directed to 
127.0.0.1:8000/task/11/edit-- (here for example 11 is the primary key/id no of the data displayed)
a form is added in this page which asks for passcode
After editing with valid data,when the user clicks on submit, if the passcode entered matches the original passcode,Success mesage will be displayed, else failure message will be displayed.

BUILD INSTRUCTIONS:

u can download django from this site: https://www.djangoproject.com/download/
then download the file named 'spider' in my repository and copy and paste it in the django directory in ur c:// drive
then go to Windows power shell
and go into the spider directory
(for eg: cd C://django/spider)
and run the command "python manage.py runserver"
copy the link displayed in ur browser and press enter
now add "/task" to the url to create form
add "/task/search" to search the database

![Alt text](https://github.com/sudharsana-kjl/Spider-WebDev-backend/blob/master/spider/Screenshot%20(176).png)
![Alt text](https://github.com/sudharsana-kjl/Spider-WebDev-backend/blob/master/spider/Screenshot%20(177).png)
![Alt text](https://github.com/sudharsana-kjl/Spider-WebDev-backend/blob/master/spider/Screenshot%20(179).png)
![Alt text](https://github.com/sudharsana-kjl/Spider-WebDev-backend/blob/master/spider/Screenshot%20(180).png)
![Alt text](https://github.com/sudharsana-kjl/Spider-WebDev-backend/blob/master/spider/Screenshot%20(181).png)
![Alt text](https://github.com/sudharsana-kjl/Spider-WebDev-backend/blob/master/spider/Screenshot%20(182).png)
![Alt text](https://github.com/sudharsana-kjl/Spider-WebDev-backend/blob/master/spider/Screenshot%20(183).png)
![Alt text](https://github.com/sudharsana-kjl/Spider-WebDev-backend/blob/master/spider/Screenshot%20(184).png)
![Alt text](https://github.com/sudharsana-kjl/Spider-WebDev-backend/blob/master/spider/Screenshot%20(185).png)
![Alt text](https://github.com/sudharsana-kjl/Spider-WebDev-backend/blob/master/spider/Screenshot%20(186).png)
![Alt text](https://github.com/sudharsana-kjl/Spider-WebDev-backend/blob/master/spider/Screenshot%20(187).png)
![Alt text](https://github.com/sudharsana-kjl/Spider-WebDev-backend/blob/master/spider/Screenshot%20(188).png)
![Alt text](https://github.com/sudharsana-kjl/Spider-WebDev-backend/blob/master/spider/Screenshot%20(189).png)
![Alt text](https://github.com/sudharsana-kjl/Spider-WebDev-backend/blob/master/spider/Screenshot%20(190).png)
![Alt text](https://github.com/sudharsana-kjl/Spider-WebDev-backend/blob/master/spider/Screenshot%20(191).png)
![Alt text](https://github.com/sudharsana-kjl/Spider-WebDev-backend/blob/master/spider/Screenshot%20(192).png)

