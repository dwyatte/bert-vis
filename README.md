# bert-vis
![](screenshot.gif)

This repo implements the BERT word sense visualization described in section 4.1 of [Visualizing and Measuring the Geometry of BERT](https://arxiv.org/abs/1906.02715). I have found it useful for investigating domain shift for a given word, e.g., the word "die" in the above example (Toys and Games vs. Video Games from [Julian McAuley's Amazon Review dataset](http://jmcauley.ucsd.edu/data/amazon/)).

# Usage
In `docker-compose.yaml`:

* Edit the `MODEL_DIR` and `CKPT_NAME` environmental variables of the `bert-server` service to point to the BERT model directory and checkpoint (this project uses [Han Xiao's bert-as-a-service](https://github.com/hanxiao/bert-as-service), see its README for more info).

* Edit the `INPUT_FILES` environmental variable in the `bert-vis` service to point to line-delimited input files, each of which will be mapped to a different colored marker in the visualization. 

Run `docker-compose up bert-vis` to start the visualization service. The visualization runs using [Bokeh](https://bokeh.org/) on `http://localhost:5006/vis`. By default, the BERT model runs as a single process on CPU and up to 500 matching sentences per input file will be visualized.

