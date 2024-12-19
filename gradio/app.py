import gradio as gr
import os
import requests
import json
from PIL import Image

import requests
import base64
from PIL import Image
from io import BytesIO

def face_detect(frame):
    url = "http://127.0.0.1:8083/api/face_detect"
    files = {'image': open(frame, 'rb')}
    r = requests.post(url=url, files=files)
    response = r.json()

    detections = response.get("detections", {})
    table_rows = ""
    face_images = []

    for face_id, details in detections.items():
        attributes = details.get("attributes", {})
        # landmarks = details.get("landmarks", [])
        # position = details.get("position", [])
        face_base64 = details.get("face", "")

        # Decode face image
        face_image = f"<img src='data:image/png;base64,{face_base64}' width='100' />" if face_base64 else "N/A"

        # Prepare attributes text without specific keys
        keys_to_remove = {"Emotion", "ForeheadCovering", "HeadCovering", "Occlusion", "StrongMakeup"}
        filtered_attributes = {key: value for key, value in attributes.items() if key not in keys_to_remove}

        attributes_text = "<br>".join(f"{key}: {value}" for key, value in filtered_attributes.items())

        # # Prepare landmarks text
        # landmarks_text = ", ".join(str(landmark) for landmark in landmarks)

        # Add table row for the face
        table_rows += f"""
        <tr>
            <td>{face_id}</td>
            <td>{face_image}</td>
            <td>{attributes_text}</td>
        </tr>
        """

    # Create final HTML table
    html = f"""
    <table border="1" style="border-collapse: collapse; width: 100%;">
        <tr>
            <th>Face ID</th>
            <th>Face Image</th>
            <th>Attributes</th>
        </tr>
        {table_rows}
    </table>
    """
    return html

def face_match(frame1, frame2):
    url = "http://127.0.0.1:8083/api/face_match"
    files = {'image1': open(frame1, 'rb'), 'image2': open(frame2, 'rb')}
    r = requests.post(url=url, files=files)
    response = r.json()

    detections = response.get("detections", [])
    matches = response.get("match", [])
    detection_rows = ""
    match_rows = ""

    # Process detections
    for detection in detections:
        face_image = detection.get("face", "")
        face_img_tag = f"<img src='data:image/png;base64,{face_image}' width='100' />" if face_image else "N/A"
        first_face_index = detection.get("firstFaceIndex", "N/A")
        second_face_index = detection.get("secondFaceIndex", "N/A")

        detection_rows += f"""
        <tr>
            <td>{first_face_index}</td>
            <td>{second_face_index}</td>
            <td>{face_img_tag}</td>
        </tr>
        """

    # Process matches
    for match in matches:
        first_face_index = match.get("firstFaceIndex", "N/A")
        second_face_index = match.get("secondFaceIndex", "N/A")
        similarity = match.get("similarity", "N/A")

        match_rows += f"""
        <tr>
            <td>{first_face_index}</td>
            <td>{second_face_index}</td>
            <td>{similarity:.6f}</td>
        </tr>
        """

    # Create HTML tables
    detections_table = f"""
    <h3>Face Detection</h3>
    <table border="1" style="border-collapse: collapse; width: 100%;">
        <tr>
            <th>First Face Index</th>
            <th>Second Face Index</th>
            <th>Face Image</th>
        </tr>
        {detection_rows}
    </table>
    """

    matches_table = f"""
    <h3>Matching Results</h3>
    <table border="1" style="border-collapse: collapse; width: 100%;">
        <tr>
            <th>First Face Index</th>
            <th>Second Face Index</th>
            <th>Similarity</th>
        </tr>
        {match_rows}
    </table>
    """

    return detections_table + matches_table

# APP Interface
with gr.Blocks() as MiniAIdemo:
    gr.Markdown(
        """
        <a href="https://miniai.live" style="display: flex; align-items: center;">
            <img src="https://miniai.live/wp-content/uploads/2024/02/logo_name-1-768x426-1.png" style="width: 18%; margin-right: 15px;"/>
            <div>
                <p style="font-size: 40px; font-weight: bold; margin-right: 20px;">FaceRecognition SDK Demo</p>
                <p style="font-size: 20px; margin-right: 0;">Experience our NIST FRVT Top Ranked FaceRecognition, iBeta 2 Certified Face Liveness Detection Engine</p>
            </div>
        </a>
        <br/>
        <div style="display: flex; justify-content: center; align-items: center;"> 
           <table style="text-align: center;">
              <tr>
                 <td style="text-align: center; vertical-align: middle;"><a href="https://github.com/MiniAiLive"><img src="https://miniai.live/wp-content/uploads/2024/10/new_git-1-300x67.png" style="height: 50px; margin-right: 5px;" title="GITHUB"/></a></td> 
                 <td style="text-align: center; vertical-align: middle;"><a href="https://huggingface.co/MiniAiLive"><img src="https://miniai.live/wp-content/uploads/2024/10/new_hugging-1-300x67.png" style="height: 50px; margin-right: 5px;" title="HuggingFace"/></a></td> 
                 <td style="text-align: center; vertical-align: middle;"><a href="https://demo.miniai.live"><img src="https://miniai.live/wp-content/uploads/2024/10/new_gradio-300x67.png" style="height: 50px; margin-right: 5px;" title="Gradio"/></a></td> 
              </tr> 
              <tr>
                 <td style="text-align: center; vertical-align: middle;"><a href="https://docs.miniai.live/"><img src="https://miniai.live/wp-content/uploads/2024/10/a-300x70.png" style="height: 50px; margin-right: 5px;" title="Documentation"/></a></td> 
                 <td style="text-align: center; vertical-align: middle;"><a href="https://www.youtube.com/@miniailive"><img src="https://miniai.live/wp-content/uploads/2024/10/Untitled-1-300x70.png" style="height: 50px; margin-right: 5px;" title="Youtube"/></a></td> 
                 <td style="text-align: center; vertical-align: middle;"><a href="https://play.google.com/store/apps/dev?id=5831076207730531667"><img src="https://miniai.live/wp-content/uploads/2024/10/googleplay-300x62.png" style="height: 50px; margin-right: 5px;" title="Google Play"/></a></td>
              </tr>
           </table>
        </div>
        <br/>
        """
    )
    with gr.Tabs():
        with gr.TabItem("Face Detection"):
            with gr.Row():
                with gr.Column():
                    im_detect_input = gr.Image(type='filepath', height=300)
                    gr.Examples(
                        [
                            os.path.join(os.path.dirname(__file__), "images/img1.jpg"),
                            os.path.join(os.path.dirname(__file__), "images/img2.jpg"),
                            os.path.join(os.path.dirname(__file__), "images/img3.jpg"),
                        ],
                        inputs=im_detect_input
                    )
                    btn_f_detect = gr.Button("Detect", variant='primary')
                with gr.Column():
                    txt_detect_output = gr.HTML()
            btn_f_detect.click(face_detect, inputs=im_detect_input, outputs=txt_detect_output)
        with gr.Tab("Face Recognition"):
            with gr.Row():
                with gr.Column():
                    im_match_in1 = gr.Image(type='filepath', height=300)
                    gr.Examples(
                        [
                            "images/img2.jpg",
                            "images/img3.jpg",
                            "images/img4.jpg",
                        ],
                        inputs=im_match_in1
                    )
                with gr.Column():
                    im_match_in2 = gr.Image(type='filepath', height=300)
                    gr.Examples(
                        [
                            "images/img5.jpg",
                            "images/img6.jpg",
                            "images/img7.jpg",
                        ],
                        inputs=im_match_in2
                    )
                with gr.Column():
                    txt_match_out = gr.HTML()
            btn_f_match = gr.Button("Check Comparing!", variant='primary')
            btn_f_match.click(face_match, inputs=[im_match_in1, im_match_in2], outputs=txt_match_out)
                
if __name__ == "__main__":
    MiniAIdemo.launch(server_port=8085, server_name="0.0.0.0")