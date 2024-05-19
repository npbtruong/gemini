import google.generativeai as genai

genai.configure(api_key="")

def upload_to_gemini(path, mime_type=None):
  
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash-latest"
)

# TODO Make these files available on the local file system
# You may need to update the file paths
image_drive0 = upload_to_gemini("RCO007_1653405184_0.png", mime_type="image/png")

chat_session = model.start_chat(
  history=[]
)
prompts = [
        "detect text in the comic image format in json",
        image_drive0,
      ]
response = chat_session.send_message(prompts)

print(response.text)
