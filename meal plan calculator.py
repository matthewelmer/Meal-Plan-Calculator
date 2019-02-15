# Version 1.1

import datetime


def get_meal_input():
    """Gathers and returns integer values for initial meals and current meals"""
    initial_meals = int(input('|Enter how many meals you purchased at the beginning of the semester: '))
    current_meals = int(input('|Enter how many meals you currently have remaining: '))
    return initial_meals, current_meals


def get_dollar_input():
    """Gathers input related to dining dollars"""
    initial_dollars = float(input('|Enter how many dining dollars you had at the start of the semester: '))
    current_dollars = float(input('|Enter how many dining dollars you currently have remaining: '))
    return initial_dollars, current_dollars


def find_slope(final=0, initial=0, final_time=0, initial_time=0):
    """Given an initial value, a final value, an initial time, and a final time, returns the average rate of change.
       Defaults to zero if no inputs are given or if a ZeroDivisionError occurs."""
    try:
        slope = (final - initial) / (final_time - initial_time)
    except ZeroDivisionError:
        slope = 0
    return slope


# welcome
print('|-------------------------------------------------------------------------------------------------')
print('|Welcome to the meal plan calculator!\n'
      '|This nifty little script will help you use ALL of your meals and dining dollars!\n|')

# get input
spring = bool(int(input('|Enter 0 for Fall semester, or 1 for Spring semester: ')))
mealsi, mealsf = get_meal_input()
dollarsi, dollarsf = get_dollar_input()

# initialize dates in datetime object format
if spring:  # for spring
    start_date = datetime.date(datetime.date.today().year, 1, 14)
    end_date = datetime.date(datetime.date.today().year, 5, 7)
else:  # for fall
    start_date = datetime.date(datetime.date.today().year, 8, 27)
    end_date = datetime.date(datetime.date.today().year, 12, 12)

# today's date
date_today = datetime.date.today()

# find how many days are in the semester
days_in_semester = (end_date - start_date).days

# find how many days since start of semester
day_difference = (date_today - start_date).days  # an integer of how many days since the beginning of the semester

# compute linear regression slope
meal_slope = find_slope(mealsf, mealsi, day_difference)
dollar_slope = find_slope(dollarsf, dollarsi, day_difference)

# use initial amount of meals/dollars as y-intercept and evaluate number of meals/dollars remaining at end of semester
meals_semester_end = mealsi + days_in_semester * meal_slope
dollars_semester_end = dollarsi + days_in_semester * dollar_slope

# compute how many meals one should use per week in order to use all meals
days_remaining = days_in_semester - day_difference
weeks_remaining = days_remaining / 7
try:
    meals_per_week = (mealsf / weeks_remaining)
    dollars_per_week = (dollarsf / weeks_remaining)
except ZeroDivisionError:
    meals_per_week = 0
    dollars_per_week = 0

# output to user
if date_today > end_date:
    print('|\n|It is past the last day of finals, which is beyond the scope of this calculator, sorry.')
else:
    # for meals
    print('|\n|Approximate meals remaining at the end of the semester: %.1f' % meals_semester_end)
    print('|Use about %.1f meals per week in order to reach 0 meals by the end of the semester.' % meals_per_week)
    # for dining dollars
    print('|Approximate dining dollars remaining at the end of the semester: %.2f' % dollars_semester_end)
    print('|Use about %.2f dining dollars per week in order to reach $0 by the end of the semester.' % dollars_per_week)
# final words
print('|\n|Remember, meals never carry over from semester to semester, and dining dollars only carry over\n'
      '|from fall to spring. Also note that this calculator does not account for breaks.')
print('|-------------------------------------------------------------------------------------------------')
input("Hit any key to exit.")
