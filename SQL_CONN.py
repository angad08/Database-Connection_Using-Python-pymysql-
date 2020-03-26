import pymysql
def Main_SQL():
	c=3;
# Open database connection
	db = pymysql.connect("localhost","root","","phy_py");
# prepare a cursor object using cursor() method
	rs = db.cursor();
	#Relese Applicable Only When Table In Database Doesn't Exist
	# sqlite_py="CREATE TABLE IF NOT EXISTS phyrusspy_details(ID INT PRIMARY KEY AUTO_INCREMENT,FIRST_NAME CHAR(100),LAST_NAME CHAR(100),AGE INT(90),SEX CHAR(40),INCOME DOUBLE)"
	# rs.execute(sqlite_py)
	def Insert_Data():
		I_Fname=input("First_Name:")
		I_Lname=input("Last_Name")
		I_Sex=input("Sex:")
		I_Income=input("Income")
		I_Age=int(input("Age:"))
		sql = "INSERT INTO phyrusspy_details(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME) VALUES ('{}', '{}', '{}', '{}','{}')".format(I_Fname,I_Lname,I_Age,I_Sex,I_Income)
		sql1 = "SELECT * FROM phyrusspy_details"
   # Execute the SQL command
		rs.execute(sql)
		db.commit();
		rs.execute(sql1)
		db.commit();
   # Fetch all the rows in a list of lists.
		results = rs.fetchall()
		print("\n\nINSERT QUERY\n\n");
		print("ID\t\tFirst_Name\tLast_Name\tAge\t\tSex\t\tIncome")
		for row in results:
			id=row[0]
			fname = row[1]
			lname = row[2]
			age = row[3]
			sex = row[4]
			income = row[5]
      # Now print fetched result
			print ("%d\t\t%s\t\t%s\t\t%d\t\t%s\t\t%s"%(id,fname, lname, age, sex, income ))

 # disconnect from server
		# db.close()
	
	def Update_Data():
		S_Fname=str(input("Set First Name:"))
		S_Lname=str(input("Set Last Name:"))
		S_Age=int(input("Set Age:"))
		S_Sex=str(input("Set Sex:"))
		S_Income=float(input("Set Income:"))
		R_ID=int(input("Enter ID of Employee:"))
		R_Fname=str(input("Replace First Name:"))
		R_Lname=str(input("Replace Last Name:"))
		R_Age=int(input("Replace Age:"))
		R_Sex=str(input("Replace Sex:"))
		R_Income=float(input("Replace Income:"))
		sql = "UPDATE phyrusspy_details SET FIRST_NAME='%s',LAST_NAME='%s',AGE='%d',SEX='%c',INCOME='%f' WHERE ((FIRST_NAME='%s' AND LAST_NAME='%s' AND ID='%d') OR ID='%d')"%(S_Fname,S_Lname,S_Age,S_Sex,S_Income,R_Fname,R_Lname,R_ID,R_ID)
		sql1 = "SELECT * FROM phyrusspy_details"
		try:
   # Execute the SQL command
			rs.execute(sql)
			db.commit()
			rs.execute(sql1)
			db.commit()
   # Fetch all the rows in a list of lists.
			results = rs.fetchall()
			print("\n\nUPDATE QUERY:\n\n");
			print("ID\t\tFirst_Name\tLast_Name\tAge\t\tSex\t\tIncome")
			for row in results:
				id=row[0]
				fname = row[1]
				lname = row[2]
				age = row[3]
				sex = row[4]
				income = row[5]
      # Now print fetched result
				print ("%d\t\t%s\t\t%s\t\t%d\t\t%s\t\t%f"%(id,fname, lname, age, sex, income ))
		except:
			db.rollback();
			print ("Error: unable to fetch data")

# # disconnect from server
		# db.close()
	def Select_Data():
		sql = "SELECT * FROM phyrusspy_details"
   # Execute the SQL command
		rs.execute(sql)
		db.commit();
   # Fetch all the rows in a list of lists.
		results = rs.fetchall();
		if(len(results) is 0):
			print("No Data To Display")
			exit()
		else:
			print("SELECT QUERY\n\n");
			print("ID\t\tFirst_Name\tLast_Name\tAge\t\tSex\t\tIncome")
			for row in results:
				id=row[0]
				fname = row[1]
				lname = row[2]
				age = row[3]
				sex = row[4]
				income = row[5]
				
		# # Now print fetched result
				print ("%d\t\t%s\t\t%s\t\t%d\t\t%s\t\t%f"%(id,fname, lname, age, sex, income ))

# # disconnect from server
		# db.close()	
	def Delete_Data():
		dip=int(input("Enter The Id No Of Row To Erase The Data:"))
		sql = "DELETE FROM phyrusspy_details WHERE ID=%d"%(dip)
		sql1 = "SELECT * FROM phyrusspy_details"
		try:
   # Execute the SQL command
			rs.execute(sql)
			db.commit()
			rs.execute(sql1)
			db.commit()
   # Fetch all the rows in a list of lists.
			results = rs.fetchall()
			print("\n\nUPDATE QUERY:\n\n");
			print("ID\t\tFirst_Name\tLast_Name\tAge\t\tSex\t\tIncome")
			for row in results:
				id=row[0]
				fname = row[1]
				lname = row[2]
				age = row[3]
				sex = row[3]
				income = row[5]
      # Now print fetched result
				print ("%d\t\t%s\t\t%s\t\t%d\t\t%s\t\t%f"%(id,fname, lname, age, sex, income ))
		except:
			db.rollback();
			print ("Error: unable to fetch data")

# # disconnect from server
	# db.close()
	while(True):
		
		print("\n1.Display_Data\n2.Insert_Data\n3.Update_Data\n4.Delete_Data\n5.Exit");
		choice=int(input("Enter Choice From Aboove:"));
		if(choice==1):
			Select_Data();
		elif(choice==2):
			Insert_Data();
		elif(choice==3):
			Update_Data();
		elif(choice==4):
			Delete_Data();
		elif(choice==5):
			print("Exitted Successfully");
		# disconnect from server
			db.close();
			return 0;
		else:
			print("Invalid Input");
		ans=input("Enter # to Exit:")
		if(ans=="#"):
			break;
if __name__=="__main__":
	Main_SQL();