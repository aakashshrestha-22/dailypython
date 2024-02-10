str_x = "Emma is good developer. Emma is a writer"

for i in str_x.split():
    if(i =="Emma"):
        print(i)
# use count method of a str class
cnt = str_x.count("Emma")
print("Emma appeared",cnt,"times")