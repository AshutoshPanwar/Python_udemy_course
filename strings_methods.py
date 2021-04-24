#strings are immutable

my_str = "This is Python"
 
# .count("") will count how many time that letter occure in that string

    print(my_str.count('s'))        # 2 times the s occured in my_str

#.index("") method will give the index of first occurence

    print(my_str.index('s'))        #at 3 place the first s is there

#.find("")metho will find the index of first occurence 

    print(my_str.find('s'))         # 3 the first s found

#.strip() will remove the element entered from starting and end
my_str = " This is Python "
    print(my_str.strip())           #will remove the space from starting and ending
    print(my_str.strip(' Tn'))      #will remove the Tn from my_str

#.split() will split the strings into parts on the basis of entered element
    print(my_str.split())

#.replace("old_value","new_value")
    print(my_str.replace('h','x'))  # h is replaced by x

#.upper & lower method will conver the text in small and capital alphabets
    print(my_str.upper())           #output: THIS IS PYTHON
    print(my_str.lower())           #output: this is python