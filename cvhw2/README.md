# Computer Vision Homework 2

```bash
conda create -n cvhw2 python=3.7
conda activate cvhw2
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
python -m ipykernel install --user --name=cvhw2
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
jupyter nbextension enable varInspector/main
```
