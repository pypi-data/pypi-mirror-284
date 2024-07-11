import argparse
import os
import sys

from litellm import completion
from qdrant_client import QdrantClient
from qdrant_client.http import models

from botrun_ask_folder.util.http_util import http_get_request
from .embeddings_to_qdrant import generate_embedding_sync
from .fast_api.util.pdf_util import pdf_page_to_image

DEFAULT_NOTICE_PROMPT = '''
妳是臺灣人，回答要用臺灣繁體中文正式用語不能輕浮、不能隨便
請妳不可以使用簡體中文回答，不可以使用大陸慣用語回答
請妳基於「知識庫」及使用者的提問，step by step 分析之後，列點（要有標題與內容）回答
若「知識庫」有談到相關的時間、數字、數據，務必一定要講出來，才精確，不能省略！
若「知識庫」有談到舉例、案例、故事、示範，務必一定要用例子回答，才能懂，不能省略！
若「知識庫」有時間或日期，而文字內容相似矛盾的話，要用最新時間日期的為準，別用舊的
如果有看到 page-number 的 tag，在結尾附上頁碼
如果有看到 <原始檔案連結> 的 tag，在結尾附上點擊的連結 markdown，markdown裡連結一定要放完整放 tag 裡所包含的資訊，不要自己修改，任何符號都要保留，尤其要保留最開頭的斜線符號
如果有看到 <檔案頁數截圖> 的 tag，在結尾附上點擊的連結 markdown，，markdown裡連結一定要放完整放 tag 裡所包含的資訊，不要自己修改，任何符號都要保留，尤其要保留最開頭的斜線符號
範例：
原本要回答的內容

來源檔案名稱："檔案名稱"[第 n 頁]
[原始檔案連結請點我](<原始檔案連結> tag 裡的內容，務必保留完全相同，不要自行修改)
[頁面截圖請點我](<檔案頁數截圖> 的內容，務必保留完全相同，不要自行修改)
如果妳不會回答的部分，不可以亂猜
'''


def query_qdrant_knowledge_base(qdrant_host,
                                qdrant_port,
                                collection_name,
                                user_input,
                                embedding_model,
                                top_k,
                                hnsw_ef,
                                file_path_field='file_path',
                                text_content_field='text_content',
                                google_file_id_field='google_file_id',
                                page_number_field='page_number',
                                ) -> str:
    qdrant_client_instance = QdrantClient(qdrant_host, port=qdrant_port)
    query_vector = generate_embedding_sync(embedding_model, user_input)
    search_params = models.SearchParams(hnsw_ef=hnsw_ef, exact=False)
    search_result = qdrant_client_instance.search(
        collection_name=collection_name,
        query_vector=query_vector['data'][0]['embedding'],
        search_params=search_params,
        limit=top_k,
        with_payload=True,
        with_vectors=True
    )

    str_knowledge_base = ""
    # fastapi_url = os.environ.get('FAST_API_URL', 'http://localhost:8000')
    api_prefix = '/api/botrun/botrun_ask_folder'
    for idx, hit in enumerate(search_result, start=1):
        google_file_id = hit.payload.get(google_file_id_field, '')
        page_number = hit.payload.get(page_number_field, '')
        str_knowledge_base += (f"\n"
                               f"<a-rag-file>\n"
                               f"<file-path>\n"
                               f"{hit.payload.get(file_path_field, 'N/A')}\n"
                               f"</file-path>\n")
        if google_file_id:
            str_knowledge_base += (f"<原始檔案連結>"
                                   f"{api_prefix}/download_file/{google_file_id}"
                                   f"</原始檔案連結>\n")
        if page_number and page_number.lower() != 'n/a':
            str_knowledge_base += (f"<page-number>\n"
                                   f"{page_number}\n"
                                   f"</page-number>\n")
        if google_file_id and page_number and page_number.lower() != 'n/a':
            # save_pdf_page_to_image(google_file_id, page_number)
            # response = http_get_request(
            #     f"https://asia-east1-scoop-386004.cloudfunctions.net/cf_pdf_page_to_image?file_id={google_file_id}&page={page_number}")
            str_knowledge_base += (f"<檔案頁數截圖>"
                                   f"/api/users/botrun_ask_folder/img/{google_file_id}_{page_number}.png"
                                   # f"{api_prefix}/get_pdf_page/{google_file_id}?page={page_number}\n"
                                   f"</檔案頁數截圖>\n")
        str_knowledge_base += (f"<text-content>\n"
                               f"{hit.payload.get(text_content_field, 'N/A')}"
                               f"</text-content>\n"
                               f"</a-rag-file>\n"
                               )
    os.makedirs("./users/botrun_ask_folder", exist_ok=True)
    open("./users/botrun_ask_folder/str_knowledge_base.txt", "w").write(str_knowledge_base)
    return str_knowledge_base

# def save_pdf_page_to_image(google_file_id, page_number):
#     os.makedirs("./users/botrun_ask_folder/img", exist_ok=True)
#     filename = f"./users/botrun_ask_folder/img/{google_file_id}_{page_number}.png"
#     if not os.path.exists(filename):
#         img_byte_arr = pdf_page_to_image(google_file_id, int(page_number))
#         with open(filename, "wb") as f:
#             f.write(img_byte_arr)

def query_qdrant_and_llm(qdrant_host, qdrant_port, collection_name, user_input,
                         embedding_model, top_k, notice_prompt,
                         chat_model,
                         hnsw_ef, file_path_field, text_content_field, google_file_id_field, page_number_field):
    str_knowledge_base = query_qdrant_knowledge_base(
        qdrant_host, qdrant_port, collection_name, user_input,
        embedding_model, top_k, hnsw_ef, file_path_field, text_content_field, google_file_id_field, page_number_field)
    if not notice_prompt:
        notice_prompt = DEFAULT_NOTICE_PROMPT
    str_message = f'''
    <知識庫RAG搜索到的內容>
    {str_knowledge_base}
    </知識庫RAG搜索到的內容>

    <回答時請妳注意>
    {notice_prompt}
    </回答時請妳注意>

    <使用者提問請妳回答>
    {user_input}
    </使用者提問請妳回答>
    '''
    return completion_call(chat_model, str_message)


def completion_call(model, message):
    try:
        response = completion(
            model=model,
            messages=[{"content": message, "role": "user"}],
            stream=True
        )
        for part in response:
            delta_content = part.choices[0].delta.content
            if delta_content:
                yield delta_content
    except Exception as e:
        print(f"query_qdrant.py, completion_call, exception: {e}")


def query_qdrant_and_llm_print(qdrant_host, qdrant_port, collection_name, user_input,
                               embedding_model, top_k, notice_prompt,
                               chat_model, hnsw_ef, file_path_field, text_content_field,
                               google_file_id_field='google_file_id', page_number_field='page_number'):
    for fragment in query_qdrant_and_llm(qdrant_host, qdrant_port, collection_name, user_input,
                                         embedding_model, top_k, notice_prompt,
                                         chat_model, hnsw_ef, file_path_field, text_content_field,
                                         google_file_id_field, page_number_field):
        print(fragment, end="")
        sys.stdout.flush()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search documents in Qdrant using natural language query.")
    parser.add_argument("--query")
    parser.add_argument("--collection", default="collection_1")
    parser.add_argument("--embedding_model", default="openai/text-embedding-3-large")
    parser.add_argument("--top_k", default=12)
    parser.add_argument("--notice_prompt", default=DEFAULT_NOTICE_PROMPT)
    parser.add_argument("--chat_model", default="gpt-4-turbo-preview")
    parser.add_argument("--hnsw_ef", default=256)
    parser.add_argument("--file_path_field", default="file_path")
    parser.add_argument("--text_content_field", default="text_content")
    args = parser.parse_args()

    qdrant_host = os.getenv('QDRANT_HOST', 'localhost')
    qdrant_port = int(os.getenv('QDRANT_PORT', '6333'))
    query_qdrant_and_llm_print(qdrant_host, qdrant_port, args.collection, args.query,
                               args.embedding_model, args.top_k,
                               args.notice_prompt, args.chat_model,
                               args.hnsw_ef, args.file_path_field,
                               args.text_content_field,
                               )
