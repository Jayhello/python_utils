# _*_ coding:utf-8 _*_
import json
import codecs


def byteify(input):
    """
    the string of json typed unicode to str in python
    This function coming from stack overflow
    :param input: {u'first_name': u'Guido', u'last_name': u'jack'}
    :return:      {'first_name': 'Guido', 'last_name': 'jack'}
    """
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input


def get_json_from_file(filename):
    """注意如果自己创建的json.txt文件读取有问题，可以在pycharm中创建file.json然后再读取"""
    with open(filename) as jf:
        jsondata = json.load(jf)

    return byteify(jsondata)


def put_unicode_to_str():
    data = {"ocrMsg": u"\u556a\u556a\u76f4\u64ad\u514d\u8d39\u8bd5"}
    js = json.dumps(data, indent=4, ensure_ascii=False)
    print js


def generate_keyword_jsonfile(lst):
    """
    generate keyword_jsonfile 'search_keywords.json' to
    the directory config
    :return:
    """

    js_data = {"0": [], "1": [], "2": []}
    for item in lst:
        id, value = str(item[0]), item[1]
        js_data[id].append(value)

    with codecs.open('../config/search_keywords.json', 'w', encoding='utf-8') as fp:
        # json.dump(js_data, fp)
        fp.write(json.dumps(js_data, indent=4, sort_keys=True, ensure_ascii=False))

if __name__ == '__main__':
    # generate_keyword_jsonfile()
    # print get_json_from_file('../config/search_keywords.json')
    js = {"aaData":[ {"id":21,"keyword":"\u8D85\u7BA1","keywordType":0}, {"id":43,"keyword":"\u516C\u5B89","keywordType":0}, {"id":44,"keyword":"\u519B\u88C5","keywordType":1}, {"id":45,"keyword":"\u66B4\u529B","keywordType":1}, {"id":46,"keyword":"\u519B\u670D","keywordType":2}, {"id":47,"keyword":"\u9732\u4E73","keywordType":2},], "data":[{"$ref":"$.aaData[0]"},{"$ref":"$.aaData[1]"}, {"$ref":"$.aaData[2]"},{"$ref":"$.aaData[3]"}, {"$ref":"$.aaData[2]"},{"$ref":"$.aaData[3]"}], "error":False,"iTotalDisplayRecords":6,"iTotalRecords":6,"recordsFiltered":6,"recordsTotal":6,"sEcho":"1","success":True}
    js = {"aaData":[{"id":195261,"keywordCore":"直播","keywordDepartment":"YY","keywordWarn":"裸聊","newsDate":"2017-02-28 20:14:01","newsTitle":"美女直播","updateKeywordDate":"2017-02-28 20:14:01","url":"http://www.junjiewang.com\/44756.html","webSrc":"junjie"}, {"id":195258,"keywordCore":"直播","keywordDepartment":"YY","keywordWarn":"裸聊","newsDate":"2017-02-28 20:13:58","newsTitle":"美女直播","updateKeywordDate":"2017-02-28 20:13:58","url":"http:www.junjiewang.com/45345.html","webSrc":"junjie"},], "contentList":[{"contentNum":67,"dateDay":"2017-01-08"},{"contentNum":20,"dateDay":"2017-01-09"}], "data":[{"$ref":"$.aaData[0]"},{"$ref":"$.aaData[1]"}], "error":False,"iTotalDisplayRecords":2,"iTotalRecords":2,"recordsFiltered":2,"recordsTotal":2,"sEcho":"3","success":True, "warnList":[{"contentNum":28,"dateDay":"2017-01-08"},{"contentNum":8,"dateDay":"2017-01-09"}]}
    js = {"aaData":[{"id":195261,"keywordCore":"\u76F4\u64AD","keywordDepartment":"YY","keywordWarn":"\u88F8\u804A","newsDate":"2017-02-28 20:14:01","newsTitle":"\u76F4\u64AD\u65B0\u89C4\u4ECA\u8D77\u5B9E\u65BD\uFF0C\u4F60\u5E94\u8BE5\u77E5\u9053\u7684\u516D\u4E2A\u95EE\u9898","updateKeywordDate":"2017-02-28 20:14:01","url":"http:\/\/www.junjiewang.com\/hulianwang\/44756.html","webSrc":"junjie"}],"data":[{"$ref":"$.aaData[0]"}],"error":False,"iTotalDisplayRecords":1,"iTotalRecords":1,"recordsFiltered":1,"recordsTotal":1,"sEcho":"11","success":True}
    # print json.dumps(js, indent=4)
    put_unicode_to_str()

