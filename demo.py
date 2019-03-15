import pymysql.cursors

# Open database connection
db = pymysql.connect("localhost","root","","contact" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
sql = 'SELECT * FROM `form`;'
cursor.execute(sql);

# Fetch a single row using fetchone() method.
countrow = cursor.execute(sql)
print ("Dddon :  " ,countrow)

#mendapatkan semua
#data = cursor.fetchall()
#print(data)


#mendapatkan satu per satu
results = cursor.fetchall()
for row in results:
      first_name = row[0]
      last_name = row[1]
      country = row[2]
      email = row[3]
      zip = row[4]
      # Now print fetched result
      print "Nama Awal=%s,Nama Belakang=%s,Kewarganegaraan=%s,email=%s,zip=%s" % \
             (first_name, last_name, country, email, zip)


# disconnect from server
db.close()