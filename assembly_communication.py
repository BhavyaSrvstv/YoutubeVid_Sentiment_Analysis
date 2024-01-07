#this file will  five not only the transcription but also the sentiment analysis of the audio
#here we used the iphone 13 review youtube video and extracted the audio url {refer the file : yt_extracror.py} and then downloaded the m4a file and converted it into mp3
#then uploaded the audio mp3 file here in this file 
import requests
from api_key import ASSEMBLY_API_KEY
import json


base_url="https://api.assemblyai.com/v2"
headers = {
    "authorization": ASSEMBLY_API_KEY 
}
filename="C:/Users/bhavy/Desktop/Speech Recognition/Youtube_Sentiment/videoplayback.mp3"


#upload
def upload(filename):
  with open(filename,"rb") as f:
    response=requests.post(base_url+"/upload",
                       headers=headers,
                       data=f)

    upload_url=response.json()["upload_url"]
    return upload_url
  

#transcribe
def transcribe(filename,sentiment_analysis):
  data = {
    "audio_url": upload(filename),
    "sentiment_analysis":sentiment_analysis
  }
  url= base_url+"/transcript"
  response=requests.post(url,json=data,headers=headers)
  job_id=response.json()['id']
  return job_id

#poll
def poll(filename,sentiment_analysis):
   j_id=transcribe(filename,sentiment_analysis)
   polling_endpoint = f"https://api.assemblyai.com/v2/transcript/{j_id}"
   while True:
     transcription_result = requests.get(polling_endpoint, headers=headers).json()
     if transcription_result['status'] == 'completed':
        return transcription_result 
     elif transcription_result['status'] == 'error':
        raise RuntimeError(f"Transcription failed: {transcription_result['error']}")
     
def output_file(filename,output_file,sentiment_analysis):
  data=poll(filename,sentiment_analysis) 
  text_filename=output_file+".txt"
  with open(text_filename,"w") as f:#this statement saves the text file containing the transcription of the audio file
    f.write(data['text'])
  if sentiment_analysis:
    file=output_file+"_sentiment.json"
    with open(file,'w')as f:
      sentiments=data["sentiment_analysis_results"]#and this file saves the json file containing the sentiment analysis of the audio
      json.dump(sentiments,f,indent=4)

output_file(filename,"Review",sentiment_analysis=True)
print("Transcription saved!!")