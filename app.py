import streamlit as st
from spellchecker import SpellChecker

spell = SpellChecker()

st.title("🔍 Instant Spell Correction Engine")

user_input = st.text_input("Type some misspelled word here:")

if user_input:
    words = user_input.split()
    corrected = []

    for word in words:
        fixed = spell.correction(word)
        corrected.append(fixed if fixed is not None else word)

    corrected_text = " ".join(corrected)

    st.markdown("**Corrected:**")
    st.success(corrected_text)
