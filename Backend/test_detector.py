from scam_detector import detect_scam

message = input("Enter message: ")

result = detect_scam(message)

print(result)