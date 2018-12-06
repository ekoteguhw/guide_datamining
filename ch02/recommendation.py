from math import sqrt

# sample data
users = {
	"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
	"Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
	"Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
	"Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
	"Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
	"Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
	"Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
	"Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
	}

# Manhattan distance
def manhattan (rating1, rating2):
	distance = 0
	for key in rating1:
		if key in rating2:
			distance += abs(rating1[key] - rating2[key])

	return distance

# Example of Manhattan's distance
# print(manhattan(users["Dan"], users["Chan"]))

# Minkowski distance
# Generalization Manhattan Distance (r = 1) and Euclidan Distance (r = 2)
def minkowski(rating1, rating2, r):
	distance = 0
	commonRatings = False
	for key in rating1:
		if key in rating2:
			distance += pow(abs(rating1[key] - rating2[key]), r)
			commonRatings = True

	if commonRatings:
		return pow(distance, 1/r)
	else:
		return 0 # No rating in common

# List of Nearest Neighbor
def nearestNeighbor(username, users):
	distances = []

	for user in users:
		if user != username:
			#distance = manhattan(users[user], users[username])
			distance = minkowski(users[user], users[username], 2)
			distances.append((distance, user))

	# after calculate, sort
	distances.sort()
	return distances

# Example of Nearest Neighbor
# print(nearestNeighbor("Veronica", users))

# Recommendation System
def recommendation(username, users):
	# Find the nearest neighbor
	nearest = nearestNeighbor(username, users)[0][1]
	recommendations = []
	# Find ratings that user doesn't have what nearest has
	neighborRatings = users[nearest]
	userRatings = users[username]
	for artist in neighborRatings:
		if not artist in userRatings:
			recommendations.append((artist, neighborRatings[artist]))

	# Sort using fn sorted
	return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse=True)

# Example of recommendation
# print(recommendation("Hailey", users))

# The Pearson Correlation Coefficient
# is a measure of correlation between two variables (the correlation between A and B). 
# It ranges between -1 and 1 inclusive. 1 indicates perfect agreement. -1 indicates perfect disagreement. 

def pearson(rating1, rating2):
	sum_xy = 0
	sum_x = 0
	sum_y = 0
	sum_x2 = 0
	sum_y2 = 0
	n = 0

	for key in rating1:
		if key in rating2:
			n += 1
			x = rating1[key]
			y = rating2[key]
			sum_xy += x * y
			sum_x += x
			sum_y += y
			sum_x2 += x ** 2
			sum_y2 += y ** 2

	# if no rating in common return 0
	if n == 0:
		return 0
  
  # compute denominator
  denominator = sqrt( sum_x2 - (sum_x ** 2) / n ) * sqrt( sum_y2 - (sum_y ** 2) / n )
  if denominator == 0:
  	return 0
  else:
  	return (sum_xy - (sum_x * sum_y) / n) / denominator

# Example of Pearson Correlation
print(pearson(users["Angelica"], users["Bill"]))

