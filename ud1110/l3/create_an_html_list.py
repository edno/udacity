#define the  html_list function
def html_list(input_list):
    html_string = ""
    for el in input_list:
        html_string += "<li>" + el + "</li>\n"
    return  "<ul>\n" + html_string + "</ul>"

print(html_list(['first string', 'second string']))
