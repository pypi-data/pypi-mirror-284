
import gradio as gr
from gradio_highlightcode import highlightcode
import time


example = highlightcode().example_value()

initial_value = """
#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}

"""

with gr.Blocks() as demo:
    code = highlightcode(initial_value, language="c", highlights=[(3, 6, "rgb(255 254 213)")])

if __name__ == "__main__":
    demo.launch()