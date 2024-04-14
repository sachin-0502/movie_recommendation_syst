# Movie Recommendation System

[LIVE DEMO](https://movierecommendationsyst-pa3bdka3kfsv2nek9onxob.streamlit.app/) 


### Project Overview
This project aims to recommend the top 10 similar movies based on the movie name which is entered by the user. The project works in such a way that the content of input movie and content of the recommended movies will be the best possible similar match.
Although the recommendation system is also possible in the form of collaborative filtering based method which recommend movie based on the user interest but, here I used the content based approach.

### Project Output
The output is in the form of webpage which is designed using streamlit module. The webpage consist the list of all available movies which can be manually typed either and a button to fetch the result. <p> </p>
![image](https://github.com/sachin-0502/movie_recommendation_syst/assets/144464445/f35896e9-a8a8-4bba-a309-502275f2981b)


Thus, we can get the recommendation of 10 similar movies to the input movies.
### Tools and libraries used
- Tools - Jupyter notebook, VS code
- Libraries - numpy, pandas, pickle, streamlit

## Project Flow


### Data Sources
TMDB Movies dataset from Kaggle which consists two csv files containing data of 5000 movies.
- tmdb_5000_credits = | movie_id | title | cast | crew |
- tmdb_5000_movies  = | budget | genre | homepage | id | keywords | original_language | orginal_title | overview | popularity | production_companies | tagline | title | vote | budget | runtime | status | spoken_language |



### Data Preprocessing
1. Merge both datasets by considering 'title' as the foreign key
- movies.merge(credits,on='title')
2. Feature Selection to use only required columns
- genres, movie_id, keywords, title, overview, cast, crew
3. Changed the data type of every column as per the requirement
4. Created useful tags using:
- tags = genres + keywords + top 3 cast + only director from crew + overview
5. Remove same word ambiguity ( remove blank spaces )
6. convert generated tags into lower case.

### Processed Data
After performing all the necessary preprocessing and generating necessary tags the processed dataset we get in the below form.<p> </p> 

![image](https://github.com/sachin-0502/movie_recommendation_syst/assets/144464445/d7532d5f-bf6e-4bd8-ad01-41933e08587f)


For doing further text analysis we need to convert these generated tags to vectors with the help of vectorization ( Bag of Words ) method.

### Vectorization
First, combine all the generated tags tinto a LARGE TEXT and found 5000 most common words from this LARGE TEXT whose frequency is high. This is done using CountVectorizer class of scikit learn. <p> </p>
- from sklearn.feature_extraction.text import CountVectorizer
- cv=CountVectorizer(max_features=5000,stop_words='english') <p> </p>
Now got a matrix of [5000*5000]

### Stemming
Stemming helps in normalizing words with the same meaning but different forms. For example, "running," "runs," and "runner" all stem to "run," making it easier to analyze them as the same concept.<p> </p>
PorterStemmer class from nltk (natural language toolkit) library is used.  

### Similarity score
Since the every vector present in the dataset is now representing a point in a 5000 Dim. space. To calculate similarity score, we would use cosine distance i.e. angle between every vector/movie which will be [0,1].
- using cosine_similarity class from sklearn
- Angle will be directly prop. to similarity between movies.
  from sklearn.metrics.pairwise import cosine_similarity  
  cosine_similarity(vectors)

### Output function
Defining a function which will first take the movie name and then fetch its index number from the dataframe and after fetching index number the same index's similarity vector will be fetched where top the similarity array will be sorted in descending order and from there we will fetch top 10 movies

### Output
![image](https://github.com/sachin-0502/movie_recommendation_syst/assets/144464445/b8deb19e-a654-4d0c-9299-8f968c01b57c)

# Store Analyzed Results
To make the webpage we need to integrate the above analysis and recommendation logic into a python file which could be run directly through live server and can be deployed to any platform.
### Dump the useful files

#### Used pickle module
The pickle module in Python is used for serializing and deserializing Python objects. This allows to save Python objects to a file or transfer them over the network and then load them back into the Python program. 
- Dumped the similarity vector to a pickle file ( to find the similarity score )
- Dumped the processed data to a pickle file ( to find the entered movie index )

#### Pickle file
Pickle files are files that contain serialized Python objects. These files have the extension .pkl or .pickle. Pickle files can store various types of Python objects, including lists, dictionaries, functions, and even instances of custom classes.

# WebPage Creation
In VS studio IDE , I used streamlit module to make the webpage after loading the required pickle files for necessary logical operations. Created function to recommend 10 most similar movies and all the required python scripting was done in a python file. <p> </p>


### How to run the project ?
Open the python file and run streamlit command in the terminal.
- streamlit run <file_name.py>





 
