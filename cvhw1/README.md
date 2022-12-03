# Computer Vision Homework 1

## Installation

```bash
conda create -n cvhw1 python=3.7
conda activate cvhw1
```

You can install requirements with the following command in the homework directory:

```bash
pip install -r requirements.txt
```

In order to visualize plotly plots in jupyter notebooks, you should run the command given below.

```bash
conda install nodejs
```

Add your conda environment to Jupyter Notebook and enable widget rendering.

```bash
python -m ipykernel install --user --name=cvhw1
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
jupyter nbextension enable varInspector/main
```
