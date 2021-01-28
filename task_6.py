subj = {}
with open('text_5.txt', encoding='utf-8') as f:
    line = f.read()
    print(line)

        #subject, lecture, practice, lab = line.split('()')
        #subj[subject] = int(lecture) + int(practice) + int(lab)
    #print(f'Общее количество часов по предмету - \n {subj}')
#new_list = [sum(x) for x in list_1 if x == int]
#print(new_list)
#dict_1 = dict(zip(list_1[::2], list_1[1::2]))
#print(dict_1)