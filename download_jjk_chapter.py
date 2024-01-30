#!/usr/bin/env python
# coding: utf-8

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import argparse
from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image



def download_images(download_directory: str, chapter: int) -> None:
    """
    Download images from a website, excluding those with specified keywords.

    Parameters:
    - chapter (int): Chapter to download.
    - download_directory (Path): Directory to download images.

    Returns:
    - int: Number of images downloaded.
    """
    url = f"https://w2.jujmanga.com/manga/jujutsu-kaisen-chapter-{chapter}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    img_tags = soup.find_all('img')
    img_urls = [urljoin(url, img['src']) for img in img_tags]


    if not os.path.exists(download_directory):
        os.makedirs(download_directory)

    # Initialize a counter for renaming images
    counter = 1

    for img_url in img_urls:
        img_data = requests.get(img_url).content
        img_filename = f"{counter}.jpg"  # You can change the file extension if needed
        with open(os.path.join(download_directory, img_filename), 'wb') as f:
            f.write(img_data)
        counter += 1

    return counter

def create_pdf(download_directory: Path, image_count:int) -> None:
    """
    Create a PDF from downloaded images.

    Parameters:
    - download_directory (Path): Directory where images are downloaded.
    - image_count (int): Number of images downloaded.
    """
    
    # Create a PDF with all images
    pdf_filename = f"{os.path.basename(download_directory)}.pdf"
    pdf_path = os.path.join(download_directory, pdf_filename)

    # Open a PDF file
    with open(pdf_path, 'wb') as pdf_file:
        # Create a PDF canvas
        pdf_canvas = canvas.Canvas(pdf_file, pagesize=letter)

        # Iterate over images and add them to the PDF
        for img_num in range(1, image_count):
            img_path = os.path.join(download_directory, f"{img_num}.jpg")
            img = Image.open(img_path)
            pdf_canvas.drawInlineImage(img, 0, 0, width=letter[0], height=letter[1])

            # Add a new page for each image (optional)
            pdf_canvas.showPage()

        # Save the PDF
        pdf_canvas.save()

    print(f"PDF created: {pdf_path}")



def delete_images(download_directory:Path) -> None:
    """
    Delete downloaded images.

    Parameters:
    - download_directory (Path): Directory where images are downloaded.
    """
    for file_name in os.listdir(download_directory):
        if file_name.endswith(".jpg"):
            file_path = os.path.join(download_directory, file_name)
            os.remove(file_path)

    print(f"All images removed from {download_directory}.")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Download Jujutsu Kaisen Manga from URL to PDF.')
    parser.add_argument('chapter', type=str, help='The chapter you want to download.')
    parser.add_argument('output_dir', type=str, help='Path to save the generated PDF.')
    #parser.add_argument('url', type=str, help='URL of the website.')

    args = parser.parse_args()

    chapter = args.chapter
    output_dir = args.output_dir

    download_directory = f"{output_dir}chapter_{chapter}"

    image_count = download_images(download_directory, chapter)
    create_pdf(download_directory, image_count) 
    delete_images(download_directory)






