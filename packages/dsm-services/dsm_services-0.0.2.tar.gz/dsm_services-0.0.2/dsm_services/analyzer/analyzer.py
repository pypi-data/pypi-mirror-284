import requests
from IPython.display import display, Markdown, IFrame
import uuid
import os
from .. import utils


def create_mermaid_html(mermaid_code):
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ startOnLoad: true }});
        </script>
    </head>
    <body>
        <div class="mermaid">
            {mermaid_code}
        </div>
    </body>
    </html>
    """
    return html_template
    
class MarkdownText:
    def __init__(self, text):
        self.text = text
    def display(self):
        display(Markdown(self.text))
    def __repr__(self):
        return f"MarkdownText {self.text[:50]}..."
    def __str__(self):
        return f"MarkdownText {self.text[:50]}..."
        
class Analyzer:
    def __init__(self, service_uri, api_key):
        self._service_uri = service_uri
        self._header = {
            'Authorization': f'Api-Key {api_key}'
        }
        res = requests.get(f"{self._service_uri}/training/api/")
        utils.check_http_status_code(response=res, extra_text="Can not connect to service")
        os.makedirs('tmp', exist_ok=True)
    
    def list_district(self):
        res = requests.get(f"{self._service_uri}/training/api/district/")
        utils.check_http_status_code(response=res)
        return res.json()

    def get_district(self, district_id):
        res = requests.get(f"{self._service_uri}/training/api/district/{district_id}/")
        utils.check_http_status_code(response=res)
        return MarkdownText(res.json().get('context'))

    def prep_context(self, data):
        require_key = {'1.1', '1.2', '1.3', '2', '3', '4', '5', '6', '7', '8', '9'}
        diff = require_key - set(data.keys())
        if diff!=set():
            raise Exception(f"Please input key {diff}")
        data10 = data.get('10')
        if data10: data10 = f"\n{data10}"
        template = f"""
# {data.get('1.1')}

## ธุรกิจ
{data.get('1.2')}

## สถานที่ตั้ง
{data.get('1.3')}

## แนวคิด
{data.get('2')}

## เอกลักษณ์
{data.get('3')}

## ปัญหา
{data.get('4')}

## จุดแข็งจุดอ่อน
{data.get('5')}

## สินค้าและบริการ
{data.get('6')}

## กลุ่มลูกค้า
{data.get('7')}

## ส่วนร่วมในชุมชน
{data.get('8')}

## แผนในอนาคต
{data.get('9')}

{f"## เพิ่มเติม {data10}" if '10' in data else ''}
"""
        return MarkdownText(template)
            
    def upload_context(self, context, district_id):
        if type(context) != MarkdownText:
            raise Exception("Please input `context` type MarkdownText")
        res = requests.post(
            f"{self._service_uri}/training/api/context/", headers=self._header,
            json={
                'context': context.text,
                'district': district_id
            }
       )
        utils.check_http_status_code(response=res)
        return res.json()

    def get_wizmap(self, version=-1):
        res = requests.get(f"{self._service_uri}/training/api/wizmap/", headers=self._header)
        utils.check_http_status_code(response=res)
        versions = res.json()[::-1]
        v = versions[version]
        print(f"\twizmap {v}")
        res = requests.get(f"{self._service_uri}/training/api/wizmap/{v.get('id')}/", headers=self._header)
        utils.check_http_status_code(response=res)
        data = res.json()
        url = f"https://poloclub.github.io/wizmap/?dataURL={data.get('data').replace('http', 'https')}&gridURL={data.get('grid').replace('http', 'https')}"
        print(url)
        topic = "- "+"\n- ".join(data.get('topic'))
        template = f"""
# Topics

{topic}
"""
        display(Markdown(template))
        return IFrame(src=url, width='100%', height='600px')

    def rag(self, prompt):
        res = requests.post(f"{self._service_uri}/training/api/rag/", headers=self._header, json={'prompt': prompt})
        utils.check_http_status_code(response=res)
        return MarkdownText(res.json().get('response'))

    def list_rag(self):
        res = requests.get(f"{self._service_uri}/training/api/rag/", headers=self._header)
        utils.check_http_status_code(response=res)
        return res.json()

    def get_rag(self, rag_id):
        res = requests.get(f"{self._service_uri}/training/api/rag/{rag_id}/", headers=self._header)
        utils.check_http_status_code(response=res)
        template = f"""
# Prompt
{res.json().get('prompt')}

# Result
{res.json().get('response')}
        """
        return MarkdownText(template)

    def create_mindmap(self, prompt):
        res = requests.post(f"{self._service_uri}/training/api/rag/mermaid/", headers=self._header, json={'prompt': prompt})
        utils.check_http_status_code(response=res)
        
        html_content = create_mermaid_html(res.json().get('response'))
        
        html_file = f"tmp/{uuid.uuid4().hex}.html"
        with open(html_file, "w") as file:
            file.write(html_content)
        
        return IFrame(src=html_file, width="100%", height=600)