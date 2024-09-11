from src.chatbot import run_conversation

# Demonstration Example 1: Password reset conversation
def demonstration_example_1(final_graph):
    messages = [
        "Hi, I forgot my password, and I'm unable to use my email to reset it. Is there any alternative that can help me recover my account?",

        "Yeah, sure. My mobile number is 347826483, my name is Alex, and my user ID is t830d83jf0.",
        "I would like my new password to be futu39dhj29."
    ]
    run_conversation(messages, final_graph)


# Demonstration Example 2: Physical check ordering conversation
def demonstration_example_2(final_graph):
    messages = [
        "Hey, I live in a condo in Toronto, and to reserve an elevator for large furniture, I need a physical check. Do you know where I can order the checks?",
        "Yeah, sure. My password for the account is 5358fbsiIHDi3, and my user ID is cgorji83d02. I need them ASAP, so please order them for me.",
        "I would like home delivery, please."
    ]
    run_conversation(messages, final_graph)