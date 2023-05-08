import csv
from datetime import datetime

def profile_matcher(first_name, last_name):
    with open('Data.csv', mode='r', encoding='utf-8-sig') as profiles_file:
        fieldnames = ['Community', 'Community Preference', 'Gender', 'First Name', 'Last Name', 'Religion', 'Height', 'Date of Birth']
        profiles_reader = list(csv.DictReader(profiles_file, fieldnames=fieldnames))
        male_profiles = []
        
        female = csv
        
        # Change the format of height of the chosen Female Candidate to ft in format, cause some are given in format like 5'9", 5.9 etc.
        female_feet = 0
        female_inches = 0
        female_feet_flag = 0
        female_dob = None
        for i in profiles_reader:
            if i['First Name'] == first_name and i['Last Name'] == last_name:
                # set the female candidate reader
                female = i
                # set female candidate DOB which will be used further
                female_dob = datetime.strptime(i['Date of Birth'], '%m/%d/%y')
                
                for j in i['Height']:
                    if j.isnumeric() == False:
                        female_feet_flag = 1
                        continue
                    if female_feet_flag == 0:
                       if j.isnumeric():
                           female_feet *= 10 
                           female_feet += int(j)
                    else:
                        if j.isnumeric():
                            female_inches *= 10
                            female_inches += int(j)
                break
            
        # set female height using the feet and inches calculated in the above for loop
        female_height = "{0}ft {1}in".format(female_feet, female_inches)
        
        for current_profile in profiles_reader:
            
            # check if the current profile is male and not the input candidate 
            if current_profile['Gender'] == 'Male' and current_profile['First Name'] != first_name and current_profile['Last Name'] != last_name:
                male_dob = datetime.strptime(current_profile['Date of Birth'], '%m/%d/%y')
                
                # standardizing the height format in feet and inches as done for the female candidate above
                male_feet = 0
                male_inches = 0
                male_feet_flag = 0
                for i in current_profile['Height']:
                    if i.isnumeric() == False:
                        male_feet_flag = 1
                        continue
                    if male_feet_flag == 0:
                       if i.isnumeric():
                           male_feet *= 10 
                           male_feet += int(i)
                    else:
                        if i.isnumeric():
                            male_inches *= 10
                            male_inches += int(i)
                
                # setting male height
                male_height = "{0}ft {1}in".format(male_feet, male_inches)
                
                if (male_dob < female_dob) and male_height > female_height and (current_profile['Community Preference'] == female['Community Preference'] or current_profile['Community Preference'] == 'Open' or current_profile['Community Preference'] == 'N/A') and current_profile['Religion'] == female['Religion']:
                    male_profiles.append(current_profile)
        
        # writing output to Matches.csv file
        fieldnames = ['Community', 'Community Preference', 'Gender', 'First Name', 'Last Name', 'Religion', 'Height', 'Date of Birth']
        with open('Matches.csv', mode='w', newline='', encoding='utf-8-sig') as result_file:
            writer = csv.DictWriter(result_file, fieldnames=fieldnames)
            writer.writeheader()
            for profile in male_profiles:
                writer.writerow(profile)


profile_matcher('F53', 'L53')
