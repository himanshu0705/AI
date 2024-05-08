import streamlit as st

bot_name = "College Buddy"
knowledge_base = {
    "what is your name?": [
        f"My name is {bot_name}! \n Happy to help you out with your college enquiry"
    ],

    "hello" : [
        f"Hello! my name is {bot_name}! \n Happy to help you out with your college enquiry"
    ],

    "which are the best engineering colleges in pune?" : [
        "COEP",
        "PICT",
        "VIT",
        "IIIT",
        "I2IT"
    ],

    "what are the best engineering branches?" : [
        "Computer Engineering",
        "IT Engineering",
        "ENTC Engineering"
    ],

    "what are the top branches cut-off for coep?" : [
        "Computer Engineering : 99.8 percentile",
        "Does not have IT Branch",
        "ENTC Engineering : 99.2 precentile"
    ],

    "what are the top branches cut-off for pict?" : [
        "Computer Engineering : 99.4 percentile",
        "IT Engineering : 98.6 percentile",
        "ENTC Engineering : 97.2 precentile"
    ],

    "what are the top branches cut-off for vit?" : [
        "Computer Engineering : 99.8 percentile",
        "IT Engineering : 97.1 percentile",
        "ENTC Engineering : 96.4 precentile"
    ],

    "what are the top branches cut-off for iiit?" : [
        "Computer Engineering : 98.4 percentile",
        "IT Engineering : 97.3 percentile",
        "ENTC Engineering : 96.6 precentile"
    ],

    "what are the top branches cut-off for i2it?" : [
        "Computer Engineering : 96.4 percentile",
        "IT Engineering : 94.3 percentile",
        "ENTC Engineering : 92.8 precentile"
    ],

    "when does the admission procedure starts?" : [
        "The admission procedure usually starts around August"
    ]
}

st.header("College Enquiry Rule Based Chatbot")

def respond(input :str):
    if(input in knowledge_base):
        print(input)
        values = knowledge_base[input]
        for value in values:
            st.write(value)
    
    else:
        key = input
        st.write("Question is not present! \nCound you please enter the appropriate answer for the question")
        answer = st.text_input("Answer")
        add = st.button("Add")
        if (add):
            knowledge_base[key] = [answer]

if __name__== "__main__":
    input = st.text_input("Enter a query")
    input = input.lower()
    col1,col2 = st.columns([1,0.1])
    with col1:
        ask = st.button("Ask")
    with col2:
        quit = st.button("Quit")
    if (ask):
        respond(input)
    if (quit):
        st.write("Thankyou for using the chatbot")