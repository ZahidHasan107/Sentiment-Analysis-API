import json  # Importing the json module to work with JSON data

from transformers import pipeline

# Importing the pipeline class from the transformers library

specific_model = pipeline(
    model="finiteautomata/bertweet-base-sentiment-analysis")  # Creating a sentiment analysis pipeline using the "finiteautomata/bertweet-base-sentiment-analysis" model


def sentiment(data):
    # Performing sentiment analysis on the input data using the specific_model pipeline
    analysis_Data = specific_model(data)
    # Converting the sentiment analysis result to a JSON string representation
    analysis_jsonString = json.dumps(analysis_Data[0])

    # Loading the JSON string back into a dictionary
    analysis_json = json.loads(analysis_jsonString)

    # Checking the value of the "label" key in the dictionary
    if analysis_json["label"] == "POS":
        # If the label is "POS", changing it to "Positive"
        analysis_json["label"] = "Positive"
    elif analysis_json["label"] == "NEG":  # If the label is "NEG"
        analysis_json["label"] = "Negative"  # Changing it to "Negative"
    else:
        # If the label is neither "POS" nor "NEG", changing it to "Neutral"
        analysis_json["label"] = "Neutral"

    analysis = {
        # Creating a new dictionary with the updated sentiment label
        "sentiment": analysis_json["label"],
    }
    return analysis  # Returning the dictionary containing the sentiment label
