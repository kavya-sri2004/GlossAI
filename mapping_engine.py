
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def build_column_description(df, column_name, sample_size=5):
    sample_values = (
        df[column_name]
        .dropna()
        .astype(str)
        .head(sample_size)
        .tolist()
    )

    sample_text = " ".join(sample_values)

    return f"{column_name} {sample_text}"


def suggest_mappings(df, glossary_df):

    # Create descriptions for dataset columns
    column_descriptions = [
        build_column_description(df, column)
        for column in df.columns
    ]

    # Create descriptions for glossary terms
    glossary_descriptions = (
        glossary_df["term"].astype(str)
        + " "
        + glossary_df["description"].astype(str)
        + " "
        + glossary_df["category"].astype(str)
    ).tolist()

    # Combine descriptions for TF-IDF processing
    all_text = column_descriptions + glossary_descriptions

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2)
    )

    tfidf_matrix = vectorizer.fit_transform(all_text)

    # Separate dataset and glossary vectors
    column_vectors = tfidf_matrix[:len(column_descriptions)]

    glossary_vectors = tfidf_matrix[len(column_descriptions):]

    # Calculate similarity
    similarity_matrix = cosine_similarity(
        column_vectors,
        glossary_vectors
    )

    results = []

    # Find the best glossary match for each dataset column
    for index, column_name in enumerate(df.columns):

        best_match_index = similarity_matrix[index].argmax()

        best_term = glossary_df.iloc[best_match_index]

        similarity_score = similarity_matrix[
            index,
            best_match_index
        ]

        results.append({
            "Dataset Column": column_name,
            "Suggested Glossary Term": best_term["term"],
            "Description": best_term["description"],
            "Category": best_term["category"],
            "Similarity Score": round(
                float(similarity_score),
                3
            )
        })

    return pd.DataFrame(results)
