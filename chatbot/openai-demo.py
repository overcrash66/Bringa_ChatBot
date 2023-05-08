import openai
#api key ="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"
openai.api_key="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"
openai.ChatCompletion.create(
model ="gpt-3.5-turbo",
message=[
    {"role" : "system", "content" : "you are a helpful assistant."},
    {"role" : "user", "content" : "who won the last presidential election in USA?"},
    ]
)