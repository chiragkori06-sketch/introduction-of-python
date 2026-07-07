import sys


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


# 1. Create variables for user details.
print("Question 1")
user_name = "chirag"
fav_app = "Spotify"
daily_usage_hours = 2.5

print("User name:", user_name)
print("Favorite app:", fav_app)
print("Daily usage hours:", daily_usage_hours)


# 2. Declare Flipkart product variables and print their data types.
print("\nQuestion 2")
product_name = "Boat Airdopes 141"
price = 1299.00
is_available = True

print("Product name:", product_name, "| Type:", type(product_name))
print("Price:", price, "| Type:", type(price))
print("Is available:", is_available, "| Type:", type(is_available))


# 3. Demonstrate single-line and multi-line comments.
print("\nQuestion 3")

# Spotify may check the songs a user plays often.
# It can compare those songs with similar users and artists.
# Then it can recommend playlists based on mood, genre, and listening history.

"""
A Spotify playlist recommendation system might work like this:
1. Collect the user's listening history.
2. Find favorite artists, genres, and moods.
3. Compare the user with people who have similar music taste.
4. Recommend playlists that match the user's recent activity.
"""

recent_artist = "Arijit Singh"
playlist_mood = "Chill"
recommended_playlist = f"{playlist_mood} Mix - Featuring {recent_artist}"

print("Recommended playlist:", recommended_playlist)


# 4. Create Zomato order variables and print a sentence.
print("\nQuestion 4")
order_total = 749.50
delivery_region = "Mumbai"
discount_percent = 15

print(
    f"Order from {delivery_region} totals \u20b9{order_total} "
    f"with {discount_percent}% discount."
)


# 5. Show mixed indentation code, then run the fixed version.
print("\nQuestion 5")

mixed_indentation_code = """
def check_delivery_status(is_delivered):
    if is_delivered:
        print("Order delivered")
\t    print("Thank you for ordering")
    else:
        print("Order is still on the way")
"""

print("Incorrect code with mixed tabs and spaces:")
print(mixed_indentation_code)

print("Fixed code output:")


def check_delivery_status(is_delivered):
    if is_delivered:
        print("Order delivered")
        print("Thank you for ordering")
    else:
        print("Order is still on the way")


check_delivery_status(True)
