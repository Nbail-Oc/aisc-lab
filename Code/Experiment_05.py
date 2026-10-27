# ==============================================================================
# House Price Prediction Model in Indian Rupees (₹)
# Supervised Machine Learning: Simple Linear Regression (Least Squares Method)
# ==============================================================================

# Training Dataset: 
# Input Feature (X): Size of the flat/house in sq. ft.
# Target Label  (y): Price of the flat in Indian Rupees (₹ in Lakhs)
# Note: 1 Lakh = ₹100,000 | 100 Lakhs = ₹1 Crore
X = [550, 650, 800, 1000, 1200, 1500, 1800, 2200]
y_lakhs = [45.0, 52.0, 68.0, 85.0, 105.0, 135.0, 160.0, 195.0]

# Step 1: Compute means (averages) of house sizes and prices
n = len(X)
mean_x = sum(X) / n
mean_y = sum(y_lakhs) / n

# Step 2: Calculate Slope (m) and Intercept (c) using Least Squares Formula
# Line equation: y = m * X + c
numerator = sum((X[i] - mean_x) * (y_lakhs[i] - mean_y) for i in range(n))
denominator = sum((X[i] - mean_x) ** 2 for i in range(n))

m = numerator / denominator
c = mean_y - (m * mean_x)

# Step 3: Define Prediction Function and Currency Formatter
def format_inr(lakhs_amount):
    """Converts amounts in Lakhs to standard INR currency string (₹ Lakhs or ₹ Crores)."""
    rupees = lakhs_amount * 100000
    if lakhs_amount >= 100:
        crores = lakhs_amount / 100
        return f"₹{crores:.2f} Crores (₹{rupees:,.2f})"
    else:
        return f"₹{lakhs_amount:.2f} Lakhs (₹{rupees:,.2f})"

def predict_house_price(sqft_area):
    """Predicts house price given an area in sq. ft."""
    predicted_lakhs = (m * sqft_area) + c
    return predicted_lakhs

# Step 4: Test Model on a Sample House (e.g., 1,350 sq. ft.)
sample_sqft = 1350
predicted_val = predict_house_price(sample_sqft)

# Step 5: Output Results
print("=" * 60)
print("        INDIAN REAL ESTATE HOUSE PRICE PREDICTOR         ")
print("=" * 60)
print(f"Learned Rate per Sq. Ft (Slope 'm') : ₹{m * 100000:.2f} / sq ft")
print(f"Learned Base Price (Intercept 'c')  : ₹{c * 100000:,.2f}")
print("-" * 60)
print(f"Target Area for Prediction          : {sample_sqft:,} sq. ft.")
print(f"Predicted House Price               : {format_inr(predicted_val)}")
print("=" * 60)
