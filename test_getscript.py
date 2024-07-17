from youtube_transcript_api import YouTubeTranscriptApi
import datetime

def seconds_to_time(seconds):
    # Convert seconds to hh:mm:ss format
    return str(datetime.timedelta(seconds=seconds))

# 유튜브 비디오 ID 입력
video_id = '7zC8-06198g'

# 비디오의 자막 추출
transcript = YouTubeTranscriptApi.get_transcript(video_id)

# 자막 출력
for caption in transcript:
    start_time = caption['start']
    duration = caption['duration']
    text = caption['text']
    end_time = start_time + duration
    print(f"Start: {seconds_to_time(start_time)}, End: {seconds_to_time(end_time)}, Text: {text}")
