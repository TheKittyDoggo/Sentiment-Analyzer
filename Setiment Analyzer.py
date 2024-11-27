from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    
    polarity = blob.sentiment.polarity  
    subjectivity = blob.sentiment.subjectivity  
    
    if polarity > 0:
        sentiment = "😊 Positive"
    elif polarity < 0:
        sentiment = "☹️ Negative"
    else:
        sentiment = "😐 Neutral"
    
    return sentiment, polarity, subjectivity

def main():
    print("Welcome to the Sentiment Analyzer! 🙌")
    print("Enter your text below to analyze its sentiment.")
    print("Type 'exit' to quit the program.")
    
    while True:
        print("\n" + "="*50)  
        text = input("\nEnter your text: ")
        
        if text.lower() == 'exit':
            print("\nThank you for using the Sentiment Analyzer! Goodbye! 👋")
            break
        
        sentiment, polarity, subjectivity = analyze_sentiment(text)
        
        print("\nAnalysis Results:")
        print(f"   Sentiment: {sentiment}")
        print(f"   Polarity Score: {polarity:.2f} (scale: -1 to +1)")
        print(f"   Subjectivity Score: {subjectivity:.2f} (scale: 0 to 1)")
        print("="*50)

main()
