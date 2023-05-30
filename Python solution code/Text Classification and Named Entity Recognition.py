import text_classification_model
import named_entity_recognition_model

for post in posts:
    # Classify sentiment of the post
    sentiment = text_classification_model.classify_sentiment(post.content)

    # Extract printer brand and model
    brand, model = named_entity_recognition_model.extract_brand_and_model(post.content)

    # Extract features mentioned in the post
    features = named_entity_recognition_model.extract_features(post.content)

    # Extract problems mentioned in the post
    problems = named_entity_recognition_model.extract_problems(post.content)

    # Store the extracted information for further processing
   
