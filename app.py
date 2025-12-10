#gradio app wrapper

import gradio as gr
import bubble 
from time import sleep
from time import time



def averageCase(n, MIN_FRAME, case):

    try:
        n = float(n)
    except:
        gr.Info("Array size must be a number.")
        return None, None
    
    if not n.is_integer(): #will throw an error if a decimal is put into array size, handling edge case
        return None, None
    
    n = int(n)

    if case == "Random": #cant save radioButton's as booleans and stil be readable to users
        sortingArr = bubble.generateArray(n)
    elif case == "Best-Case":
        sortingArr = bubble.generateBest(n, True)
    else:
        sortingArr = bubble.generateBest(n, False)
        
    lastTime = time()
    for frame in bubble.bubbleSort(sortingArr):
        lastTime = time()
        yield sortingArr, frame #generating function so we can return 1 frame at a time
        nowTime = time()
        dt = nowTime - lastTime #delta time to prevent from skipping frames too fast
        if dt < MIN_FRAME:
            sleep(MIN_FRAME - dt)


with gr.Blocks() as sort:
    with gr.Row():
        
        with gr.Column():
            MIN_FRAME = gr.Slider(0.8, 5, label="animation speed", step=.05) # sliders prevent users from using non-numbers (with specified step), and keep it in a specific range
            array_elements = gr.Slider(5, 100, label="array size", step=1)
            userGuide = gr.Textbox(label="⚠️How To Use:⚠️", value="🟠Drag the sliders, or input into the input boxes to change the minimum amount of time between frames or the array size respectivley" \
            "\n\n🟠Select your case for the program's time complexity on the Right side pannel bellow \"sort!\" button" \
            "\n\n🟠Press the button that read's \"sort!\" on the right side pannel to begin simmulation after configuring settings")
            sortingInfo = gr.Textbox(label="🤓About Bubble Sort:🤓", value="🔴Bubble sort is a sorting alogrithim that compares an element to the one on it left; if the element to left is smaller then a swap is preformed " \
            "and we move to the next element. This is continued until all elements in the array are sorted" \
            "\n\n🔴Bubble sort got its name from larger how larger values \"bubble up\" to the top faster than all the other elements as if they were more buoyant. And this is best seen when graphically displayed" \
            "\n\n🔴Best case time-complexity O(n), Average time-complexity O(n^2), Worst case time-complexity O(n^2) ascending order, random order, and reverse order respectivley")

        with gr.Column():
            array = gr.Textbox(label="Current Array", lines=2)
            graph = gr.Image()

            sortButton = gr.Button(value="sort!")
            caseRadio = gr.Radio( #radio buttons are nice
                choices=["Random", "Best-Case", "Worst-Case"],
                value="Random",
                label="Case")
            
            sortButton.click(fn=averageCase, inputs=[array_elements, MIN_FRAME, caseRadio], outputs=[array, graph]) #one button simple!


if __name__ == "__main__":
    sort.launch()

