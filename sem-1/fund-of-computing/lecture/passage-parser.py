import re;

def main():
    passage = input('\nEnter passage here: ');
    organizedPassage = organize(passage);
    
    resultDict = {};
    for word in organizedPassage:
        resultDict[word] = resultDict[word]+1 if word in resultDict.keys() else 1;
     
    print(f'\n{resultDict}');

def organize(user_str):
    
    organizedPassage = [re.sub('[^a-z]', '', word) for word in user_str.lower().split(' ')];
    #take in passage as input, lower the characters, split them by spaces, store each word into list stripped of all characters besides a-z
    
    organizedPassage.sort(reverse=True); #put in reverse alphabetical order
    return organizedPassage
    
