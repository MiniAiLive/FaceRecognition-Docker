<div align="center">
   <h1>Face Recognition Windows SDK</h1>
   <img src=https://miniai.live/wp-content/uploads/2024/02/logo_name-1-768x426-1.png alt="MiniAiLive Logo"
   width="300">
</div>

## Welcome to the [MiniAiLive](https://www.miniai.live/)!
Check the likelihood that two faces belong to the same person. You will get a confidence score and thresholds to evaluate the similarity. Feel free to use our MiniAI Face Recognition Windows SDK.

> **Note**
>
> SDK is fully on-premise, processing all happens on hosting server and no data leaves server.

## Table of Contents

- [Installation Guide](#installation-guide)
- [API Details](#api-details)
- [Gradio Demo](#gradio-demo)
- [Python Test API Example](#python-test-api-example)

## FaceSDK Installation Guide

### Prerequisites

- Python 3.6+
- Windows
- CPU: 2cores or more
- RAM: 4GB or more

### Installation Steps

1. **Download the Face Recognition Windows Server Installer:**

   Download the Server installer for your operating system from the following link:
   
   [Download the On-premise Server Installer](https://drive.google.com/file/d/1cNaJETo2liaAn0ijXqM45B6sNEhbNj6L/view?usp=sharing)

2. **Install the On-premise Server:**

   Run the installer and follow the on-screen instructions to complete the installation.
   <div align="center">
      <img src="https://github.com/user-attachments/assets/3438fa1c-f869-4ac0-85fc-762716da09bc" width="450" />
   </div>

3. **Request License and Update:**

   Run MIRequest.exe file to generate a license request file. You can find it here.
   
   > C:\Program Files\MiniAiLive\MiniAiLive-FaceSDK-WinServer

   Open it, generate a license request file, and send it to us via email or WhatsApp. We will send the license based on your Unique Request file, then you can upload the license file to allow to use. Refer the below images.
   <div align="center">
      <img src="https://github.com/user-attachments/assets/d54686be-c7d8-42ba-8c57-f62fe1ec81e3" width="300" />
      <img src="https://github.com/user-attachments/assets/e33757a7-7fb1-411e-8136-129800198773" width="300" />
      <img src="https://github.com/user-attachments/assets/f34cdb2d-2b4e-48ec-b303-fd38cf128336" width="300" />
      <img src="https://github.com/user-attachments/assets/b1579722-462c-478a-9106-67b9a10b3514" width="300" />
   </div>

4. **Verify Installation:**

   After installation, verify that the On-premise Server is correctly installed by checking the task manager:
   <div align="center">
      <img src="https://github.com/user-attachments/assets/98e87782-073d-475c-962f-37151ef9754f" width="450" />
   </div>

## FaceSDK API Details

### Endpoint

- `POST http://127.0.0.1:8083/api/face_detect` Face Detection, Face Attributes API
- `POST http://127.0.0.1:8083/api/face_detect_base64` Face Detection, Face Attributes API
  
- `POST http://127.0.0.1:8083/api/face_match` Face Matching API
- `POST http://127.0.0.1:8083/api/face_match_base64` Face Matching API

### Request

- **URL:** `http://127.0.0.1:8083/api/face_detect`
- **Method:** `POST`
- **Form Data:**
  - `image`: The image file (PNG, JPG, etc.) to be analyzed. This should be provided as a file upload.
<img width="1049" alt="Screenshot 2024-07-16 at 5 12 01 AM" src="https://github.com/user-attachments/assets/e05be690-f474-4ad5-b800-ea64ee763461">

- **URL:** `http://127.0.0.1:8083/api/face_detect_base64`
- **Method:** `POST`
- **Raw Data:**
  - `JSON Format`:
    {
       "image": "--base64 image data here--"
    }
<img width="1049" alt="Screenshot 2024-07-16 at 5 11 34 AM" src="https://github.com/user-attachments/assets/70c50c55-3c39-4885-ab9f-8e0c34e525f0">

### Response

The API returns a JSON object with the recognized details from the input Face image. Here is an example response:
   <div align="center">
      <img src="https://github.com/user-attachments/assets/e05be690-f474-4ad5-b800-ea64ee763461" />
   </div>

## Gradio Demo

We have included a Gradio demo to showcase the capabilities of our Face Recognition SDK. Gradio is a Python library that allows you to quickly create user interfaces for machine learning models.

### How to Run the Gradio Demo

1. **Install Gradio:**

   First, you need to install Gradio. You can do this using pip:

   ```sh
   git clone https://github.com/MiniAiLive/FaceRecognition-Windows.git
   pip install -r requirement.txt
   cd gradio
   ```
2. **Run Gradio Demo:**
   ```sh
   python app.py
   ```
## Python Test API Example

To help you get started with using the API, here is a comprehensive example of how to interact with the Face Recognition API using Python. You can use API with another language you want to use like C++, C#, Ruby, Java, Javascript, and more

### Prerequisites

- Python 3.6+
- `requests` library (you can install it using `pip install requests`)

### Example Script

This example demonstrates how to send an image file to the API endpoint and process the response.

```python
import requests

# URL of the web API endpoint
url = 'http://127.0.0.1:8083/api/face_detect'

# Path to the image file you want to send
image_path = './test_image.jpg'

# Read the image file and send it as form data
files = {'image': open(image_path, 'rb')}

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
```


## Request license
Feel free to [Contact US](https://www.miniai.live/contact/)  to get a trial License. We are 24/7 online on WhatsApp: [+19162702374](https://wa.me/+19162702374).

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
```java 
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the original repository.
```

## Face & IDSDK Online Demo, Resources
<div style="display: flex; justify-content: center; align-items: center;"> 
   <table style="text-align: center;">
      <tr>
         <td style="text-align: center; vertical-align: middle;"><a href="https://github.com/MiniAiLive"><img src="https://miniai.live/wp-content/uploads/2024/10/new_git-1-300x67.png" style="height: 60px; margin-right: 5px;" title="GITHUB"/></a></td> 
         <td style="text-align: center; vertical-align: middle;"><a href="https://huggingface.co/MiniAiLive"><img src="https://miniai.live/wp-content/uploads/2024/10/new_hugging-1-300x67.png" style="height: 60px; margin-right: 5px;" title="HuggingFace"/></a></td> 
         <td style="text-align: center; vertical-align: middle;"><a href="https://demo.miniai.live"><img src="https://miniai.live/wp-content/uploads/2024/10/new_gradio-300x67.png" style="height: 60px; margin-right: 5px;" title="Gradio"/></a></td> 
      </tr> 
      <tr>
         <td style="text-align: center; vertical-align: middle;"><a href="https://docs.miniai.live/"><img src="https://miniai.live/wp-content/uploads/2024/10/a-300x70.png" style="height: 60px; margin-right: 5px;" title="Documentation"/></a></td> 
         <td style="text-align: center; vertical-align: middle;"><a href="https://www.youtube.com/@miniailive"><img src="https://miniai.live/wp-content/uploads/2024/10/Untitled-1-300x70.png" style="height: 60px; margin-right: 5px;" title="Youtube"/></a></td> 
         <td style="text-align: center; vertical-align: middle;"><a href="https://play.google.com/store/apps/dev?id=5831076207730531667"><img src="https://miniai.live/wp-content/uploads/2024/10/googleplay-300x62.png" style="height: 60px; margin-right: 5px;" title="Google Play"/></a></td>
      </tr>
   </table>
</div>

## Our Products
No | Project | Feature
---|---|---|
1 | [FaceRecognition-Android](https://github.com/MiniAiLive/FaceRecognition-Android) | 1:N Face Matching, 3D Face Passive LivenessDetection
2 | [FaceRecognition-LivenessDetection-Windows](https://github.com/MiniAiLive/FaceRecognition-LivenessDetection-Windows) | 1:N Face Matching, 3D Face Passive LivenessDetection
3 | [FaceLivenessDetection-Android](https://github.com/MiniAiLive/FaceLivenessDetection-Android) | 2D & 3D Face Passive LivenessDetection
4 | [FaceLivenessDetection-Linux](https://github.com/MiniAiLive/FaceLivenessDetection-Linux) | 2D & 3D Face Passive LivenessDetection
5 | [FaceLivenessDetection-Windows](https://github.com/MiniAiLive/FaceLivenessDetection-Windows) | 2D & 3D Face Passive LivenessDetection
6 | [FaceMatching-Android](https://github.com/MiniAiLive/FaceMatching-Android) | 1:1 Face Matching
7 | [FaceMatching-Windows](https://github.com/MiniAiLive/FaceMatching-Windows) | 1:1 Face Matching
8 | [FaceAttributes-Android](https://github.com/MiniAiLive/FaceAttributes-Android) | Face Attributes, Age & Gender Estimation
9 | [ID-DocumentRecognition-Android](https://github.com/MiniAiLive/ID-DocumentRecognition-Android) | IDCard, Passport, Driver License, Credit, MRZ Recognition
10 | [ID-DocumentRecognition-Linux](https://github.com/MiniAiLive/ID-DocumentRecognition-Linux) | IDCard, Passport, Driver License, Credit, MRZ Recognition
11 | [ID-DocumentRecognition-Windows](https://github.com/MiniAiLive/ID-DocumentRecognition-Windows) | IDCard, Passport, Driver License, Credit, MRZ Recognition
12 | [ID-DocumentLivenessDetection-Linux](https://github.com/MiniAiLive/ID-DocumentLivenessDetection-Linux) | ID Document LivenessDetection
13 | [ID-DocumentLivenessDetection-Windows](https://github.com/MiniAiLive/ID-DocumentLivenessDetection-Windows) | ID Document LivenessDetection

## About MiniAiLive
[MiniAiLive](https://www.miniai.live/) is a leading AI solutions company specializing in computer vision and machine learning technologies. We provide cutting-edge solutions for various industries, leveraging the power of AI to drive innovation and efficiency.

## Contact US
For any inquiries or questions, please [Contact US](https://www.miniai.live/contact/)

<p align="center">
<a target="_blank" href="https://t.me/Contact_MiniAiLive"><img src="https://img.shields.io/badge/telegram-@MiniAiLive-blue.svg?logo=telegram" alt="www.miniai.live"></a>&emsp;
<a target="_blank" href="https://wa.me/+19162702374"><img src="https://img.shields.io/badge/whatsapp-MiniAiLive-blue.svg?logo=whatsapp" alt="www.miniai.live"></a>&emsp;
<a target="_blank" href="https://join.skype.com/invite/ltQEVDmVddTe"><img src="https://img.shields.io/badge/skype-MiniAiLive-blue.svg?logo=skype" alt="www.miniai.live"></a>&emsp;
</p>
