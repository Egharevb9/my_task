# collecting users name 
name =  input("enter your name: ")


# age requiredment
age = int(input("enter your age: "))

utme_score = int(input("Enter you UTME score: "))
choice = input("is UNILAG your first choice?: (yes /no): ").title

# O"level requirement
olevel_requiredment = input("how many credit did you have in one sitting? ")
english_pass = input = input("Did you pass english language? (yes/no): ").title()
# post_ utme screening
post_utme_score = int(input("enter you post uutme score (0 - 100)"))

# department cut_ off
dept_cutoff = int(input("Enter your Departmental cut-off mark (200 - 320): "))
# conditionas for considering the user admission
# must be at least 16
meets_age = age >= 16
# must be >= 200 and unilag as first choice
meets_utme = (utme_score >= 200) and (first_choice =="Yes")
# must be 5 credits including english $ math
meets_olevel = (olevel_requiredment >= 5) and (english_pass =="Yes") and (math_pass == "yes")
# total score for admission = utme + post-utme
total_score = utme_score + post_utme_score
meets_cutoff = total_score >= dept_cutoff
# final decision
eligibility = age and meets_utme and meets_olevel and meets_cutoff
# mapping true and false to statement for final result

result = {
    True:f"congratulations{name} you have been ofered admission tovthe course of your choice",
    False: f"sorry, no admission yet"
}
print("\n === admission status ===")
print(f"staus:{result[eligibility]}")