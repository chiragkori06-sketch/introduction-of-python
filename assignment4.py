# 1. Declare variables and print each variable with its type.
followers = 2500
average_rating = 4.7
favorite_app_name = "Instagram"
is_premium_user = True

print("Followers:", followers, "| Type:", type(followers))
print("Average rating:", average_rating, "| Type:", type(average_rating))
print("Favorite app:", favorite_app_name, "| Type:", type(favorite_app_name))
print("Is premium user:", is_premium_user, "| Type:", type(is_premium_user))


# 2. Convert Zomato order price input to float and add 18% GST.
order_price_string = input("\nEnter Zomato order price: ")
order_price = float(order_price_string)
final_bill = order_price + (order_price * 18 / 100)

print("Final bill amount after 18% GST:", final_bill)


# 3. Convert Flipkart product prices to floats and calculate total cart value.
product_prices = ["199.99", "299.50", "150"]
product_prices_float = [float(price) for price in product_prices]
total_cart_value = sum(product_prices_float)

print("\nTotal Flipkart cart value:", total_cart_value)


# 4. Check whether discount is applicable.
def is_discount_applicable(order_amount):
    return order_amount > 500


print("Discount applicable for 450:", is_discount_applicable(450))
print("Discount applicable for 750:", is_discount_applicable(750))


# 5. Convert Spotify ratings to floats and print the highest rating.
spotify_ratings = ["4.5", "3.0", "5", "4.2"]
spotify_ratings_float = [float(rating) for rating in spotify_ratings]
highest_rating = max(spotify_ratings_float)

print("Highest Spotify rating:", highest_rating)