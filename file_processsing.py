#to read file 
myfile = open("fruits.txt","r")
print(myfile.read()) #read the file but the cursor at last row
#read file multi times
content=myfile.read()
print(content)
print(content)
print(content)
#you must colse your file
myfile.close()

#the best way to open a file
with open('fruits.txt') as myfile2:
    content2=myfile2.read
#the close here is auto
#write a file
with open('fruits.txt','w') as myfile2:
    myfile2.write('pear\napple\norange\nmandarin\nwatermelon\npomegranate\ntommato')
#append
with open('fruits.txt','a') as myfile2:
    myfile2.write('\nbanana')
#a+ for read and append
myfile.seek(0)
#to make the coursor at zero possition
