import pickle
import streamlit as st
import numpy as np

st.header("Book Recommender System")
# to run, go in the terminal and run : streamlit run app.py

model = pickle.load(open('artifacts/model.pkl', 'rb'))
books_name = pickle.load(open('artifacts/books_name.pkl', 'rb'))
final_rating = pickle.load(open('artifacts/final_rating.pkl', 'rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))


def fetch_image(suggestion):
    books_name = []
    ids_index = []
    img_url = []

    for book_id in suggestion:
        books_name.append(book_pivot.index[book_id])
    
    for book_name in books_name[0]:
        ids = np.where(final_rating["title"] == book_name)
        ids_index.append(ids)
    
    for ids in ids_index:
        url = final_rating["img_url"].iloc[ids]
        img_url.append(url)
    
    return img_url

def recommend_books(book_name):
    book_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1,-1), n_neighbors=6)

    img_url = fetch_image(suggestion)
    
    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for book in books:
            book_list.append(book)
    
    return book_list, img_url

seleted_book = st.selectbox(
    "Type or select a book",
    books_name
)

if st.button("Show recommendation"):
    recommendation_books, img_url = recommend_books(seleted_book)
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(img_url[1])
        #st.text(recommendation_books[1])
        #st.image(f"{img_url[1]}")

    with col2:
        st.text(recommendation_books[2])
        #st.image(img_url[2])

    with col3:
        st.text(recommendation_books[3])
        #st.image(img_url[3])

    with col4:
        st.text(recommendation_books[4])
        #st.image(img_url[4])

    with col5:
        st.text(recommendation_books[5])
        #st.image(img_url[5])

    
    

