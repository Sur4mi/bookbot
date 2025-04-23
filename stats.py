def word_count(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = len(words)
    return num_words

def num_char(path_to_file):
    with open(path_to_file, 'r') as f:
        file_contents = f.read().lower()
        char_dic = {}
      
        for i in file_contents:
            if i.isalpha():
                if i in char_dic:
                    char_dic[i] +=1
                else:
                    char_dic[i] = 1
        return char_dic
        
def sorted_list(char_dic):
    list_dict = [{key: value} for key, value in char_dic.items()]
    def sort_on(d):
        return list(d.values())[0]
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict