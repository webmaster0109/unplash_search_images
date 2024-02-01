import streamlit as st
import requests
import io
from PIL import Image

# Your Unsplash API key
UNSPLASH_ACCESS_KEY = "cR3xV4ZICrFDNXWeOsIwDpVlA3Rx65pjYz9-cZj0ea8"

def search_images(query, count=100):
    url = "https://api.unsplash.com/search/photos"
    headers = {"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"}
    params = {"query": query, "per_page": count}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data["results"]

def download_image(image_url):
    response = requests.get(image_url)
    img = Image.open(io.BytesIO(response.content))
    return img

def main():
    st.markdown("# :rainbow[Millions of Images Search Engine]")

    # Input for user to enter search query
    query = st.text_input("Enter your search query:", "trendings")

    if st.button("Search"):
        # Fetch images from Unsplash API
        images = search_images(query, count=100)
        st.write(f"## Title: {query}")
        total_results = len(images)
        st.write(f"Total Images Searched: {total_results}")

        col1, col2, col3 = st.columns(3)

        for i, image in enumerate(images):
            if i % 3 == 0:
                col = col1
            elif i % 3 == 1:
                col = col2
            else:
                col = col3

            # Display image with a download button
            with col:
                st.image(image["urls"]["regular"])


        # Display images
        # for image in images:
        #     st.image(image["urls"]["regular"], caption=image["description"])

if __name__ == "__main__":
    main()
