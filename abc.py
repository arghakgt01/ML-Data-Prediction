from graphviz import Source
path = 'MusicRecommender.dot'
s = Source.from_file(path)
s.view()

# import os
# os.environ["PATH"] += os.pathsep + 'C:\Program Files (x86)\Graphviz2.38\bin'