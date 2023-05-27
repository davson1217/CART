from pandas import Index, DataFrame
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz, plot_tree
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from rules import letter_a_context_rules, all_rules
from helpers import encode_features, drop_categorical_features, name_vectorize
import matplotlib.pyplot as plt
import graphviz
from sklearn.preprocessing import LabelEncoder
from typing import List
import json


def visualize_tree(clf, feature_names, target_data_frame: DataFrame, proper_name):
    # Generate the tree visualization in DOT format
    dot_data = export_graphviz(clf,
                               out_file=None,
                               feature_names=feature_names,
                               class_names=sorted(target_data_frame.unique()),
                               filled=True, rounded=True,
                               label='all'
                               )
    # Create a Graph object from the DOT data
    graph = graphviz.Source(dot_data)
    output_path = f"viz/_{proper_name}_"
    graph.format = 'svg'
    graph.render(output_path)

    return


def tree_properties(clf: DecisionTreeClassifier):
    number_of_leaves = clf.get_n_leaves()
    tree_depth = clf.get_depth()

    return {
        "leaves": number_of_leaves,
        "depth": tree_depth
    }


def adapt_name(name: str, visualize_clf: bool):
    df = pd.DataFrame(all_rules)
    data_frame = df.fillna("No")
    # print(data_frame.head())
    xInputs = data_frame.drop("transcription", axis="columns")
    target = data_frame["transcription"]
    original_x_columns = xInputs.columns
    # print(f"transformed_train_data \n {xInputs}")

    # label-encode categorical features
    encoded_features = encode_features(original_x_columns, xInputs)
    transformed_train_data = encoded_features['transformed_train_data']
    # fittedLabelEncoder = encoded_features['label_encoder']

    # drop categorical features
    numerical_features = drop_categorical_features(transformed_train_data, original_x_columns)

    # transform name into vector
    vectorized_name = name_vectorize(name.upper())
    # print(f"vectorized_name -> {vectorized_name}")

    # initialize decision tree classifier
    model = DecisionTreeClassifier()

    # numbered_letters_check = numerical_features['le_letter']
    # print(numerical_features)

    # train model
    model.fit(numerical_features, target.values)

    # predict
    prediction = model.predict(vectorized_name)

    # ==================== Post Prediction ====================
    if visualize_clf:
        visualize_tree(model, original_x_columns, target, proper_name=name.lower())
    tree_props = tree_properties(model)
    # ==================== Post Prediction ====================

    # read the generated viz diagram
    with open(f'viz/_{name.lower()}_.svg', 'r') as file:
        viz_content = file.read()

    # print(f'viz content => {viz_content}')

    return {
        "prediction": ''.join(prediction),
        "leaves": str(tree_props['leaves']),
        "depth": str(tree_props['depth']),
        "viz": json.dumps({'svg_image': viz_content})
    }

# adapt_name("alao", True)
