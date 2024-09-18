import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset: movies and user ratings/preferences
movies = pd.DataFrame({
    'movie_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'title': ['Extraction', 'The Wolf of Wall Street', 'Shazam', 'The Forge', 'Cars 4', 'Smile', 'Trap', 'My Fault', 'The Long Game', 'Joker: Folie à Deux'],
    'genre': ['Action', 'Biography', 'Comedy', 'Drama', 'Family', 'Horror', 'Mystery', 'Romance', 'Sport', 'Thriller']
})

ratings = pd.DataFrame({
    'user_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'movie_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'rating': [5, 4, 3, 5, 2, 5, 4, 2, 4, 5]
})

# Collaborative Filtering Recommendation
def collaborative_filtering(user_id, ratings, movies):
    # Pivot the ratings matrix (users x movies)
    user_movie_matrix = ratings.pivot_table(index='user_id', columns='movie_id', values='rating').fillna(0)
    
    # Compute similarity between users using cosine similarity
    user_similarity = cosine_similarity(user_movie_matrix)
    
    # Convert similarity matrix into a DataFrame for easy access
    user_similarity_df = pd.DataFrame(user_similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)
    
    # Get the most similar users for the given user_id
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)
    
    # Get the ratings of the most similar user
    most_similar_user_id = similar_users.index[1]  # Exclude the first user as it will be the same user
    
    # Get the movies rated by the most similar user but not rated by the current user
    current_user_ratings = user_movie_matrix.loc[user_id]
    most_similar_user_ratings = user_movie_matrix.loc[most_similar_user_id]
    
    # Recommend movies that the current user has not rated
    recommendations = most_similar_user_ratings[most_similar_user_ratings > 0].index.difference(current_user_ratings[current_user_ratings > 0].index)
    
    return movies[movies['movie_id'].isin(recommendations)]['title'].tolist()

# Content-Based Filtering Recommendation
def content_based_filtering(user_id, ratings, movies):
    # Merge movies and ratings
    movie_ratings = pd.merge(ratings, movies, on='movie_id')
    
    # Get the movies the user has rated
    user_ratings = movie_ratings[movie_ratings['user_id'] == user_id]
    
    # Get the user's favorite genre by averaging their ratings per genre
    user_preferences = user_ratings.groupby('genre')['rating'].mean().sort_values(ascending=False)
    
    # Find the top-rated genre for the user
    if not user_preferences.empty:
        top_genre = user_preferences.idxmax()
        
        # Recommend movies in the top genre that the user has not already rated
        recommendations = movies[(movies['genre'] == top_genre) & (~movies['movie_id'].isin(user_ratings['movie_id']))]
        return recommendations['title'].tolist()
    else:
        return []

# Main program to choose between Collaborative or Content-based Filtering
def main():
    print("Welcome to the Recommendation System!")
    print("Please choose a recommendation method:")
    print("1. Collaborative Filtering")
    print("2. Content-Based Filtering")
    
    choice = input("Enter your choice (1 or 2): ")
    user_id = int(input("Enter your user ID (1, 2, 3, 4, 5, 6, 7, 8, 9 or 10): "))
    
    if choice == '1':
        print("\nUsing Collaborative Filtering...")
        recommendations = collaborative_filtering(user_id, ratings, movies)
    elif choice == '2':
        print("\nUsing Content-Based Filtering...")
        recommendations = content_based_filtering(user_id, ratings, movies)
    else:
        print("Invalid choice. Please select 1 or 2.")
        return
    
    if recommendations:
        print(f"Recommended movies for user {user_id}: {', '.join(recommendations)}")
    else:
        print(f"No recommendations available for user {user_id}.")

if __name__ == "__main__":
    main()
