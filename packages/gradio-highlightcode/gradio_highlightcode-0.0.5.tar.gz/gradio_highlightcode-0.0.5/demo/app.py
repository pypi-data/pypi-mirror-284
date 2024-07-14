
import gradio as gr
from gradio_highlightcode import highlightcode
import time


example = highlightcode().example_value()

initial_value = """import random
#include <iostream>

def scramble_name(name):
    name_list = list(name)
"""

completion = """    random.shuffle(name_list)
    return ''.join(name_list)

# Example usage:
print(scramble_name("Python"))
"""

def generate_code():
    for i in range(len(completion)):
        time.sleep(0.03)
        yield highlightcode(initial_value + completion[:i], highlights=[(5, "rgb(255 254 213)")])

with gr.Blocks() as demo:
    code = highlightcode(initial_value, language="c")
    btn = gr.Button("Generate", variant="primary")
    btn.click(generate_code, outputs=code)

if __name__ == "__main__":
    demo.launch()