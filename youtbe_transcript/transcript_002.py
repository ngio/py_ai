""" 유튜브 자막 가져오기, 주소 입력받기 
    pip install youtube-transcript-api
    
    -- 최신 버전으로 업데이트
    pip install --upgrade youtube-transcript-api

    https://www.youtube.com/watch?v=XyljmT8dGA4
    
    자막있는 동영상 : https://www.youtube.com/watch?v=zRz9q8dPjC4
"""


from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled, VideoUnavailable
import re # 정규표현식 모듈 임포트

def extract_video_id(youtube_url):
    """
    YouTube URL에서 동영상 ID를 추출합니다.
    다양한 형태의 YouTube URL을 처리할 수 있습니다.
    """
    # 일반적인 YouTube 동영상 URL (v= 뒤)
    match = re.search(r'(?:v=|youtu\.be\/|embed\/)([a-zA-Z0-9_-]{11})', youtube_url)
    if match:
        return match.group(1)
    # 짧은 URL (youtu.be/ 뒤)
    match = re.search(r'youtu\.be\/([a-zA-Z0-9_-]{11})', youtube_url)
    if match:
        return match.group(1)
    # 그 외 (예: shorts URL)
    match = re.search(r'youtube\.com\/shorts\/([a-zA-Z0-9_-]{11})', youtube_url)
    if match:
        return match.group(1)
    return None # 유효한 ID를 찾지 못한 경우

def get_youtube_transcript(video_id, languages=['ko', 'en']):
    """
    주어진 YouTube 동영상 ID와 언어 목록에 대해 자막을 가져옵니다.
    자동 생성 자막과 공식 자막을 모두 시도합니다.
    """
    if not video_id:
        print("유효한 동영상 ID를 찾을 수 없습니다.")
        return None

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
        except Exception as e: # 요청 과다 등을 포함한 모든 예외를 잡습니다.
            print(f"[{video_id}] 자막을 가져오는 중 예기치 않은 오류가 발생했습니다: {e}")
            return None

    except TranscriptsDisabled:
        print(f"[{video_id}] 이 동영상은 자막이 비활성화되어 있습니다.")
        return None
    except VideoUnavailable:
        print(f"[{video_id}] 동영상을 사용할 수 없거나 비공개/삭제되었습니다.")
        return None
    except Exception as e: # 모든 예외를 잡습니다.
        print(f"[{video_id}] 자막을 가져오는 중 예기치 않은 오류가 발생했습니다: {e}")
        return None


if __name__ == "__main__":
    print("유튜브 동영상 자막 가져오기")
    print("1. 유튜브 URL 입력")
    print("2. 동영상 ID 직접 입력")

    choice = input("선택 (1 또는 2): ")
    target_video_id = None

    if choice == '1':
        youtube_url_input = input("유튜브 동영상 URL을 입력하세요: ")
        target_video_id = extract_video_id(youtube_url_input)
    elif choice == '2':
        target_video_id = input("유튜브 동영상 ID를 직접 입력하세요: ")
        # 동영상 ID의 유효성 검사 (간단하게 11자리인지 확인)
        if not (target_video_id and len(target_video_id) == 11 and re.match(r'[a-zA-Z0-9_-]{11}', target_video_id)):
            print("유효하지 않은 동영상 ID 형식입니다. 11자리의 영숫자(하이픈, 밑줄 포함)여야 합니다.")
            target_video_id = None
    else:
        print("잘못된 선택입니다. 프로그램을 종료합니다.")

    if target_video_id:
        print(f"\n--- 처리할 동영상 ID: {target_video_id} ---")
        transcript_data = get_youtube_transcript(target_video_id, languages=['ko', 'en'])

        if transcript_data:
            print("\n--- 자막 내용 (처음 5개 세그먼트) ---")
            for i, segment in enumerate(transcript_data[:5]):
                print(f"[{segment.start:.2f}-{segment.start + segment.duration:.2f}] {segment.text}")
            print(f"... (총 {len(list(transcript_data))}개 세그먼트)")

            full_text = " ".join([segment.text for segment in transcript_data])
            print("\n--- 전체 자막 텍스트 (앞부분만) ---")
            print(full_text[:1000] + "...") # 앞부분 1000자만 출력
        else:
            print("자막을 가져오지 못했습니다.")
    else:
        print("자막을 가져올 동영상 ID가 유효하지 않습니다.")
