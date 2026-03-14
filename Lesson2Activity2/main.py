import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN} Welcome to Sentiment Spy! {Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}")
if not user_name:
    user_name = "Mystery Agent"

conversation_his = []

print(f"\n{Fore.CYAN}Hello, Agent {user_name}")
print(f"Type a sentence and I will analyze your sentencec with TextBlob and show you the sentiment.")
print(f"Type {Fore.YELLOW}reset{Fore.CYAN}, {Fore.YELLOW}history{Fore.CYAN}", f"or {Fore.YELLOW}exit{Fore.CYAN} to quit.{Style.RESET_ALL}")

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue

    if user_input.lower() == "exit":
        print(f"\n{Fore.BLUE} Exiting Sentiment Spy. Farewell, Agent {user_name}! {Style.RESET_ALL}")
        break

    elif user_input.lower() == "reset":
        conversation_his.clear()
        print(f"{Fore.CYAN} All conversations history cleared!{Style.RESET_ALL}")
        continue
    elif user_input.lower() == "history":
        if not conversation_his:
            print(f"{Fore.YELLOW}No converstaion history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN} Conversation History:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_his, start=1):
                if sentiment_type == "Positive":
                    colour = Fore.GREEN
                    emoji = " "
                elif sentiment_type == "Negative":
                    colour = Fore.RED
                    emoji = " "
                else:
                    colour = Fore.YELLOW
                    emoji = " "

                print(f"{idx}. {colour}{emoji} {text}" f"Polarity: {polarity:.2f}, {sentiment_type}{Style.RESET_ALL}")
        
        continue

    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
        colour = Fore.GREEN
        emoji = " "
    elif polarity > -0.25:
        sentiment_type = "Negative"
        colour = Fore.RED
        emoji = " "
    else: 
        sentiment_type = "Neutral"
        colour = Fore.YELLOW
        emoji = " "
    
    conversation_his.append((user_input, polarity, sentiment_type))
    
    print(f"{colour}{emoji} {sentiment_type} sentiment detected! " f"Polarity: {polarity:.2f}")




