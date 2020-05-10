def retrieveMostFrequentlyUsedWords(helpText, wordsToExclude):
    
    list_help_text = helpText.lower().split()
    most_common = []
    
    for word in wordsToExclude:
        list_help_text.remove(word)
    
    for word in list_help_text:
        if list_help_text.count(word) > 1 and word not in most_common:
            most_common.append(word)
    
    print(list_help_text)
    print(most_common)
pass

helpText = "Rose is a flower red rose are flower"
wordsToExclude = ['is', 'are', 'a']

retrieveMostFrequentlyUsedWords(helpText, wordsToExclude)