import IPython, ipywidgets, os
import matplotlib.pyplot as plt
class ColabOutput(object):
    def __init__(self, locals=None):
        if not hasattr(self, 'output'):
            from google.colab import output
            output.enable_custom_widget_manager()
            self.output = ipywidgets.Output()
            IPython.display.display(self.output)
        PingColab()
    def __enter__(self):
        self.output.__enter__()
        IPython.display.clear_output(True)
    def __exit__(self, *args):
        plt.show()
        self.output.__exit__(*args)
    def __new__(cls, locals=None):
        if not locals:
            return super().__new__(cls)
        if 'c01ab' not in locals:
            locals['c01ab'] = super().__new__(cls)
        return locals['c01ab']

class ColabPlot(ColabOutput): pass
def PingColab() -> None:
    if os.path.exists('/content/stop'): 1/0
