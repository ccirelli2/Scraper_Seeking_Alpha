
text = "Today's weather forcast is cloudy"


def insert_backslash_into_text(dirty_text):

    clean_text = dirty_text.replace("'", "\\'")
           
    return clean_text


test = insert_backslash_into_text(text)

print(test)

