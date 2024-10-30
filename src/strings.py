example_question_1 = """
I have forgotten my password and lost my email address. Is there any way I can reset my password for my saving account? I still have my user ID for my XYZ bank account.
"""

question_1_workflow = """
1. User must provide their mobile number, user ID if applicable, and legal name that is associated with the account.
2. Check whether there is an account linked to the information provided.
3. Verify the identity of the user once.
4. Ask user for the new password.
5. Update the user's password.
6. Inform the user that their password has been updated.

If the user is not able to provide sufficient information, please inform the user that you are not able to proceed.
"""

# Simulate a typical conversation with AI
sample_conversation_1 = [
"""
Hi, I forgot my password for my saving account and I was unable to use my email to reset it for some reasons. Is there any alternatives that can help me recover my account?
""",
"""
My mobile number is 347826483, my name is Alex, and my user ID is t830d83jf0.
""",
"""
I would like my new password to be futu39dhj29, appreciate it.
"""]


example_question_2 = """
I would like to order physical checks and receive them as soon as possible. Could you assist with that?
"""

question_2_workflow = """
1. Users must provide their User ID and password for the account that they want to order physical checks from.
2. Verify user's identity once.
3. Ask whether they prefer pick-up or home delivery service.
4. Inform that the fees will be subtracted from their account balance.
5. Help the users to order checks and inform them afterward.

If the user is not able to provide sufficient information, please inform the user that you are not able to proceed.
"""

# Simulate a typical conversation with AI
sample_conversation_2 = [
"""
Hey, I live in a condo in Toronto, and to reserve an elevator for large furniture delivery, I need a physical check. 
Do you know where I can order them?
""",
"""
Yea sure. My password for the account is 5358fbsiHDi3, and my user ID is cgorji83d02. Ideally, I want to get them ASAP, so please order them for me.
""",
"""
I wuold like home delivery please.
"""]