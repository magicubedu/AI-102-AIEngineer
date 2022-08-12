from dotenv import load_dotenv
import os
from PIL import Image, ImageDraw
import sys
from matplotlib import pyplot as plt

# Import namespaces


def main():
    global cv_client

    try:
        # Get Configuration Settings
        load_dotenv()
        cog_endpoint = os.getenv('COG_SERVICE_ENDPOINT')
        cog_key = os.getenv('COG_SERVICE_KEY')

        # Get image
        image_file = 'images/street.jpg'
        if len(sys.argv) > 1:
            image_file = sys.argv[1]

        # Authenticate Computer Vision client


        # Analyze image
        AnalyzeImage(image_file)

        # Generate thumbnail
        GetThumbnail(image_file)

    except Exception as ex:
        print(ex)

def AnalyzeImage(image_file):
    print('Analyzing', image_file)

    # Specify features to be retrieved
    
    
    # Get image analysis


    # Get image description


    # Get image tags
    if (len(analysis.tags) > 0):
        print("Tags: ")
        for tag in analysis.tags:
            print(" -'{}' (confidence: {:.2f}%)".format(tag.name, tag.confidence * 100))


    # Get image categories
    if (len(analysis.categories) > 0):
        print("Categories:")
        landmarks = []
        for category in analysis.categories:
            # Print the category
            print(" -'{}' (confidence: {:.2f}%)".format(category.name, category.score * 100))
            if category.detail:
                # Get landmarks in this category
                if category.detail.landmarks:
                    for landmark in category.detail.landmarks:
                        if landmark not in landmarks:
                            landmarks.append(landmark)

        # If there were landmarks, list them
        if len(landmarks) > 0:
            print("Landmarks:")
            for landmark in landmarks:
                print(" -'{}' (confidence: {:.2f}%)".format(landmark.name, landmark.confidence * 100))


    # Get brands in the image
    if (len(analysis.brands) > 0):
        print("Brands: ")
        for brand in analysis.brands:
            print(" -'{}' (confidence: {:.2f}%)".format(brand.name, brand.confidence * 100))

    # Get objects in the image
    if len(analysis.objects) > 0:
        print("Objects in image:")

        # Prepare image for drawing
        fig = plt.figure(figsize=(8, 8))
        plt.axis('off')
        image = Image.open(image_file)
        draw = ImageDraw.Draw(image)
        color = 'cyan'
        for detected_object in analysis.objects:
            # Print object name
            print(" -{} (confidence: {:.2f}%)".format(detected_object.object_property, detected_object.confidence * 100))
            
            # Draw object bounding box
            r = detected_object.rectangle
            bounding_box = ((r.x, r.y), (r.x + r.w, r.y + r.h))
            draw.rectangle(bounding_box, outline=color, width=3)
            plt.annotate(detected_object.object_property,(r.x, r.y), backgroundcolor=color)
        # Save annotated image
        plt.imshow(image)
        outputfile = 'objects.jpg'
        fig.savefig(outputfile)
        print('  Results saved in', outputfile)

    # Get moderation ratings
    ratings = 'Ratings:\n -Adult: {}\n -Racy: {}\n -Gore: {}'.format(analysis.adult.is_adult_content,
                                                                        analysis.adult.is_racy_content,
                                                                        analysis.adult.is_gory_content)
    print(ratings)
        

def GetThumbnail(image_file):
    print('Generating thumbnail')

    # Generate a thumbnail


if __name__ == "__main__":
    main()
