from pandas import DataFrame
from sklearn.preprocessing import LabelEncoder
from typing import List

from rules import yoruba_letters, encodings, yoruba_vowels


def encode_features(headers: List[str], train_data: DataFrame):
    # print(f'data to encode => \n', train_data)
    transformed_train_data = train_data
    label_encoder = LabelEncoder()
    for header in headers:
        transformed_train_data[f'le_{header}'] = label_encoder.fit_transform(transformed_train_data[header])

    return {'transformed_train_data': transformed_train_data, "label_encoder": label_encoder}


def drop_categorical_features(encoded_features: DataFrame, categorical_columns: List[str]):
    numerical_features = encoded_features.drop(categorical_columns, axis="columns")

    return numerical_features


def name_vectorize(proper_name: str):
    vector = []
    letter_encoding_alignment = dict(zip(yoruba_letters, encodings))

    for i in range(len(proper_name)):
        sublist = []
        letter = proper_name[i]

        # Condition 1: Check if the letter is a vowel
        if letter in yoruba_vowels:
            sublist.append(1)
        else:
            sublist.append(0)

        # Condition 2: Append letter_encoding in index 1 of the sublist
        sublist.append(letter_encoding_alignment[letter])

        # Condition 3: Check if the preceding letter is 'N'
        if i > 0 and proper_name[i - 1] == 'N':
            sublist.append(1)
        else:
            sublist.append(0)

        # Condition 4: Check if the succeeding letter is 'N'
        if i < len(proper_name) - 1 and proper_name[i + 1] == 'N':
            sublist.append(1)
        else:
            sublist.append(0)

        # Condition 5: Check if the succeeding letter is the same as the current letter
        if i < len(proper_name) - 1 and proper_name[i + 1] == letter:
            sublist.append(1)
        else:
            sublist.append(0)

        # Condition 6: Check if the preceding letter is the same as the current letter
        if i > 0 and proper_name[i - 1] == letter:
            sublist.append(1)
        else:
            sublist.append(0)

        # Condition 7: Check if the letter is diphthong i.e., vowel glide
        if letter in yoruba_vowels and i > 0 and proper_name[i - 1] == 'I':
            sublist.append(1)
        else:
            sublist.append(0)

        vector.append(sublist)

    return vector
