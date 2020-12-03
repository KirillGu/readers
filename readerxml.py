import xml.etree.ElementTree as ET

def op_files(name):
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(name, parser)
    root = tree.getroot()

    text_f = ''
    news_xml = root.findall('channel/item')
    for news in news_xml:
        title = news.find("title")
        descr = news.find('description')
        descr_text = descr.text
        text_f += descr_text
    return text_f



def the_word(text_f): #word >6
    to_list = text_f.split()
    words_value = {}
    for word in to_list:
        if len(word) > 6:
            if word in words_value:
                words_value[word] += 1
            else:
                words_value[word] = 1
    return words_value



def sort_top(words_value): #sort and top
    l = lambda words_value: words_value[1]
    sort = sorted(words_value.items(), key = l, reverse = True)
    #print(sort)
    count = 1
    top = {}
    for word in sort:
        top[count] = word
        count += 1
        if count == 10:
            break
    return top



print('Top 10 popular Words:')
top = sort_top(the_word(op_files('newsafr.xml')))
for finish in top.values():
    print (f'{finish[0]} - {finish[1]}')
