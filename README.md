# Books Recommender System Using Machine Learning

## Overview

This project implements a book recommendation system using machine learning techniques. The goal is to suggest books to users based on their preferences, reading history, and similarities between books, aiming to enhance user discovery and engagement on a hypothetical book platform.

## Features

* **User-Based Recommendations**: Suggests books favoured by users with similar rating patterns.
* **Item-Based Recommendations**: Suggests books similar (based on user interactions) to those a user has previously liked or rated highly.
* **Content-Based Filtering**: Recommends books based on attributes like genre and author, matching them with a user's profile.

## Methodology & Algorithms

This recommendation system utilizes the following machine learning approaches:

* **Collaborative Filtering (Item-Item)**: Calculates similarity between books based on user rating patterns (e.g., using Cosine Similarity or Pearson Correlation on the user-item interaction matrix) and recommends books similar to those the user liked.
* **Content-Based Filtering (TF-IDF)**: Creates TF-IDF (Term Frequency-Inverse Document Frequency) vectors from book descriptions or genres. Recommends books whose content vectors are most similar (using Cosine Similarity) to the user's profile vector (derived from the content of books they liked).

## Technologies Used

* **Language**: Python 3.9
* **Libraries**:
    * Pandas (Data manipulation and analysis)
    * NumPy (Numerical operations)
    * Scikit-learn (TF-IDF, Cosine Similarity, evaluation metrics)
    * NLTK (Text processing for content-based filtering)
    * Matplotlib / Seaborn (Data visualization)
