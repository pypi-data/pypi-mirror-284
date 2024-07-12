import weka.core.jvm as jvm
from weka.core.converters import load_any_file
from weka.classifiers import Classifier, Evaluation
from weka.core.classes import Random

jvm.start()

data = load_any_file("/home/fracpete/development/datasets/uci/labor.arff", class_index="last")

cls = Classifier(classname="weka.classifiers.trees.RandomForest")
evl = Evaluation(data)
evl.crossvalidate_model(cls, data, 10, Random(1))
print(evl.summary())
print(evl.class_details())
print(evl.matrix())

jvm.stop()
