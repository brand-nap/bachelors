def main():
    str_list = getStringList(); #function that prompts for str list
    result_list = []; 
    average = 0;

    for string in str_list:
        result_list.append([string, len(string)]); #appends redundant key pairs of str and length
        print(result_list[len(result_list)-1]);
        average += len(string)/len(str_list);

    print(f'average string length is {average} characters');
    
    
#prompts a user for strings until they escape with the Enter key
def getStringList():
    
    result_list = [];
    user_str = input('Please enter a string (or press Enter when done): ');

    while user_str != '': #while user hasn't escaped with Enter key
        result_list.append(user_str); #append previous input to result
        user_str = input('Please enter a string (or press Enter when done): ');

    return result_list;
