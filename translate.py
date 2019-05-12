def translate(bilingual_dict,english_words_list):
    
    for i in english_words_list:
        swedish_words_list=bilingual_dict[i]
        print(swedish_words_list)
    
bilingual_dict= {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
english_words_list=["merry","year","and"]
print("The bilingual dict is:",bilingual_dict)
print("The english words are:",english_words_list)

swedish_words_list=translate(bilingual_dict, english_words_list)
