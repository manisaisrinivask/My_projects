
# coding: utf-8

# In[49]:


def get_dimensions():
    request = input("Please choose the dimensions of the game board. ")
    while True:
        try:
            request = request.strip().split("*")
            if len(request) != 2:
                int("error")
            dimensions = (int(request[0]), int(request[1]))
            if dimensions[0] >= 0 and dimensions[1] >= 0:
                return dimensions
            else:
                int("error")
        except:
            request = input("Please choose two natural numbers seperated by an '*'. For example '3*3'. ")

def draw (rows, columns):
    top = columns *     " ----"
    strich = columns *  "|    " + "|"
    for i in range(0, rows):
        print(top)
        print(strich)
    print(top)

dim = get_dimensions()
x = dim[0]
y = dim[1]
draw(x, y)

