#print('hello')

import csv
Avarages =[];
Firstnames=[];
Surname=[];
with open('input.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    count=0
    for row in csv_reader:
        Firstnames.append(row[0])
        Surname.append(row[1])
        print(row[4])
        if count>0:
            Sum=0; #Initital sum at each row
            for marks in range(2,5):
                Sum = int(row[marks])+Sum;

            Avrge= Sum/4;
            Avarages.append(Avrge)
        count= count+1;

print(Avarages[0])

Grades =[]
for StudentAverage in Avarages:
    if StudentAverage>=80 and StudentAverage<=100:
        Grades.append('A')
    elif StudentAverage>=70 and StudentAverage<79.9:
        Grades.append('B')
    elif StudentAverage>=60 and StudentAverage<69.9:       
        Grades.append('C')
    elif StudentAverage>=50 and StudentAverage<59.9:
       
        Grades.append('D')
    elif StudentAverage>=40 and StudentAverage<49.9:
        
        Grades.append('E')
    else:
        Grades.append('F')


print(Grades[0])

import csv
from itertools import zip_longest
d = [Firstnames,Surname, Avarages, Grades]
export_data = zip_longest(*d, fillvalue = '')
with open('Output.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Firstnames","Surname", "Avarages", "Grades"))
      wr.writerows(export_data)
myfile.close()
