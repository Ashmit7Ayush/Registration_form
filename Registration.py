# first makae the course registration format and subjects


class Registration:
    def FirstSem(self):
        print('Select the Courses ')
        sem_1_dict = {
            'MA101':'Mathematics 1',
            'CS101':'Computer Programming',
            'CS110':'Computer Programming Lab',
            'EC101':'Digital Design',
            'EC110':'Degital Design Lab',
            'EC102':'Electrical Circuit Analysis',
            'HS101':'English'
        }
        selected_sub = ['Sem-->1st      COURSES :-->  ']
        while True:
            print('y/Y for YES','n/N for no')
            for x,y in sem_1_dict.items():
                print(x,y)
                i = input('y/n :-->    ')
                if i == 'y' or i == 'Y':
                    selected_sub.append(x)
                    selected_sub.append(y)
                    selected_sub.append('\t')
                else:
                    pass

            if len(selected_sub) >= 5:
                break
            else:
                print('\n','Please select atleast five subjects','\n')
                selected_sub = []
        return selected_sub
           

    def Second_Sem(self):
        print('Select the Courses')
        sem_2_dict = {
            'MA102':	'Mathematics II',
            'CS103':	'Data Structures',
            'CS111':	'Data Structures Lab',
            'CS104':	'Computer Organization',
            'EC103':	'Basic Electronic Circuits',
            'EC111':	'Basic Electronics Lab',
            'HS102':	'Economics'
        }
        selected_sub = ['Sem--> 2nd     COURSES :-->  ']
        while True:
            print('y/Y for YES','n/N for no')
            for x,y in sem_2_dict.items():
                print(x,y)
                i = input('y/n :-->    ')
                if i == 'y' or i == 'Y':
                    selected_sub.append(x)
                    selected_sub.append(y)
                    selected_sub.append('\t')
                else:
                    pass

            if len(selected_sub) >= 5:
                break
            else:
                print('\n','Please select atleast five subjects','\n') 
                selected_sub = []
        return selected_sub

    def Third_Sem(self):
        print('Select the Courses')
        sem_3_dict = {
            'MA203':	'Mathematics III',
            'MA205':	'Discrete Mathematics',
            'CS201':	'Algorithms',
            'CS210':	'Algorithm Lab',
            'CS221':	'Data Communication',
            'CS202':	'IT Workshop I',
            'SC201':	'Physics I',
            'HS301':	'Macroeconomic Problems and Policies'
        }

        selected_sub = ['Sem:-> 3rd     COURSES :-->  ']
        while True:
            print('y/Y for YES','n/N for no')
            for x,y in sem_3_dict.items():
                print(x,y)
                i = input('y/n :-->    ')
                if i == 'y' or i == 'Y':
                    selected_sub.append(x)
                    selected_sub.append(y)
                    selected_sub.append('\t')
                else:
                    pass

            if len(selected_sub) >= 5:
                break
            else:
                print('\n','Please select atleast five subjects','\n')
                selected_sub = []
        return selected_sub

    def Fourth_Sem(self):
        print('Select the Courses')
        sem_4_dict = {
            'CS210':	'Formal Languages and Automata',
            'CS231':	'Operating Systems',
            'CS232':	'Operating Systems Lab',
            'CS235':	'Artificial Intelligence',
            'CS240':	'Database Management Systems',
            'CS241':	'DBMS Lab',
            'SC202':	'Chemistry',
            'HS303':	'Indian Writing in English'
        }

        selected_sub = ['Sem--> 4th     COURSES :-->  ']
        while True:
            print('y/Y for YES','n/N for no')
            for x,y in sem_4_dict.items():
                print(x,y)
                i = input('y/n :-->    ')
                if i == 'y' or i == 'Y':
                    selected_sub.append(x)
                    selected_sub.append(y)
                    selected_sub.append('\t')
                else:
                    pass

            if len(selected_sub) >= 5:
                break
            else:
                print('\n','Please select atleast five subjects','\n')
                selected_sub = [] 
        return selected_sub

    def Fifth_Sem(self):
        print('Select the Courses')
        sem_5_dict = {
            'CS301':	'Theory of Computation',
            'CS352':	'Computer Networks',
            'CS353':	'Computer Networks Lab',
            'CS351':	'IT Workshop III: Cloud Computing',
            'CS306':	'Machine Learning',
            'CS316':	'Machine Learning Lab',
            'SC301':	'Biology',
            'HS302':	'Language, Cognition and Culture'
        }

        selected_sub = ['Sem--> 5th     COURSES :-->  ']
        while True:
            print('y/Y for YES','n/N for no')
            for x,y in sem_5_dict.items():
                print(x,y)
                i = input('y/n :-->    ')
                if i == 'y' or i == 'Y':
                    selected_sub.append(x)
                    selected_sub.append(y)
                    selected_sub.append('\t')
                else:
                    pass

            if len(selected_sub) >= 5:
                break
            else:
                print('\n','Please select atleast five subjects','\n')
                selected_sub = []
        return selected_sub

    def Sixth_Sem(self):
        print('Select the Courses')
        sem_6_dict = {
            'MA305':	'Optimization Techniques',
            'CS330':	'Software Engineering',
            'CS331':	'Software Engineering Lab',
            'CS320':	'Compilers',
            'CS321':	'Compilers Lab',
            'CS361':	'Computer Security',
            'SC302':	'Physics II',
            'CS300':    'Project I(Optional)',
            'HS203':	'Science Fiction I',

        }
        selected_sub = ['Sem--> 6th     COURSES :-->  ']
        while True:
            print('y/Y for YES','n/N for no')
            for x,y in sem_6_dict.items():
                print(x,y)
                i = input('y/n :-->    ')
                if i == 'y' or i == 'Y':
                    selected_sub.append(x)
                    selected_sub.append(y)
                    selected_sub.append('\t')
                else:
                    pass

            if len(selected_sub) >= 5:
                break
            else:
                print('\n','Please select atleast five subjects','\n')
                selected_sub = []
        return selected_sub

    def Seventh_Sem(self):
        print('Select the Courses')
        sem_7_dict = {
            'CS401':    'Data Analytics',
            'CS4XX':	'Open Elective',
            'CS4XX':	'Elective I',
            'CS400':	'Project II',
            'HS403':	'Science Fiction II'
        }
        selected_sub = ['Sem--> 7th     COURSES :-->  ']
        while True:
            print('y/Y for YES','n/N for no')
            for x,y in sem_7_dict.items():
                print(x,y)
                i = input('y/n :-->    ')
                if i == 'y' or i == 'Y':
                    selected_sub.append(x)
                    selected_sub.append(y)
                    selected_sub.append('\t')
                else:
                    pass

            if len(selected_sub) >= 3:
                break
            else:
                print('\n','Please select atleast three subjects','\n')
                selected_sub = []
        return selected_sub

    def Eighth_Sem(self):
        print('Select the Courses')
        sem_8_dict = {
            'CS4XX':	'Elective II',
            'CS4XX':	'Elective III',
            'CS4XX':	'Elective IV',
            'CS410':	'Project III',
            'HS304':	'Science, Technology and Society'
        }
        selected_sub = ['Sem--> 8th     COURSES :-->  ']

        # here while loop does that it print the courses and one by one user select the y or n then it returns the list of courses 
        while True:
            print('y/Y for YES','n/N for no')
            for x,y in sem_8_dict.items():
                print(x,y)
                i = input('y/n :-->    ')
                if i == 'y' or i == 'Y':
                    # here appending the course id and course name seperated by the tab
                    selected_sub.append(x)
                    selected_sub.append(y)
                    selected_sub.append('\t')
                else:
                    pass
            # if the course length is less then the 3 here then it will again tell the user to select the courses and minimum is 3 to be selected
            if len(selected_sub) >= 3:
                break
            else:
                print('\n','Please select atleast three subjects','\n')
                selected_sub = [] 
        # return the course list
        return selected_sub

    

    # when main is called  then first it will print the sem dictionary as in the while loop then select tthe semesterand after choosing the semester it will let to the 
    # semester function which is being selected
    def Main(self):
        print('Select the semester for which you are registering')
        sem = {
            '1':'sem-I',
            '2':'sem-II',
            '3':'sem-III',
            '4':'sem-IV',
            '5':'sem-V',
            '6':'sem-VI',
            '7':'sem-VII',
            '8':'sem-VIII'
        }
        
        while True:
            for x,y in sem.items():
                print(x,':--> ',y)

            i = int(input('choose from the above : -->   '))
            if i == 1:
                return self.FirstSem()
            elif i==2 :
                return self.Second_Sem()
            elif i==3:
                return self.Third_Sem()
            elif i==4:
                return self.Fourth_Sem()
            elif i==5:
                return self.Fifth_Sem()
            elif i==6:
                return self.Sixth_Sem()
            elif i==7:
                return self.Seventh_Sem()
            elif i==8:
                return self.Eighth_Sem()
            else:
                print('choose from the given option','\n')



# the code will staart from here
if __name__ == "__main__":
    # making object of the class Registration
    reg = Registration()

    # a while loop to take students
    while True:
        print('1 --> Start Registration')
        print('2 --> Exit')

# here try except is for the when user gives the wrong input like 's'  'a'   any string     correct input will be 1 or 2
        try:
            i=int(input('select 1 or 2 : --> '))
        except:
            print('choose correct option')
            continue
# if user puts 1 then registration will start  first takes name   roll number   branch
        if i == 1:
            # for each student it will take the input and store it as a list
            info_list = []
            
            name = input('Name :-->    ')
            roll_no = input('Roll Number:-->    ')
            branch = input('Branch:-->      ')

# giving the name roll branch in the list by extend
            info_list.extend([name,'\t',roll_no,'\t',branch,'\t'])

            # calling the Main function of the class Registration
            ret_list = reg.Main()
            # here ret_list contains the subjects that the user have given yes
            info_list.extend(ret_list)

# open the file and then add the next line as the student information
# if the file is not formed then the file will automatically form
            ffile = open('Student_Create_Information.txt','a')
            
            # before adding the list convert it in the string 
            ffile.writelines(' '.join(info_list)+'\n')
            
            # /close the file
            ffile.close()

            
            print('\n')

            # if the user select the 2 then exit the registration
        elif i==2:
            break
        else:
            print('choose the correct option','\n')
        

    # after exit the while loop then we are printing the data of the file
    ffile = open('Student_Create_Information.txt','r')
    print(ffile.read())


    
