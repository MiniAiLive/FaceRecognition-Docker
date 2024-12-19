import requests

# URL of the web API endpoint
url = 'http://127.0.0.1:8083/api/face_match'

# Path to the image file you want to send
image_path_1 = './test_image/img1.jpg'
image_path_2 = './test_image/img2.jpg'

# Read the image file and send it as form data
files = {
    'image1': open(image_path_1, 'rb'),
    'image2': open(image_path_2, 'rb')
    }

try:
    # Send POST request
    response = requests.post(url, files=files)

    # Check if the request was successful
    if response.status_code == 200:
        print('Request was successful!')
        # Parse the JSON response
        response_data = response.json()
        print('Response Data:', response_data)
    else:
        print('Request failed with status code:', response.status_code)
        print('Response content:', response.text)

except requests.exceptions.RequestException as e:
    print('An error occurred:', e)