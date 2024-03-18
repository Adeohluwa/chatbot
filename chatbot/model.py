from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from .data import faq_data, bursary_data, registry_data, courses_data, exam_schedule_data, school_fees_data, new_data
# from .new import new_data


api_key = "OKFTByB8mjGauHqbZBovA77a6unUJJZN"
model = "mistral-tiny-2312"
# model = "none"


client = MistralClient(api_key=api_key)



# for llm function calling

# tools = [
#      {
#         "type": "function",
#         "function": {
#             "name": "contact_staff",
#             "description": "Reach out to an administrative staff",
#             "parameters": {
#                 "type": "object",
#                 "properties": {
#                     # "transaction_id": {
#                     #     "type": "string",
#                     #     "description": "The transaction id.",
#                     }
#                 },
#                 # "required": ["transaction_id"],
#             },
#         },
#     # }
# ]




def handle_query(prompt):
 messages = [
     ChatMessage(role="user", content=f"""
      you always obey

      Context:You have being hired as Babcock University's customer support "personel" 
      you shall answer question(s) accurately below using only these {faq_data}, {bursary_data}, {registry_data},{courses_data}, {exam_schedule_data}, {school_fees_data},{new_data}  as your source of truth, 
      if the answer does not exist within the provided sources, you correctly say you dont have that information and direct them to your university’s website here https://www.babcock.edu.ng/

      you are a friendly, professional and smart person and you shall reply in simple english language, no coding.

      Examples
      Sorry, I'm not aware we offer that service at the moment
      Sorry, I currently i don't have answer to that. I would recommend checking the university's official website (<https://www.babcock.edu.ng/>) or contacting the university's transportation department directly for the most accurate and up-to-date information.

      Serve data from {exam_schedule_data}, {school_fees_data} as a well formatted and detailed table of information, remember you are communicating with a non technical end user 

      do not make up any information not inside of these sources {faq_data}, {bursary_data}, {registry_data}, {courses_data}, {exam_schedule_data}, {school_fees_data}, {new_data}
      also when you dont have answer. let the user know in a brief manner, do not launch in to long wordy texts.
      {prompt}
      """)
 ]

 # No streaming
 response = client.chat(
     model=model,
     messages=messages
 )

 # return response
 return response.choices[0].message.content
 


# DEBUG
# result = handle_query("I want to reach a staff")
# print(result)
# if the user wants to contact an administrative staff, signal with the word "DM"
