""" 유튜브 자막 가져오기 
    pip install youtube-transcript-api
    
    -- 최신 버전으로 업데이트
    pip install --upgrade youtube-transcript-api

    https://www.youtube.com/watch?v=XyljmT8dGA4
    
    자막있는 동영상 : https://www.youtube.com/watch?v=zRz9q8dPjC4
"""


from youtube_transcript_api import YouTubeTranscriptApi
# youtube_transcript_api._errors 에서 TooManyRequests를 제외하고 임포트합니다.
# TooManyRequests는 더 이상 직접 임포트할 수 없는 것으로 보입니다.
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled, VideoUnavailable

def get_youtube_transcript(video_id, languages=['ko', 'en']):
    """
    주어진 YouTube 동영상 ID와 언어 목록에 대해 자막을 가져옵니다.
    자동 생성 자막과 공식 자막을 모두 시도합니다.
    """
    try:
        # 우선 공식 자막을 시도
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        # 사용 가능한 언어 목록에서 요청한 언어 중 하나를 찾아 가져옵니다.
        chosen_transcript = None
        for lang_code in languages:
            for transcript in transcript_list:
                if transcript.language_code == lang_code:
                    chosen_transcript = transcript
                    break
            if chosen_transcript:
                break

        if chosen_transcript:
            print(f"[{video_id}] {chosen_transcript.language} ({chosen_transcript.language_code}) 자막을 가져옵니다.")
            # fetch()는 이제 FetchedTranscript 객체를 반환하며, 이는 이터러블합니다.
            transcript_segments = chosen_transcript.fetch()
            return transcript_segments
        else:
            raise NoTranscriptFound(
                f"No suitable official transcript found for video {video_id} in languages {languages}.",
                video_id
            )

    except NoTranscriptFound:
        print(f"[{video_id}] 공식 자막을 찾을 수 없습니다. 자동 생성 자막을 시도합니다.")
        try:
            for lang_code in languages:
                try:
                    # get_transcript() 역시 이터러블한 객체를 반환하는 것으로 가정합니다.
                    transcript_segments = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang_code], preserve_formatting=True)
                    print(f"[{video_id}] {lang_code} 자동 생성 자막을 가져왔습니다.")
                    return transcript_segments
                except NoTranscriptFound:
                    continue # 다음 언어로 시도
            print(f"[{video_id}] 요청된 언어 ({languages})로 자동 생성 자막도 찾을 수 없습니다.")
            return None # 적합한 자막을 찾지 못함
        except TranscriptsDisabled:
            print(f"[{video_id}] 이 동영상은 자막이 비활성화되어 있습니다.")
            return None
        except VideoUnavailable:
            print(f"[{video_id}] 동영상을 사용할 수 없거나 비공개/삭제되었습니다.")
            return None
        except Exception as e: # TooManyRequests를 포함한 모든 예외를 잡습니다.
            # 이 부분에서 TooManyRequests 에러를 포함하여 일반적인 오류를 처리합니다.
            print(f"[{video_id}] 자막을 가져오는 중 예기치 않은 오류가 발생했습니다: {e}")
            return None

    except TranscriptsDisabled:
        print(f"[{video_id}] 이 동영상은 자막이 비활성화되어 있습니다.")
        return None
    except VideoUnavailable:
        print(f"[{video_id}] 동영상을 사용할 수 없거나 비공개/삭제되었습니다.")
        return None
    except Exception as e: # TooManyRequests를 포함한 모든 예외를 잡습니다.
        # 이 부분에서 TooManyRequests 에러를 포함하여 일반적인 오류를 처리합니다.
        print(f"[{video_id}] 자막을 가져오는 중 예기치 않은 오류가 발생했습니다: {e}")
        return None


if __name__ == "__main__":
    # 예시 동영상 ID (실제 존재하는 동영상 ID로 변경해야 합니다)
    # 제가 추천해 드렸던 URL에서 ID를 추출했습니다.
    video_id_with_subtitle = "XyljmT8dGA4" # "모바일 유튜브 자동번역 한글자막 보는 방법"
    video_id_auto_caption = "XyljmT8dGA4" # 짧은 영상 (자동 생성 자막 가능성)
    #video_id_invalid = "invalid_video_id_123"
    video_id_invalid = "XyljmT8dGA4"

    print("--- 예제 1: 자막이 있는 동영상 ---")
    transcript_data = get_youtube_transcript(video_id_with_subtitle, languages=['ko', 'en'])
    if transcript_data:
        # segment.start, segment.duration, segment.text와 같이 속성으로 접근합니다.
        for i, segment in enumerate(transcript_data[:5]): # 슬라이싱은 여전히 가능해야 합니다.
            print(f"[{segment.start:.2f}-{segment.start + segment.duration:.2f}] {segment.text}")
        print(f"... (총 {len(list(transcript_data))}개 세그먼트)") # len()을 위해 list로 변환

        # 전체 자막 텍스트만 추출하고 싶다면:
        full_text = " ".join([segment.text for segment in transcript_data])
        print("\n--- 전체 자막 텍스트 (예제 1) ---")
        print(full_text[:500] + "...")
    else:
        print("자막을 가져오지 못했습니다.")

    print("\n--- 예제 2: 자동 생성 자막을 시도할 수 있는 동영상 ---")
    transcript_data_auto = get_youtube_transcript(video_id_auto_caption, languages=['en', 'ko'])
    if transcript_data_auto:
        for i, segment in enumerate(transcript_data_auto[:5]):
            print(f"[{segment.start:.2f}-{segment.start + segment.duration:.2f}] {segment.text}")
        print(f"... (총 {len(list(transcript_data_auto))}개 세그먼트)")
    else:
        print("자막을 가져오지 못했습니다.")

    print("\n--- 예제 3: 존재하지 않는 동영상 ID ---")
    transcript_data_invalid = get_youtube_transcript(video_id_invalid)
    if transcript_data_invalid:
        print("자막을 가져왔습니다.")
    else:
        print("자막을 가져오지 못했습니다.")


