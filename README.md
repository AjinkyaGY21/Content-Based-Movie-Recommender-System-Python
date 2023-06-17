What are Recommender Systems
============================

1.Uses data to help predict, narrow down, and find what people are looking for among an exponentially growing number of options.

2.An AI algorithm that uses Big Data to suggest or recommend additional products to consumers. 

3.Driving personalized user experiences, deeper engagement with customers

4.These recommendations can be based on various criteria, including past purchases, search history, demographic information, and other factors. 

5.Help users discover products and services they might otherwise have not found on their own.

6.Trained to understand the preferences, previous decisions, and characteristics of people and products using data gathered about their interactions(impressions, clicks, likes, and purchases).

7.Predict consumer interests and desires on a highly personalized level,so used by content and product providers

Types of Recommender Systems
---------------------------
1.content-based        
2.collaborative filtering(users of similar ratings,  interests) 
*     i. model-based 
*     ii.memory-based  *   a.User-based  
                           b.Item-based            
3.hybrid           
4.context filtering.(similar content)      
                            
                                                               
 __Collaborative filtering__ : 
 ---------------------------
 have data about which interactions have occurred in the past, you’ll probably be interested in collaborative filtering.

recommend items based on preference information from many users
uses similarity of user preference behavior, given previous interactions between users and items, recommender algorithms learn to predict future interaction. 
build a model from a user’s past behavior, such as items purchased previously or ratings given to those items and similar decisions by other users. 
some people have made similar decisions and purchases in the past, then there is a high probability they will agree on additional future selections.                                                              

CF uses the concept of user-item interaction matrix or Matrix factorization 
=> includes tech. like word embedding and topic modeling, MF can be used to calculate the similarity in user’s ratings or interactions to provide recommendations.

Matrix factorization using the  alternating least squares (ALS) algorithm => approximates the sparse user item rating matrix u-by-i as the product of two dense matrices, 
user and item factor matrices of size u × f and f × i  (where u is the number of users, i the number of items and f the number of latent features) . 
The factor matrices represent latent or hidden features which the algorithm tries to discover. 
One matrix tries to describe the latent or hidden features of each user, and one tries to describe latent properties of each item. 
For each user and for each item, the ALS algorithm iteratively learns (f) numeric “factors” that represent the user or item. 
In each iteration, the algorithm alternatively fixes one factor matrix and optimizes for the other, and this process continues until it converges.  


**Content based filtering** : 
--------------------------
you have data describing the user and items they have interacted with recommendations can be made by using content and context filtering. 

uses the attributes or features of an item to recommend other items similar to the user’s preferences. 
based on similarity of item and user features, given information about a user and items they have interacted with. 
eg. if you liked the movies(ABC and ACD), it might recommend another movie(CDG) to you with the same genres and/or cast 


**Hybrid recommender systems**
------------------------------ 
combine both to create a more comprehensive recommending system


**Context filtering**
--------------------- 
includes users’ contextual information in the recommendation process. 
uses a sequence of contextual user actions, plus the current context, to predict the probability of the next action. 
In the Netflix example, given one sequence for each user—the country, device, date, and time when they watched a movie => they trained a model to predict what to watch next. 


**USE CASES and APPLICATIONS** :
----------------------------- 
1. E-Commerce & Retail: Personalized Merchandising 
   ##### Complete the look” or “You might also like” sections in e-commerce platforms like Amazon, Walmart, Target, Flipkart
2. Media & Entertainment: Personalized Content
   ##### analyze an individual’s purchase behavior and detect patterns that will help provide them with the content suggestions that matches his/her interests. 
   ##### Google and Facebook recommends relevant ads, or what Netflix does to recommend movies and TV shows.
3. Personalized Banking
   ##### A mass market product that is consumed digitally by millions, banking is prime for recommendations. Knowing a customer’s detailed financial situation and their past preferences, coupled by data of thousands of similar users, is quite powerful.


**WHY even recommend ???**
--------------------------

## 1. Improving retention
#### retain them as loyal subscribers or shoppers -> truly understood by a brand -> far more likely to remain loyal and continue shopping at your site.
## 2. Increasing sales
#### increases in upselling revenue from 10-50% resulting from accurate ‘you might also like’ product recommendations. 
#### adding matching product recommendations to a purchase confirmation; sharing information on ‘what customers are buying now’; and sharing other buyers’ purchases and comments.
## 3.Helping to form customer habits and trends
#### Consistently serving up accurate and relevant content -> influence usage patterns in customers.
## 4.Speeding up the pace of work. 
## 5.Boosting cart value. 
#### vast products to suggest from -> challenging product suggestions -> using various means of filtering, these ecommerce titans can find just the right time to suggest new products customers are likely to buy, either on their site or through email or other means.


**Why Recommendation Systems Run Better with GPUs**
----------------------------------------------------
The mathematical operations underlying many machine learning algorithms are often matrix multiplications. These types of operations are highly parallelizable and can be greatly accelerated using a GPU. 

A GPU is composed of hundreds of cores that can handle thousands of threads in parallel. Because neural nets are created from large numbers of identical neurons they are highly parallel by nature. This parallelism maps naturally to GPUs,  which can deliver a 10X higher performance than CPU-only platforms.