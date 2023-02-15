# Author: Aubrey Floyd
# GitHub username: aubreyfloyd2
# Date: 2/15/2023
# Description: Class called person with two data members and a function to return population
#              standard deviation from list of ages.

class Person():
    """Represents two private data members including name and age."""

    def __init__(self, name, age):
        """Creates person with name and age"""
        self._name = name
        self._age = age

    def get_age(self):
        """Returns age"""
        return self._age

def std_dev(person_list):
    """Returns population standard deviation in ages from a list of ages"""
    total = 0
    for person in person_list:
        total += person.get_age()
    mean_age = total / len(person_list)
    square_sum = 0
    for person in person_list:
        square_sum += (mean_age - person.get_age()) ** 2 # variance
    return (square_sum / len(person_list)) ** 0.5 # sqaure root


# p1 = Person("Kyoungmin", 73)
# p2 = Person("Mercedes", 24)
# p3 = Person("Beatrice", 48)
# person_list = [p1, p2, p3]
# answer = std_dev(person_list)
# print(answer)
