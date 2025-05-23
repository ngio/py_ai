## py_ai

# AI 관련 



# 파이썬으로 AI 에이전트 만들기 
https://github.com/dabidstudio/python-ai-agents

# 함께해요 파이썬 생태계
https://wikidocs.net/book/14021
![image](https://github.com/user-attachments/assets/61963c80-6de2-4d9e-ac19-fab9761b3158)

# 자세히 쓰는 Gemini API
https://wikidocs.net/book/14285
![image](https://github.com/user-attachments/assets/f9c7e452-9bcd-404d-8eb2-c7bc8086600d)

    Google Gemini API의 사용법을 쉽고 자세히 배우는 책입니다.
    
    다음 독자들이 읽으면 좋습니다.
    
    파이썬 기초 지식은 있으며, LLM API를 처음 배우려는 독자
    프로그래밍 경험이 있으며, LLM API를 처음 배우려는 독자
    챗GPT API를 다루어 본 독자

# steamlit
* 문서 : https://docs.streamlit.io/get-started/fundamentals/main-concepts

Streamlit은 데이터 과학자와 머신러닝 엔지니어에게 매우 유용한 도구로, 복잡한 웹 프레임워크를 사용하지 않고도 강력한 웹 애플리케이션을 신속하게 개발할 수 있게 해줍니다.

특히 Streamlit 에서 운영하는 Cloud에 Streamlit application이 들어있는 github 레포지터리를 등록하면, 무료로 streamlit을 운영할 수 있는 점도 매우 큰 장점입니다.2 이 서비스를 이용하여 https://{my app name}.streamlit.app 주소로 나만의 Streamlit web app. 을 운영해 볼 수 있습니다.



# 가상환경 생성

    (p_ai) PS D:\_py_ai> conda create -n p_ai python=3.10
    
    (base) PS D:\_py_ai> conda activate p_ai
    (p_ai) PS D:\_py_ai> conda env list



# 명령어
    conda create -n p_ai python=3.10
    conda activate p_ai
    conda install streamlit numpy pandas matplotlib

![image](https://github.com/user-attachments/assets/c9ba575b-2069-4eb6-ad20-92019984162b)


# Streamlit 확장 도구

Streamlit은 Python으로 간편하게 웹 애플리케이션을 만들 수 있는 훌륭한 도구입니다. 이를 더욱 확장하고 기능을 강화하기 위해 다양한 추가 패키지(애드온)가 제공됩니다. 이러한 패키지들은 스트림릿의 기능을 보완하거나 특정한 요구를 충족시키는 데 도움을 줍니다. 아래는 대표적인 Streamlit 애드온 패키지들입니다.

    pip install streamlit-extras
    pip install streamlit-option-menu
    pip install streamlit-aggrid
    pip install streamlit-pandas-profiling
    pip install streamlit-ace
    pip install streamlit-echarts

![image](https://github.com/user-attachments/assets/96273787-ee17-4f95-bc06-aba1c3ac3ec2)





* 가상 환경 확인 (선택 사항):
가상 환경이 제대로 활성화되었는지 확인하려면, 다음 명령어를 입력하여 현재 사용 중인 파이썬의 경로를 확인합니다.    

        >
        >where python
        >

* Ctrl + ` : VScode에서 터미널 오픈
  
#  Streamlit 앱을 종료하는 방법
    1. Ctrl + C 를 이용한 종료 (가장 일반적이고 권장되는 방법)
    대부분의 Streamlit 앱은 명령 프롬프트(CMD) 또는 PowerShell에서 streamlit run your_app.py 명령어를 사용하여 실행합니다. 
    이 경우 앱을 종료하는 가장 일반적이고 권장되는 방법은 다음과 같습니다.
    
    Streamlit 앱을 실행했던 명령 프롬프트 또는 PowerShell 창으로 돌아갑니다.
    앱을 실행할 때 사용했던 검은색 또는 파란색 터미널 창을 찾으세요.
    Ctrl + C 키를 동시에 누릅니다.
    키보드의 Ctrl 키를 누른 상태에서 C 키를 한 번 누릅니다.


* steamlit 실행시 URL :  http://localhost:8501/

***

## 파이썬 분야별 추천 라이브러리

| 대분류 | 분야 | 라이브러리들 |
| :------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **데이터 과학** | 데이터 분석 | **Pandas**, **NumPy**, **SciPy** |
| | 이미지 처리 | **Pillow**, **OpenCV**, **scikit-image** |
| | 오디오 처리 | **librosa**, **PyAudio**, **wave** |
| | 비디오 처리 | **MoviePy**, **OpenCV** |
| | 자연어 처리 | **NLTK**, **spaCy**, **Gensim**, **KoNLPy** |
| | 시계열 데이터 | **Statsmodels**, **Facebook's Prophet** |
| | 데이터 시각화 | **Matplotlib**, **Seaborn**, **Plotly**, **Bokeh** |
| | 머신 러닝 및 딥러닝 | **scikit-learn**, **TensorFlow**, **PyTorch**, **Keras**, **FastAI** |
| **웹 개발** | 웹 프레임워크 | **Flask**, **Django**, **FastAPI** |
| | 웹 스크래핑 | **BeautifulSoup**, **Scrapy**, **Selenium** |
| | API 개발 | **FastAPI**, **Flask-RESTful**, **Django REST framework** |
| | 웹 App | **Streamlit** |
| | 클라우드 인터페이스 | **boto3** (for AWS), **google-cloud-python** (GCP), **azure-sdk-for-python** (Azure) |
| **네트워킹** | 비동기 프로그래밍 | **asyncio**, **aiohttp**, **Twisted** |
| | 네트워크 자동화 | **Ansible**, **Fabric**, **Paramiko** |
| | HTTP 클라이언트 | **Requests**, **HTTPX** |
| | 소켓 프로그래밍 | **socket**, **PyZMQ** |
| | 실시간 통신 | **WebSockets**, **Socket.IO**, **MQTT** (with paho-mqtt) |
| **파일 및 데이터 처리** | 표준 라이브러리 | **glob**, **os**, **shutil** |
| | CSV/Excel 처리 | **Pandas**, **openpyxl**, **csvkit** |
| | JSON/XML 처리 | **json** (stdlib), **xml.etree.ElementTree**, **lxml** |
| | 파일 및 데이터 직렬화 | **JSON** (stdlib), **pickle** (stdlib), **PyYAML** |
| **GUI 개발** | 데스크톱 애플리케이션 | **Tkinter**, **PyQt/PySide**, **Kivy**, **wxPython** |
| **게임 개발** | 게임 개발 프레임워크 | **Pygame**, **Panda3D** |
| | 게임 엔진 스크립팅 | **Godot** (with Python scripting), **Blender Python API**, **Ren'Py** |
| | 3D 그래픽스 | **Blender Python API**, **PyOpenGL**, **Panda3D** |
| **데이터베이스** | ORM | **SQLAlchemy**, **Django ORM**, **Peewee** |
| | 데이터베이스 드라이버 | **pymongo** (MongoDB), **redis-py (Redis)**, **psycopg2** (for PostgreSQL), **PyMySQL** (for MySQL) |
| **개발 도구 및 유틸리티** | 버전 관리 | **GitPython**, **dulwich** |
| | 가상 환경 관리 | **virtualenv**, **conda**, **Pipenv** |
| | 코드 품질 및 스타일 | **Ruff**, **Flake8**, **Black**, **isort** |
| | 테스트 및 QA | **PyTest**, **unittest**, **Selenium** |
| | 빌드 도구 | **setuptools**, **Poetry**, **Pipenv** |
| | 커맨드 라인 도구 | **Click**, **argparse** (stdlib), **Typer** |
| **기타** | 학습 및 교육용 | **Jupyter**, **IPython**, **nbgrader** |

---




