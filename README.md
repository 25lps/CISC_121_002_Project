# Algorithm Name

Bubble sort

I chose to use bubble sort for this assingment because it the only sorting algorithm (that im aware of) which requires to see the actual sorting to understand why it is named "bubble sort".  I found this out online while studying and figured it'd be cool to make an actual live demo for myself.  Essentially the name bubble sort comes from the idea that the bigger values float to the top faster, like bigger bubbles.  Alternitavley called sinking sort as the heavier/bigger values sink into palce faster. which I had never considedered before and previously was a little confused on the name.  I found this cool enough to warrant me making project on bubble sort.


## Demo video/gif/screenshot of test

As you can in the video there are no bugs or much room for unique input to mess up and where you can you are not able to input anyting but a number within the provided range. Except for decimals, as the slider is natually a float. So I naturally added a check to see if it is a whole number.
![image alt](https://github.com/25lps/CISC_121_002_Project/blob/012ef540fd276ae98a153108385e5448663007b8/Test.mp4)

Another test I did but patched durring the devlopment was initally the radio buttons used to be 3 unique buttons, however they you could still start a new sort under a different time complexity if you pressed a different button. I could not find anything on gradio's docs to manage it.  So I used another feature radio buttons, wich solved my problem wholy, but I also think look a little better. 

![image alt](https://github.com/25lps/CISC_121_002_Project/blob/012ef540fd276ae98a153108385e5448663007b8/demo1-1.png)
![image alt](https://github.com/25lps/CISC_121_002_Project/blob/012ef540fd276ae98a153108385e5448663007b8/demo1-2.png)

![image alt](https://github.com/25lps/CISC_121_002_Project/blob/012ef540fd276ae98a153108385e5448663007b8/demo2-1.png)
![image alt](https://github.com/25lps/CISC_121_002_Project/blob/012ef540fd276ae98a153108385e5448663007b8/demo2-2.png)

![image alt](https://github.com/25lps/CISC_121_002_Project/blob/012ef540fd276ae98a153108385e5448663007b8/demo3-1.png)
![image alt](https://github.com/25lps/CISC_121_002_Project/blob/012ef540fd276ae98a153108385e5448663007b8/demo3-2.png)

## Problem Breakdown & Computational Thinking (You can add a flowchart and write the

four pillars of computational thinking briefly in bullets)

1. Decoposisition:
- parse through array
- read & compare values of array
- preform swaps (inplace preffriably)

2. Patern recognition
- It repeatedly reaches values by looping through a for loop to access more values
- It also compares values in a nested for loop going through and comparing if the left index is bigger than the right index
- It swaps values repeatedly using pythons built in method (arr[i], arr[j] = arr[j], arr[i])
- Another pattern of note is that the total loops we must do shrinks on each pass as the next largest value will naturally "bubble up" and be correctly sorted

3. Abstraction:
- The user should be in control of the array size, time complexity, and overall speed of the program, as this directly impacts how much they are able to learn/pick up
- The user should not be in control and the max/min values, as they are not relevant to understanding the algorithim beyond surface level which may be picked up with hte provided range
-I think the user should interact with this through sliders and input boxes to lower the risk of failure and keep it as simple as possible, (at max like 2 buttons, the program has 1 function, 1 button preferably)

4. Algorithm design:
- stick to using integers for all numbers for array values, not worth confusing people with complex fractions
- allow fractions for speed, due to required fine tuining
- use arrays to store integer as we are not preforming complex computations and they are relativley efficent (compared to other data types) & muteable
- I used matplot lib graphs simply beacuse they're easy to work with since it it not nessisarly the focus of the assignment compared to bubble sort + this is a time sensitive assingment
- array size 1 < n < 100, int

![image alt](https://github.com/25lps/CISC_121_002_Project/blob/012ef540fd276ae98a153108385e5448663007b8/flowchart.png)


## Steps to Run

1. isntall external libraries outlined in requirements.txt with either pip or compatable python package manager
2. run "python .\app.py" frpm project root
3. or visit hugging face link (see section bellow)
4. configure array size/sorting speed outlined on webapp & choose time complexity
5. click the big "sort!" button on right-side pannel


## Hugging Face Link
https://huggingface.co/spaces/25lps/CISC_121_002_Project

## Author & Acknowledgment
Aaron Campbell
20551958
25lps@queensu.ca

[NO AI WAS USED FOR THIS PROJECT]

resources:
https://stackoverflow.com/questions/65639284/how-do-i-convert-an-bytes-image-from-bytesio-to-a-pil-image-in-python
https://www.gradio.app/docs
https://www.gradio.app/docs/gradio/image
https://hugovk-pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.frombytes
https://docs.python.org/3/library/time.html#time.time
https://www.geeksforgeeks.org/dsa/bubble-sort-algorithm/
https://www.geeksforgeeks.org/python/how-to-save-a-plot-to-a-file-using-matplotlib/
https://stackoverflow.com/questions/8598673/how-to-save-a-pylab-figure-into-in-memory-file-which-can-be-read-into-pil-image
https://stackoverflow.com/questions/32908639/open-pil-image-from-byte-file
https://matplotlib.org/stable/

https://www.geeksforgeeks.org/python/how-to-save-a-plot-to-a-file-using-matplotlib/

