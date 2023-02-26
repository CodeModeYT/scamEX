#from discordwebhook import Discord
#discord = Discord(url="https://discord.com/api/webhooks/1057656849308078110/9q8eSCeOmImzXCDkieO51AVZg1sMYmkx-qxrK5bCySnTcs0yPWlm6XdSI2yYcXnL9P1I")
#discord.post(content="Hello, world.")
scams = ["scam", "scams"]
legits = ["legti", "legit"]
print('Welcome to the Checker - chek if a Server is listed at scamEX as scam or not!')
print('To begin, enter a Server ID.')
check = input
if check in scams:
    print('Server is marked as scam!')
elif check in legits:
    print('Server is marked as legit!')
else:
    print('Server not registered at scamEX yet!"')