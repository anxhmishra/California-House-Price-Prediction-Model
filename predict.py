import joblib

model = joblib.load("model/house_price_model.pkl")

sample = [[8.32,41,6.98,1.02,322,2.55,37.88,-122.23]]

prediction = model.predict(sample)

print(prediction)