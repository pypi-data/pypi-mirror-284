---
tags: [gradio-custom-component, SimpleTextbox]
title: gradio_storybook_params_table
short_description: 
colorFrom: blue
colorTo: yellow
sdk: gradio
pinned: false
app_file: space.py
---

# `gradio_storybook_params_table`
<a href="https://pypi.org/project/gradio_storybook_params_table/" target="_blank"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/gradio_storybook_params_table"></a>  

Python library for easily interacting with trained machine learning models

## Installation

```bash
pip install gradio_storybook_params_table
```

## Usage

```python
import gradio as gr
from gradio_storybook_params_table import storybook_params_table

project_params = []
machine_params = []

with gr.Blocks(css=".column-form .wrap {flex-direction: column;}") as demo:
    with gr.Row():
        storybook_params_table(params=machine_params)

if __name__ == '__main__':
    demo.launch()

# import json
# import gradio as gr
# from gradio_uni_view import uni_view
# from gradio_materialviewer import MaterialViewer as material_viewer
# from gradio_dp_project import dp_project
# from bohrium_open_sdk.view.gradio import dp_machine
# from gradio_storybook_params_table import storybook_params_table

# structure = {}
# structure['format'] = 'sdf'
# structure['content'] = """1a
#      RDKit          3D

#  27 29  0  0  1  0  0  0  0  0999 V2000
#   -15.3524  -19.2206  -25.9684 C   0  0  0  0  0  0  0  0  0  0  0  0
#   -14.6526  -19.7081  -27.0823 C   0  0  0  0  0  0  0  0  0  0  0  0
#   -15.8555  -20.1235  -25.0241 C   0  0  0  0  0  0  0  0  0  0  0  0
#   -14.4541  -21.0636  -27.2485 C   0  0  0  0  0  0  0  0  0  0  0  0
#   -15.6357  -21.4854  -25.1840 C   0  0  0  0  0  0  0  0  0  0  0  0
#   -15.0526  -16.9445  -26.6871 N   0  0  0  0  0  0  0  0  0  0  0  0
#   -14.9347  -21.9631  -26.2988 C   0  0  0  0  0  0  0  0  0  0  0  0
#   -15.2162  -15.5610  -26.5929 C   0  0  0  0  0  0  0  0  0  0  0  0
#   -15.9031  -15.0059  -25.5037 C   0  0  0  0  0  0  0  0  0  0  0  0
#   -15.4462  -12.8187  -26.3599 C   0  0  0  0  0  0  0  0  0  0  0  0
#   -14.7773  -13.3552  -27.4525 C   0  0  0  0  0  0  0  0  0  0  0  0
#   -16.0203  -13.6235  -25.3815 C   0  0  0  0  0  0  0  0  0  0  0  0
#   -14.6768  -14.7359  -27.5934 C   0  0  0  0  0  0  0  0  0  0  0  0
#   -16.5313  -15.9392  -24.4895 C   0  0  0  0  0  0  0  0  0  0  0  0
#   -16.2584  -17.2435  -24.7671 N   0  0  0  0  0  0  0  0  0  0  0  0
#   -15.5317  -17.7669  -25.8203 C   0  0  0  0  0  0  0  0  0  0  0  0
#   -17.2406  -15.6098  -23.5374 O   0  0  0  0  0  0  0  0  0  0  0  0
#   -14.2525  -19.0464  -27.8382 H   0  0  0  0  0  0  0  0  0  0  0  0
#   -16.3981  -19.7943  -24.1510 H   0  0  0  0  0  0  0  0  0  0  0  0
#   -13.8938  -21.4078  -28.1049 H   0  0  0  0  0  0  0  0  0  0  0  0
#   -15.9903  -22.1635  -24.4209 H   0  0  0  0  0  0  0  0  0  0  0  0
#   -14.3604  -12.6891  -28.1964 H   0  0  0  0  0  0  0  0  0  0  0  0
#   -16.5458  -13.1713  -24.5494 H   0  0  0  0  0  0  0  0  0  0  0  0
#   -16.7352  -17.8915  -24.1540 H   0  0  0  0  0  0  0  0  0  0  0  0
#   -14.1941  -15.1755  -28.4537 H   0  0  0  0  0  0  0  0  0  0  0  0
#   -15.5319  -11.7476  -26.2520 H   0  0  0  0  0  0  0  0  0  0  0  0
#   -14.7660  -23.0224  -26.4244 H   0  0  0  0  0  0  0  0  0  0  0  0
#   1  2  2  0
#   1  3  1  0
#   1 16  1  0
#   2  4  1  0
#   2 18  1  0
#   3  5  2  0
#   3 19  1  0
#   4  7  2  0
#   4 20  1  0
#   5  7  1  0
#   5 21  1  0
#   6  8  1  0
#   6 16  2  0
#   7 27  1  0
#   8  9  2  0
#   8 13  1  0
#   9 12  1  0
#   9 14  1  0
#  10 11  1  0
#  10 12  2  0
#  10 26  1  0
#  11 13  2  0
#  11 22  1  0
#  12 23  1  0
#  13 25  1  0
#  14 15  1  0
#  14 17  2  0
#  15 16  1  0
#  15 24  1  0
# M  END
# """
# structure['reprType'] = 'BallAndStick'
# structure['carbonColor'] = 'red'
# data1 = """# generated using pymatgen
# data_Na2CrNiF7
# _symmetry_space_group_name_H-M   'P 1'
# _cell_length_a   7.27889000
# _cell_length_b   7.33433943
# _cell_length_c   7.33434858
# _cell_angle_alpha   89.52670711
# _cell_angle_beta   60.24975983
# _cell_angle_gamma   60.24971896
# _symmetry_Int_Tables_number   1
# _chemical_formula_structural   Na2CrNiF7
# _chemical_formula_sum   'Na4 Cr2 Ni2 F14'
# _cell_volume   280.04214068
# _cell_formula_units_Z   2
# loop_
#  _symmetry_equiv_pos_site_id
#  _symmetry_equiv_pos_as_xyz
#   1  'x, y, z'
# loop_
#  _atom_site_type_symbol
#  _atom_site_label
#  _atom_site_symmetry_multiplicity
#  _atom_site_fract_x
#  _atom_site_fract_y
#  _atom_site_fract_z
#  _atom_site_occupancy
#   Cr  Cr1  1  0.50000000  0.50000000  0.50000000  1.0
#   Cr  Cr2  1  0.50000000  0.00000000  1.00000000  1.0
#   F  F1  1  0.84896000  0.40104000  0.90104000  1.0
#   F  F2  1  0.15104000  0.59896000  0.09896000  1.0
#   F  F5  1  0.26844000  0.14265000  0.32047000  1.0
#   F  F6  1  0.73156000  0.85735000  0.67953000  1.0
#   F  F7  1  0.73156000  0.17953000  0.35735000  1.0
#   F  F8  1  0.26844000  0.82047000  0.64265000  1.0
#   F  F13  1  0.75447000  0.82680000  0.05766000  1.0
#   F  F14  1  0.63893000  0.17320000  0.94234000  1.0
#   F  F15  1  0.63893000  0.44234000  0.67320000  1.0
#   F  F16  1  0.75447000  0.55766000  0.32680000  1.0
#   F  F17  1  0.24553000  0.17320000  0.94234000  1.0
#   F  F18  1  0.36107000  0.82680000  0.05766000  1.0
#   F  F19  1  0.36107000  0.55766000  0.32680000  1.0
#   F  F20  1  0.24553000  0.44234000  0.67320000  1.0
#   Na  Na1  1  0.00000000  0.00000000  0.00000000  1.0
#   Na  Na2  1  0.00000000  0.50000000  0.50000000  1.0
#   Na  Na5  1  0.50000000  1.00000000  0.50000000  1.0
#   Na  Na6  1  1.00000000  0.00000000  0.50000000  1.0
#   Ni  Ni1  1  0.00000000  0.50000000  0.00000000  1.0
#   Ni  Ni2  1  0.50000000  0.50000000  0.00000000  1.0
# """

# uni_view_params = [{
#     "name": "structure",
#     "description": """[{
#     # 必填，目前支持pdb、sdf、mol、cif、dump、mmcif、mol2、POSCAR、xyz
#     format: 'sdf',
#     # 必填，结构文件内容
#     content: '',
#     # 非必填，展示模式，支持Line/Stick/BallAndStick/CPK/Ribbon
#     reprType: 'Line',
#     # 非必填，展示模式选择Line/Stick/BallAndStick/CPK时，支持传入carbonColor用于设置碳骨架的颜色
#     # 可以传入十六进制数颜色代码，如#f7aa61
#     # 也可以传入预设的颜色名（ligand-default/residue-default/reference/green/purple/pink/yellow/brown/gray/red/blue）
#     carbonColor: '#f7aa61'
# }]""",
#     "defaultValue": [structure],
#     "value": [structure],
#     "type": "list",
# }, {
#     "name": "height",
#     "description": "Height",
#     "defaultValue": 480,
#     "value": 480,
#     "type": "number",
# }]
# material_view_params = [{
#     "name": "materialFile",
#     "description": "必填，预览的结构文件内容",
#     "defaultValue": data1,
#     "value": data1,
#     "type": "string",
# }, {
#     "name": "format",
#     "description": "非必填，预览的结构文件格式，支持的文件预览格式包括：POSCAR、dump、xyz 和 cif",
#     "defaultValue": 'cif',
#     "value": 'cif',
#     "type": "enum",
#     "options": ["cif", "xyz", "dump", "POSCAR"]
# }, {
#     "name": "height",
#     "description": "非必填，组件高度",
#     "defaultValue": 480,
#     "value": 480,
#     "type": "number",
# }, {
#     "name": "style",
#     "description": "非必填，展示模式，支持Line/Stick/BallAndStick/CPK",
#     "defaultValue": 'BallAndStick',
#     "value": "BallAndStick",
#     "type": "enum",
#     "options": [["BallAndStick", "Ball&Stick"], ["Stick", "Stick"], ["Line", "Line"], ["CPK", "CPK"]]
# }]
# project_params = []
# machine_params = []

# with gr.Blocks(css=".column-form .wrap {flex-direction: column;}") as demo:
#     with gr.Row():
#         with gr.Column(visible=True, min_width=200, scale=0) as sidebar:
#             options = gr.Radio(["Uni-View", "Material-View", "Project", 'Machine',], value="Uni-View", label="Components", elem_classes="column-form")
#         with gr.Column(visible=True) as content:
#             title = gr.HTML("""<h2>Uni-View</h2>""")
#             uniview = uni_view(height=480, structures=[structure], visible=True)
#             materialview = material_viewer(materialFile=data1, format='cif', height=480, visible=False)
#             project = dp_project(visible=False)
#             machine = dp_machine(visible=False)
#             params = storybook_params_table(params=uni_view_params)
#             update_btn = gr.Button('Update')

#             def changed(value):
#                 structure, height = [item['value'] for item in uni_view_params]
#                 materialFile, format, material_height, style = [item['value'] for item in material_view_params]
#                 if value == "Uni-View":
#                     return [gr.HTML("""<h2>Uni-View</h2>"""), storybook_params_table(params=uni_view_params), uni_view(height=height, structures=structure, visible=True), material_viewer(materialFile=materialFile, format=format, height=material_height, style=style, visible=False), dp_project(visible=False), dp_machine(visible=False)]
#                 if value == 'Material-View':
#                     return [gr.HTML("""<h2>Material-View</h2>"""), storybook_params_table(params=material_view_params), uni_view(height=height, structures=structure, visible=False), material_viewer(materialFile=materialFile, format=format, height=material_height, style=style, visible=True), dp_project(visible=False), dp_machine(visible=False)]
#                 if value == 'Project':
#                     return [gr.HTML("""<h2>dp-project(需开启OAuth)</h2>"""), storybook_params_table(params=project_params), uni_view(height=height, structures=structure, visible=False), material_viewer(materialFile=materialFile, format=format, height=material_height, style=style, visible=False), dp_project(visible=True), dp_machine(visible=False)]
#                 if value == 'Machine':
#                     return [gr.HTML("""<h2>dp-machine(需开启OAuth)</h2>"""), storybook_params_table(params=machine_params), uni_view(height=height, structures=structure, visible=False), material_viewer(materialFile=materialFile, format=format, height=material_height, style=style, visible=False), dp_project(visible=False), dp_machine(visible=True)]
#             options.change(changed, inputs=options, outputs=[title, params, uniview, materialview, project, machine])
#             def update(key, params):
#                 if not params:
#                     return changed(key)
#                 global uni_view_params
#                 global material_view_params
#                 global project_params
#                 global machine_params
#                 if key == "Uni-View":
#                     uni_view_params = json.loads(params)
#                 if key == 'Material-View':
#                     material_view_params = json.loads(params)
#                 if key == 'Project':
#                     project_params = json.loads(params)
#                 if key == 'Machine':
#                     machine_params = json.loads(params)
#                 return changed(key)
#             update_btn.click(update, inputs=[options, params], outputs=[title, params, uniview, materialview, project, machine])
            
# demo.launch()
```

## `storybook_params_table`

### Initialization

<table>
<thead>
<tr>
<th align="left">name</th>
<th align="left" style="width: 25%;">type</th>
<th align="left">default</th>
<th align="left">description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>value</code></td>
<td align="left" style="width: 25%;">

```python
str | Callable | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">default text to provide in textbox. If callable, the function will be called whenever the app loads to set the initial value of the component.</td>
</tr>

<tr>
<td align="left"><code>placeholder</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">placeholder hint to provide behind textbox.</td>
</tr>

<tr>
<td align="left"><code>label</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">component name in interface.</td>
</tr>

<tr>
<td align="left"><code>every</code></td>
<td align="left" style="width: 25%;">

```python
float | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute.</td>
</tr>

<tr>
<td align="left"><code>show_label</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">if True, will display label.</td>
</tr>

<tr>
<td align="left"><code>scale</code></td>
<td align="left" style="width: 25%;">

```python
int | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">relative size compared to adjacent Components. For example if Components A and B are in a Row, and A has scale=2, and B has scale=1, A will be twice as wide as B. Should be an integer. scale applies in Rows, and to top-level Components in Blocks where fill_height=True.</td>
</tr>

<tr>
<td align="left"><code>min_width</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>160</code></td>
<td align="left">minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.</td>
</tr>

<tr>
<td align="left"><code>interactive</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">if True, will be rendered as an editable textbox; if False, editing will be disabled. If not provided, this is inferred based on whether the component is used as an input or output.</td>
</tr>

<tr>
<td align="left"><code>visible</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, component will be hidden.</td>
</tr>

<tr>
<td align="left"><code>rtl</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>False</code></td>
<td align="left">If True and `type` is "text", sets the direction of the text to right-to-left (cursor appears on the left of the text). Default is False, which renders cursor on the right.</td>
</tr>

<tr>
<td align="left"><code>elem_id</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.</td>
</tr>

<tr>
<td align="left"><code>elem_classes</code></td>
<td align="left" style="width: 25%;">

```python
list[str] | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.</td>
</tr>

<tr>
<td align="left"><code>render</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.</td>
</tr>

<tr>
<td align="left"><code>key</code></td>
<td align="left" style="width: 25%;">

```python
int | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">if assigned, will be used to assume identity across a re-render. Components that have the same key across a re-render will have their value preserved.</td>
</tr>

<tr>
<td align="left"><code>params</code></td>
<td align="left" style="width: 25%;">

```python
Any
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>
</tbody></table>


### Events

| name | description |
|:-----|:------------|
| `change` | Triggered when the value of the storybook_params_table changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input. |
| `input` | This listener is triggered when the user changes the value of the storybook_params_table. |
| `submit` | This listener is triggered when the user presses the Enter key while the storybook_params_table is focused. |



### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As output:** Is passed, passes text value as a {str} into the function.
- **As input:** Should return, expects a {str} returned from function and sets textarea value to it.

 ```python
 def predict(
     value: str | None
 ) -> str | None:
     return value
 ```
 
