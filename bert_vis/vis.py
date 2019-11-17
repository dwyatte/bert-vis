from umap import UMAP
from bokeh.layouts import column
from bokeh.plotting import Figure, curdoc, ColumnDataSource
from bokeh.models.widgets import Paragraph, TextInput, Button

import utils

class Visualization:

    COLORS = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

    def __init__(self):
        # widgets
        self.instructions = Paragraph(text='Enter a word')
        self.text_input = TextInput(value='""')
        self.submit_button = Button(label='Submit', button_type="success")
        self.figure = Figure()
        self.projector = UMAP()
        self.layout = column(self.instructions,
                             self.text_input,
                             self.submit_button,
                             self.figure)

        self.submit_button.on_click(self.handle_submit)

    def handle_submit(self):
        filename_sentence_pairs = utils.get_sentences(self.text_input.value)
        sentences = [pair[1] for pair in filename_sentence_pairs]
        encodings = utils.get_encodings(sentences)
        embedding = self.projector.fit_transform(encodings)

        filename_to_color = dict()
        for filename, _ in filename_sentence_pairs:
            if filename not in filename_to_color:
                filename_to_color[filename] = self.COLORS[len(filename_to_color)]
        color = [filename_to_color[filename] for filename, _ in filename_sentence_pairs]

        source = ColumnDataSource(data=dict(
            x=embedding[:, 0],
            y=embedding[:, 1],
            text=sentences,
            fill_color=color
        ))

        figure = Figure(tooltips=[('text', '@text')])
        figure.circle('x', 'y', fill_color='fill_color', radius=.05, line_color=None, source=source)
        self.layout.children[-1] = figure


visualization = Visualization()
curdoc().add_root(visualization.layout)

