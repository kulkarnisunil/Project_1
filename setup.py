from setuptools import find_packages, setup

setup(
    name="Ecommercebot",
    version="0.0.2",
    author="kulkarnisunil",
    author_email="sunilkulkarni603@gmail.com",
    packages=find_packages(),
    install_requires=['torch','transformers','accelerate','bitsandbytes','sentence-transformers','unstructured[all-docs]', 
                      'langchain', 'chromadb', 'langchain_community', 'langchain-astradb', 'langchain-google-genai', 
                      'google-generativeai' ,'datasets','pypdf','python-dotenv', 'flask']
)