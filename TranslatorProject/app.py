import streamlit as st

st.title("🌍 Language Translation Tool")
st.write("This is my AI Translation App")

# Simple translation dictionary
translations = {
    "Good Morning": "सुप्रभात",
    "Good Night": "शुभ रात्रि",
    "How are you": "आप कैसे हैं",
    "Thank you": "धन्यवाद",
    "Hello": "नमस्ते"
}

text = st.text_area("Enter text to translate")

source_lang = st.selectbox("Select Source Language", ["en", "hi"])
target_lang = st.selectbox("Select Target Language", ["hi", "en"])

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text")
    else:
        if source_lang == "en" and target_lang == "hi":
            translated_text = translations.get(text, "Translation not available")
        elif source_lang == "hi" and target_lang == "en":
            reverse = {v: k for k, v in translations.items()}
            translated_text = reverse.get(text, "Translation not available")
        else:
            translated_text = text

        st.success("Translated Text")
        st.text_area("", translated_text)