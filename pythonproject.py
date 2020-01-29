import matplotlib.pyplot as plt
import random
import statistics

students=random.randint(15,25)
chemistry_list=[]
english_list=[]
history_list=[]
recreation_list=[]
physics_list=[]
math_list=[]

def grades(my_list):
    for i in range(students):
        my_grades=random.randint(0,100)
        my_list.append(my_grades)  


grades(chemistry_list)
grades(english_list)
grades(history_list)
grades(recreation_list)
grades(physics_list)
grades(math_list)

totalclasses={"Chemistry":0, "English":0,
              "History":0, "Recreation":0,
              "Physics":0, "Math":0}
totalclasses["Chemistry"]=chemistry_list
totalclasses["English"]=english_list
totalclasses["History"]=history_list
totalclasses["Recreation"]=recreation_list
totalclasses["Physics"]=physics_list
totalclasses["Math"]=math_list

for a in totalclasses:
    print(a, ":" ,totalclasses[a])

def stats(my_statistics):
    stat_sum = sum(my_statistics)
    average = stat_sum / len(my_statistics)    
    if  my_statistics == chemistry_list:
        print ("\nChemistry Stats")
    elif my_statistics == english_list:
        print("\nEnglish Stats")
    elif my_statistics == history_list:
        print("\nHistory Stats")
    elif my_statistics == recreation_list:
        print("\nRecreation Stats")
    elif my_statistics == physics_list:
        print("\nPhysics Stats")
    elif my_statistics == math_list:
        print("\nMath Stats")
        
    print("Max:", max(my_statistics),
          "\nMin:", min(my_statistics),
          "\nAverage:", average,
          "\nMedian:", statistics.median(my_statistics),
          "\nStandard Deviation:", statistics.stdev(my_statistics))
    
stats(chemistry_list)
stats(english_list)
stats(history_list)
stats(recreation_list)
stats(physics_list)
stats(math_list)


plt.ylim(0,100)
plt.xlim(0,students)

student_id=[]
for d in range(students):
    student_id.append(d)

my_xticks=[]
for ppl in student_id:
    studentlabel="Student"
    my_xticks.append(studentlabel+str(ppl+1))

def plot(grade_plot, color, label, marker): 
    plt.scatter(x=student_id, y=grade_plot, color=color,
                label=label, marker=marker)
    plt.xlabel("Students")
    plt.ylabel("Grades")
    
    plt.xticks(student_id, my_xticks, rotation='vertical')
    plt.title('Scatterplot of Student Grades')
  
        
plot(chemistry_list, "g", 'Chemistry', "8")
plot(english_list, "c", 'English', "s")
plot(history_list, "b", 'History', "p")
plot(recreation_list, "r", 'Recreation', "P")
plot(physics_list, "y", 'Physics', "*")
plot(math_list, "m", 'Math', "X")
plt.legend(loc='upper right')
plt.show()

plt.boxplot(history_list)
plt.xlabel('History')
plt.ylabel('History Grades')
plt.title('History Grades Boxplot')
plt.show()

plt.hist(math_list)
plt.xlabel('Math Grade')
plt.ylabel('Number of students')
plt.title('Math Grades Histogram')
plt.show()

            

