from ai_engine import predict_message

message = input("Enter message: ")

result = predict_message(message)

print("Prediction:", result)