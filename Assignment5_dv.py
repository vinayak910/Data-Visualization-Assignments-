                                                    #Assignment 5
#question 1
# import numpy as np
# from scipy.spatial import distance
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.metrics import jaccard_score

# customer_A = [4,5,2,3,4]
# customer_B = [5,3,2,4,5]

# customer_A_binary = [1,0,1,1,0,1]
# customer_B_binary = [1,1,1,0,0,1]

# #euclidean distance
# euclidean_dis = distance.euclidean(customer_A,customer_B)
# print(f"Euclidean distance is:{euclidean_dis:.2f}")

# #Manhattan distance
# manhattan_dis = distance.cityblock(customer_A,customer_B)
# print(f"Manhattan distance is:{manhattan_dis:.2f}")

# #Hamming distance
# hamming_dis = distance.hamming(customer_A_binary,customer_B_binary)*len(customer_A_binary)
# print(f"Hamming distance is:{hamming_dis:.2f}")

# #cosine_similarity
# cosine_sim = cosine_similarity([customer_A],[customer_B])[0][0]
# print(f"cosine_similarity is:{cosine_sim:.2f}")

import numpy as np
from scipy.spatial import distance


#question2
user1 = [5,3,4,4,2]
user2 = [4,2,5,4,3]

#chebyshev distance
chebyshev_dis = distance.chebyshev(user1,user2)
print(f"Chebyshev distance is:{chebyshev_dis:.2f}")

#Minkowski Distance
minkowski_dis = distance.minkowski(user1,user2,3)
print(f"Minkowski distance is:{minkowski_dis:.2f}")