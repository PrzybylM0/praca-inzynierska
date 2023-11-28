import openai


# https://learn.deeplearning.ai/chatgpt-prompt-eng/lesson/4/summarizing

def get_chatgpt_response(number, openai_api_key, transcript_sample, chatgpt_model):


    SHORT_SUMMARY =f"""
    Your task is to generate a short summary of a conversation, \
    focusing on the key points and providing a quick overview of the main topics discussed. 

    Summarize the conversation below, delimated by triple \
    backticks, in at most 80 words and capturing the essence of the dialogue.

    Write in polish language.

    Conversation: '''{transcript_sample}'''
    """

    LONG_SUMMARY =f"""
    Your task is to generate a long summary of a conversation, \
    focusing on the key points and providing a quick overview of the main topics discussed. 

    Summarize the conversation below, delimated by triple \
    backticks, in at most 300 words and capturing the essence of the dialogue.

    Write in polish language.

    Conversation: '''{transcript_sample}'''
    """

    TABLE_OF_CONTENTS = f"""
    Your task is to generate a table of contents for a conversation, \
    highlighting the main sections and topics covered. 

    Please create a table of contents for the conversation below, \
    delimited by triple backticks, in at most 200 words, and ensure that 
    it clearly outlines the key topics and moments of the dialogue.

    Write in polish language.

    Conversation: '''{transcript_sample}'''
    """

    SENTIMENT_ANALYSIS = f"""
    Your task is to analyze the sentiment of a conversation, \
    focusing on assessing the emotional tone of the speakers. 

    Please provide a sentiment analysis for the conversation below, \
    delimited by triple backticks. Identify positive, negative, or neutral attitudes exhibited \
    by the speakers throughout the dialogue, in at most 80 words.

    Write in polish language.

    Conversation: '''{transcript_sample}'''
    """

    KEY_WORDS = f"""
    Your task is to generate and list key words and terms discussed during the conversation. 

    Please extract and provide a list of the most important keywords \
    delimited by triple backticks. Focus on highlighting the main concepts. 
    Key words write delimited by commas, in at most 20 words.

    Write in polish language.

    Conversation: '''{transcript_sample}'''
    """

    
    
    if number == '3':
        prompt = SHORT_SUMMARY
    elif number == '4':
        prompt = LONG_SUMMARY
    elif number == '7':
        prompt = TABLE_OF_CONTENTS
    elif number == '6':
        prompt = SENTIMENT_ANALYSIS
    elif number == '5':
        prompt = KEY_WORDS
    else:
        prompt = "There is no conversation here."
        
    openai.api_key = openai_api_key

    response = openai.ChatCompletion.create(
        model=chatgpt_model,
        messages=[{"role": "system", "content": "You are a helpful assistant."}, 
                {"role": "user", "content": prompt}]
    )

    return response.choices[0].message['content']

