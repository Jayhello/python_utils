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
    with open(filename) as jf:
        jsondata = json.load(jf)

    return byteify(jsondata)


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
    print get_json_from_file('../config/search_keywords.json')