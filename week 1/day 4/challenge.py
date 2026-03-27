#how the logic works (results)
******************
* Hello          *
* World          *
* in             *
* reallylongword *
* a              *
* frame          *
******************

#a minor pro tip
length = max(len(str(word)) for word in words)
# ... then in the loop ...
print(f"* {str(word).ljust(length)} *")