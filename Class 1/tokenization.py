import tiktoken

encoder = tiktoken.encoding_for_model("gpt-4o")

 
print("vocab Size", encoder.n_vocab) #vocab Size 2,00,019


text = "hello i am a coder"  #Tokens [24912, 575, 939, 261, 161238]

tokens = encoder.encode(text)

print("Tokens", tokens)


my_token = [24912, 575, 939, 261, 161238]

decoded = encoder.decode(my_token)

print("Decoded: ",decoded)