
# coding: utf-8

# In[1]:


"""
This mmodule contains functions for converting
temperature between Fahrenheit and Celsius
"""

def to_celsius(fahrenheit):
    """
    Accepts Fahrenheit degrees as argument
    Returns Celsius degree
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def to_fahrenheit(celsius):
    """
    Accepts Celsius degrees (celsius argument)
    Returns Fahrenheit degrees
    """
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

# main function used to test other functions
# only run if module is the main
def main():
    for temp in range(0, 212, 40):
        print(temp, "Fahrenheit =", round(to_celsius(temp)), "Celsius")
        
    for temp in range(0, 100, 20):
        print(temp, "Celsius =", round(to_fahrenheit(temp)), "Fahrenheit")
        
# check if main module
if __name__ == "__main__":
    main()

