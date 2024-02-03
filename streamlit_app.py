import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers


def getllamaresponse(input_text, blog_style, no_words):
    llm=CTransformers(model="X:/llama-7b", 
                      model_type="llama", config={"temperature":0.01})
    
    template=""" Write a blog for {blog_style} job profile for {input_text} in {no_words} words """

    prompt=PromptTemplate(input_variables=["blog_style", "input_text", "no_words"], template=template) 

    #generating response
    response=llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    print(response)
    return response





st.set_page_config(page_title="Generate Blogs",
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Blogs ")

input_text=st.text_input("Enter the Blog Topic")

## creating two more columns for additonal 2 fields

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('No of Words')
with col2:
    blog_style=st.selectbox('Writing the blog for',
                            ('Researchers','Data Scientist','Developer','Content Creation','Common People'),index=0)
    
submit=st.button("Generate")

if submit:
    st.write(getllamaresponse(input_text, blog_style, no_words))
