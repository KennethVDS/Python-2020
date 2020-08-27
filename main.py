username = input ('What is your name?')
password = input('What is your password?')

password_length = len(password)
hidden_password = '*' * password_length

print(f'{username}, you sexy motherfucker. Your password, {hidden_password}, is {password_length} letters long')

