#alogrithims & functions class
import matplotlib
matplotlib.use("Agg") #using matplotlib agg for effincency a& we want to render as an image on our own in a more friendly format for gradio

from random import randint
import matplotlib.pyplot as plt
import io
from PIL import Image

fig, g = plt.subplots(figsize=(5, 3)) #making one public subplot so we dont have to re-render background every time
#^fitting size to not waste resources on rendering large images & consistent size


def bubbleSort( myarr: list[int]):
    n = len(myarr)

    for i in range(0, n):
        swapped = False
        
        for j in range(0, n-i-1): #largest element will allways be sorted ad the end of each pass reduce no. of passes for time's sake
            yield plotBubble(myarr, j, False) #generating function to send images as they're rendered to reduce wait times & not clog up memory storing in arrays
            if(myarr[j] > myarr[j+1]):
                myarr[j], myarr[j+1] = myarr[j+1], myarr[j]
                swapped = True
                yield plotBubble(myarr, j, True) #generating function to send images as they're rendered to reduce wait times & not clog up memory storing in arrays

        if(swapped == False): #early exit  to reduce time complexity
            break 


def plotBubble(myarr: list[int], focus: int, swapped: bool):
    x=[i for i in range(1, len(myarr)+1)]
    highlight = [focus, focus + 1]
    
    g.clear()

    color=[]
    title=""
    for i in range(len(myarr)):
        if i == focus or i == focus + 1: 
            if swapped:
                title = (f"index {focus} is greater than {focus+1} and are thus swapped") #desiscion for explination of step
                color.append("lightcoral") #unique shade on pointers durrin swap for clarity
            else:
                title = (f"check if value at index {focus} > {focus+1}")
                color.append("red")
        else:
            color.append("blue") #contrasts red well for unimportant pointers

    g.bar(x, myarr, width= 0.9, color=color,) 
    g.set_title(title)
    g.set_xticks([]) #improve visibility/clairty, numbers can get crowded on large datasets, plus size does a better job at conveying value
    g.set_yticks([])
    
    buffer = io.BytesIO()
    fig.savefig(buffer, format="png") #save matplot lib to memory as a byte image on a buffer scince we have to render the image to be more friendly with gradio, file is only temporarly stored as 1 frame
    buffer.seek(0)
    img = Image.open(buffer) #gradio image, only accepts numpy image, a file from disk, or a PIL.Image.Image 
    return img


def generateArray(n: int) -> list[int]:
    myarr = []
    for n in range(0, n):
        myarr.append(randint(1,100))
    return myarr

def generateBest(n:int, bestCase:bool) -> list[int]:
    myarr = []
    for i in range(1, n): #option select for 'best/worst case'
        if bestCase:
            myarr.append(i)
        else:
            myarr.append(n-i)
    return myarr


