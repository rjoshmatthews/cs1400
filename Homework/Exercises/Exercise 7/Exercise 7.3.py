"""
Robert Matthews
CS 1400
Section 002
Exercise 7

7.3
Chapter 7, Programming Exercise #8, pg. 239. Submit your source code as your answer.
"""

# a person is eligible fo be a US senator if they are at least 30 years old and have been a US citizen for at least 9
# years. to be a US representative these numbers are 25 and 7, respectively. Write a program that accepts a person's age
# and years of citizenship as input and outputs their eligibility for the Senate and the House.

age = eval(input("Please enter your age: "))
citizenship = eval(input("Please enter how long you have been a US citizen: "))

if age >= 30 and citizenship >= 9:
    print("You fit both requirements for the Senate and House of Representatives.")

elif age >= 30 and 7 <= citizenship < 9:
    print("You fit the requirements of age for Senate and House. You have enough citizenship to run for the House but "
          "not enough for the Senate.")

elif age >= 30 and citizenship < 7:
    print("You pass the age requirement but do not qualify for either the Senate or House with length of citizenship.")

elif 25 <= age < 30 and citizenship >= 9:
    print("Citizenship eligibility passes both, and you are old enough for the House, but not old enough for the "
          "Senate.")

elif 25 <= age < 30 and 7 <= citizenship < 9:
    print("You only qualified to run for the House of Representatives.")

elif 25 <= age < 30 and citizenship < 7:
    print("You are old enough to qualify for the House, but lack citizenship for both the House and Senate.")

elif age < 25 and citizenship >= 9:
    print("You're citizenship is enough to qualify, but lack age for both the House and Senate.")

elif age < 25 and 7 <= citizenship < 9:
    print("Your citizenship qualifies you for the House, but you are not old enough.")

else:
    print("You do not fit any requirements to be eligible for the US Senate or "
          "House of Representatives")

# I could have followed a layered pattern that would have allowed to sort for age and then citizenship before creating
# a print statement. I enjoyed laying out the logic ladder for this though!
