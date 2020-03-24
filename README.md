# Database-Connection_Using-Python-pymysql-
This Project Consists Of An Simple Database Application Using Python's Tkinter
Requirements:
    1.Xammp Server
    2.HeidiSql[Note:-To See The Database if you dont want to open and see the database online each time on phpmyadmin]
    Python Packages:
        a.{pymysql} For SQL Database
        b.{Pillow} For Loading Images On Window
        c.{smtplib} For Sending Mails 



Procedure And Steps:
    1.Unzip The Folder Where you want to but remember to change the image path of CrizalBlumeForestDB.py by opening it and paste the path inside the Image.open(path_file)
    For eg:-"""Image.open("D:/Update Drive/Blume/Python/Tkinter Apps/Database/Login/Leopard.jpg")"""...Here My File Is in D Drive 
    2.In Xammp,Start The Apache and MySQL Services By Clicking The Start
    3.Load The {ang08_details.sql} in Xammp By Going on http://localhost:8080/phpmyadmin/ or http://localhost/phpmyadmin/ 
    [Note:Incase Any Error Occours In Localhost Connection,Kindly Google,Youtube The Configugration Of Localhost Connection Methods Of Xampp,Because For Every System its Different]
    4.[Optional] Install HeidiSql depending on your OS from https://www.heidisql.com/download.php
    [Note:4th Step is Optional.This is to see the database without connection to phpmyadmin but Xammp is manadatory and 2nd Step also]
    5.After All The Steps Are Completed,Run The Python File {CrizalBlumeForestDB.py}
