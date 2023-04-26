import email


msg = email.message_from_string(message.body)
encryption_header = msg.get("Encryption")

if encryption_header and encryption_header.lower() in ["1", "true"]:
    print("encrypted")
else:
    print("not encrypted.")