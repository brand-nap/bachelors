"""
Name: Brandon Perez
Class: CSCI 1411-006
Due Date: 11/10/23
Description: Calculates descriptive information about data... numpy ripoff
Status: works as expected
"""

import math;

def main():
    intList = read_data();
    print();
    display_result(compute_sum(intList), compute_mean(intList), compute_sd(intList))

def read_data(intList = []):
    """
    Function Name: read_data
    Description: prompts user for a list of numbers
    Parameters: intList, type list, should only be passed recursively
    Returns: list of integers
    """
    
    nextInt = input('Number [Press Enter when Done]: ')
    
    if nextInt == '':
        return
    
    intList.append(int(nextInt))
    read_data(intList);
    
    return intList;

def compute_sum(intList):
    """
    Function Name: compute_sum
    Description: sum of integers in a list
    Parameters: intList, type list
    Returns: sum as integer
    """
    return sum(intList); 

def compute_mean(intList):
    """
    Function Name: compute_mean
    Description: computes the mean of a list of integers
    Parameters: intList, type list
    Returns: mean as float
    """
    return compute_sum(intList)/len(intList); # ugh. redundant. curse you, rubric!

def compute_sd(intList):
    """
    Function Name: compute_sd
    Description: computes the standard deviation of a list of integers
    Parameters: intList, type list
    Returns: standard deviation of int list as float
    """
    return math.sqrt(sum((num-compute_mean(intList))**2 for num in intList)/(len(intList)-1));

def display_result(E, mean, sd):
    """
    Function Name: display_result
    Description: prints sum, mean, and sd in a cute format
    Parameters: E for sum of int list, mean for mean of int list, sd for Standard Deviation of int list
    Returns: None
    """
    print(f"Sum: {'%.2f' % E}\nMean: {'%.2f' % mean}\nStandard Deviation: {'%.2f' % sd}");
