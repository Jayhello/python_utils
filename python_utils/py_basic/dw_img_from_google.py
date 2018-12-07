from google_images_download import google_images_download

chrome_driver_path = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"
out_put_path = "E:/face_rec/yy_face_demand/cartoon_sample/"
out_put_path = "E:/face_rec/short_vedio_famous_people/people_lst/"
out_put_path = "E:/people_detection/test_datasets/"


def dw(s_keyword):
    """
    :param s_keyword: like "pet cat images, pet dog images"
    :return: None
    """
    # class instantiation
    response = google_images_download.googleimagesdownload()

    # creating list of arguments
    arguments = {"keywords": s_keyword,
                 "limit": 200, "print_urls": True,
                 "output_directory": out_put_path,
                 "chromedriver": chrome_driver_path}

    # passing the arguments to the function
    paths = response.download(arguments)

    # printing absolute paths of the downloaded images
    print(paths)


def do_dw():
    lst_keywords = ["pedestrian images"
                    ]
    dw(lst_keywords[0])
    pass


def dw_famous():
    f_path = 'E:/face_rec/short_vedio_famous_people/famous_list.txt'
    lst_famous = open(f_path).read().split('\n')

    # print len(lst_famous)
    # print ",".join(lst_famous[-3:])

    s_key_word = ",".join(lst_famous)
    dw(s_key_word)


if __name__ == '__main__':
    dw_famous()
    # do_dw()
    pass
