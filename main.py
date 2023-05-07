import sys


def activate(num_of_pages):
    indent = '            '
    html1 = open("html1", 'r')
    moti = open(str(num_of_pages) + ".html", 'w')
    moti.write(html1.read())
    moti.write('\n' + indent + '<li data-address="page1" data-page="1"></li>\n')

    for i in range(2, int(num_of_pages) - 1, 2):
        moti.write(indent + """<li data-address="page""" + str(i) + "_" + str(i + 1) + '" ' +
                   """data-page=""" + '"' + str(i) + '"' + """></li>\n""")

        moti.write(indent + """<li data-address="page""" + str(i) + "_" + str(i + 1) + '" ' +
                   """data-page=""" + '"' + str(i + 1) + '"' + """></li>\n""")

    moti.write(indent + """<li data-address="end""" + '" ' +
               """data-page=""" + '"' + str(num_of_pages) + '"' + """></li>\n""")

    html2 = open("html2", 'r')
    html3 = open("html3", 'r')
    my_html3 = html3.read()
    moti.write(html2.read())

    for i in range(1, int(num_of_pages) + 1):
        moti.write('\n' + indent + "<!-- BEGIN PAGE " + str(i) + "-->\n")
        if i < 10:
            moti.write('\n' + indent + '<div style="background-image:url(pages/web_Page_0'
                       + str(i) + '.jpg)" class="">\n')
        else:
            moti.write('\n' + indent + '<div style="background-image:url(pages/web_Page_'
                       + str(i) + '.jpg)" class="">\n')
        moti.write(my_html3)
        moti.write(indent + "<!-- END PAGE " + str(i) + "-->\n")

    html4 = open("html4", 'r')
    moti.write(html4.read())

    for i in range(1, int(num_of_pages) + 1):

        if i < 10:
            moti.write(indent + indent + '<li class="' + str(i) + '"><img alt="" src="pages/thumbs/web_Page_0'
                       + str(i) + '.jpg"></li>\n')
        else:
            moti.write(indent + indent + '<li class="' + str(i) + '"><img alt="" src="pages/thumbs/web_Page_'
                       + str(i) + '.jpg"></li>\n')

    html5 = open("html5", 'r')
    moti.write(html5.read())
    moti.close()


if __name__ == "__main__":
    num_of_pages = int(input("Enter number of pages: "))
    try:
        num_of_pages % 2 == 0 and num_of_pages >= 0
    except:
        print("Error: number of pages must be a positive, even number")
    else:
        activate(num_of_pages)