def main():
    user_str=' ';
    final_str='';
    abc_dict = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0};
    result_dict = {};

    while user_str != '':
        final_str += user_str;
        user_str = input('Please enter a string: ');

    final_str = final_str.lower();
    
    for i in range(len(final_str)):
        key = final_str[i]; #readability++
        
        if key in abc_dict.keys(): #ignores all non-alphabetic chars in str
            abc_dict[key] = abc_dict[key]+1 #increment instances of char

    for pair in abc_dict.items():
        
        if pair[1] > 0: #ignores all chars that aren't featured
            result_dict[pair[0]] = pair[1]; #create pair for featured char
            
    print(result_dict);
