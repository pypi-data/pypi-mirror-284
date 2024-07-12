import gradio as gr
from gradio_storybook_params_table import storybook_params_table

project_params = []
machine_params = []

with gr.Blocks(css=".column-form .wrap {flex-direction: column;}") as demo:
    with gr.Row():
        storybook_params_table(params=machine_params)

if __name__ == '__main__':
    demo.launch()