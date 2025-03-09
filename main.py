import streamlit as st
import re

def count_vowels(text):
    return sum(1 for char in text.lower() if char in 'aeiou')

def main():
    st.set_page_config(page_title="Text Analyzer", page_icon="📝")
    
    # Custom CSS for background image and styling
    st.markdown(
        """
        <style>
        body {
            background-image: url('https://source.unsplash.com/1600x900/?abstract,nature');
            background-size: cover;
        }
        .main, .stTextInput, .stTextArea, .stButton {
            background: rgba(255, 255, 255, 0.8);
            padding: 15px;
            border-radius: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.title("✨ Text Analyzer ✨")
    st.markdown("---")
    
    # User Input
    paragraph = st.text_area("📜 Enter a paragraph:", height=150)
    
    if paragraph:
        words = paragraph.split()
        total_words = len(words)
        total_characters = len(paragraph)
        vowels_count = count_vowels(paragraph)
        contains_python = "✅ Yes" if "Python" in paragraph else "❌ No"
        
        search_word = st.text_input("🔍 Enter a word to search for:")
        replace_word = st.text_input("✍️ Enter a word to replace it with:")
        modified_paragraph = paragraph.replace(search_word, replace_word) if search_word else paragraph
        
        uppercase_text = paragraph.upper()
        lowercase_text = paragraph.lower()
        avg_word_length = round(total_characters / total_words, 2) if total_words > 0 else 0
        
        # Display Results
        st.subheader("📊 Analysis Results")
        st.markdown(f"**📝 Total Words:** {total_words}")
        st.markdown(f"**🔢 Total Characters:** {total_characters}")
        st.markdown(f"**🔡 Number of Vowels:** {vowels_count}")
        st.markdown(f'**🐍 Contains "Python"?** {contains_python}')
        
        if search_word:
            st.subheader("✏️ Modified Paragraph:")
            st.write(modified_paragraph)
        
        st.subheader("🔠 Paragraph in Uppercase:")
        st.write(uppercase_text)
        
        st.subheader("🔡 Paragraph in Lowercase:")
        st.write(lowercase_text)
        
        st.subheader("📏 Average Word Length:")
        st.markdown(f"**{avg_word_length}**")
    else:
        st.warning("⚠️ Please enter a paragraph to analyze.")

if __name__ == "__main__":
    main()

