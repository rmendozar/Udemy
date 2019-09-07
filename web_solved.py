import csv
import os

# we want the tittle, the price, the sucribers
# review, percentage of review, lenght 

#udemy_csv = "./resources/web_starter.csv"
udemy_csv = os.path.join(".","resources","web_starter.csv")


title = []
price = []
subscribers = []
reviews = []
review_percentage=[]
lenght = []

with open(udemy_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    #test = next(csvreader)
    for row in csvreader:
        #add title
        title.append(row[1])
        #add price
        price.append(row[4])
        #add subscribers
        subscribers.append(row[5])
        #add reviews
        reviews.append(row[6])
        #add percentage    
        percent = round(int(row[6])/int(row[5]),2)*100
        review_percentage.append(percent)
        #lenght
        new_lenght = row[9].split(" ")
        lenght.append(float(new_lenght[0]))



merge = zip(title,price,subscribers,reviews,review_percentage,lenght)
file = os.path.join("webFinal.csv")

with open(file,"w") as datafile:
    writer=csv.writer(datafile)
    #add header
    writer.writerow(["Tittle","Price","Subscriber","Reviews","Percentage of Reviews","lenght"])
    #add all the lines for the file that was selected in wth.. open, attention the 's' in rows
    writer.writerows(merge)



#print (review_percentage)
#print (test)


