""" 유튜브 자막 가져오기, 주소 입력받기, 자동 생성 자막 세그먼트도 같이 출력
    pip install youtube-transcript-api
    
    -- 최신 버전으로 업데이트
    pip install --upgrade youtube-transcript-api

    https://www.youtube.com/watch?v=XyljmT8dGA4
    
    자막있는 동영상 : https://www.youtube.com/watch?v=zRz9q8dPjC4
"""

# 파이썬 컴파일 경로가 달라서 현재 폴더의 이미지를 호출하지 못할때 작업디렉토리를 변경한다. 
import os
from pathlib import Path
# src 상위 폴더를 실행폴더로 지정하려고 한다.
###real_path = Path(__file__).parent.parent
real_path = Path(__file__).parent
print(real_path)
#작업 디렉토리 변경
os.chdir(real_path) 


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

def get_youtube_transcript_with_auto(video_id, preferred_languages=['ko', 'en']):
    """
    주어진 YouTube 동영상 ID와 선호 언어 목록에 대해 자막을 가져옵니다.
    공식 자막을 우선하고, 없으면 자동 생성 자막을 시도합니다.
    반환 값은 자막 세그먼트 리스트와 자막 유형(공식/자동)입니다.
    """
    if not video_id:
        return None, "유효한 동영상 ID 없음"

    transcript_segments = None
    transcript_type = "없음"

    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        chosen_transcript_info = None

        # 1. 선호 언어의 공식 자막 찾기 (find_transcript 대신 직접 순회)
        for lang_code in preferred_languages:
            for transcript in transcript_list:
                # 공식 자막이고 언어 코드가 일치하는지 확인
                if transcript.language_code == lang_code and not transcript.is_generated:
                    chosen_transcript_info = transcript
                    transcript_type = "공식"
                    break # 찾았으면 내부 루프 종료
            if chosen_transcript_info:
                break # 찾았으면 외부 루프 종료

        # 2. 공식 자막이 없으면 선호 언어의 자동 생성 자막 찾기 (find_transcript 대신 직접 순회)
        if not chosen_transcript_info:
            print(f"[{video_id}] 공식 자막을 찾을 수 없습니다. 자동 생성 자막을 시도합니다.")
            for lang_code in preferred_languages:
                for transcript in transcript_list:
                    # 자동 생성 자막이고 언어 코드가 일치하는지 확인
                    if transcript.language_code == lang_code and transcript.is_generated:
                        chosen_transcript_info = transcript
                        transcript_type = "자동 생성"
                        break # 찾았으면 내부 루프 종료
                if chosen_transcript_info:
                    break # 찾았으면 외부 루프 종료

        if chosen_transcript_info:
            print(f"[{video_id}] {chosen_transcript_info.language} ({chosen_transcript_info.language_code}) {transcript_type} 자막을 가져옵니다.")
            transcript_segments = chosen_transcript_info.fetch()
            return transcript_segments, transcript_type
        else:
            print(f"[{video_id}] 요청된 언어 ({preferred_languages})로 공식 및 자동 생성 자막 모두 찾을 수 없습니다.")
            return None, "없음"

    except TranscriptsDisabled:
        print(f"[{video_id}] 이 동영상은 자막이 비활성화되어 있습니다.")
        return None, "비활성화"
    except VideoUnavailable:
        print(f"[{video_id}] 동영상을 사용할 수 없거나 비공개/삭제되었습니다.")
        return None, "사용 불가"
    except Exception as e:
        print(f"[{video_id}] 자막을 가져오는 중 예기치 않은 오류가 발생했습니다: {e}")
        return None, f"오류: {str(e)}"


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
        exit() # 잘못된 선택 시 프로그램 종료

    if target_video_id:
        # **여기! 'languages'를 'preferred_languages'로 변경합니다.**
        transcript_data, transcript_type = get_youtube_transcript_with_auto(target_video_id, preferred_languages=['ko', 'en'])

        if transcript_data:
            print(f"\n--- {transcript_type} 자막 내용 (처음 5개 세그먼트) ---")
            for i, segment in enumerate(transcript_data[:5]):
                print(f"[{segment.start:.2f}-{segment.start + segment.duration:.2f}] {segment.text}")
            print(f"... (총 {len(list(transcript_data))}개 세그먼트)")

            full_text = " ".join([segment.text for segment in transcript_data])
            print(f"\n--- 전체 {transcript_type} 자막 텍스트 (앞부분만) ---")
            print(full_text[:1000] + "...") # 앞부분 1000자만 출력
        else:
            print(f"자막을 가져오지 못했습니다. 유형: {transcript_type}")
    else:
        print("자막을 가져올 동영상 ID가 유효하지 않습니다.")
