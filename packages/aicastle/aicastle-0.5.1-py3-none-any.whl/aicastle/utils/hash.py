import hashlib
import os

class UnsupportedTypeError(Exception):
    pass

def get_hash(data=None, prefix="", suffix="", **kwargs):
    # 버전 호환: 이전 버전에서 data 변수가 아닌 text 로 받음
    if ("text" in kwargs) and (data is None):
        data=kwargs["text"]
    
    # 딕셔너리인 경우, 키를 정렬하여 재귀적으로 처리
    if isinstance(data, dict):
        items = sorted((k, get_hash(v)) for k, v in data.items())
        data_string = prefix + str(items) + suffix
    # 리스트인 경우, 요소를 재귀적으로 처리
    elif isinstance(data, list):
        items = [get_hash(item) for item in data]
        data_string = prefix + str(items) + suffix
    # 그 외 타입인 경우, 문자열로 변환
    else :
        data_string = prefix + str(data) + suffix

    # 해시값 생성
    encoded_string = data_string.encode('utf-8', errors='ignore')
    hash_value = hashlib.sha256(encoded_string).hexdigest()
    return hash_value


def get_hash_file(file_path, prefix="", suffix="", use_chunked=True, chunk_size=4096):
    sha256_hash = hashlib.sha256()
    
    # Prefix를 해시 업데이트
    sha256_hash.update(prefix.encode('utf-8', errors='ignore'))
    
    file_size = os.path.getsize(file_path)
    
    # 파일을 읽어와서 해시 업데이트
    with open(file_path, "rb") as f:
        if use_chunked and file_size > chunk_size:
            # 큰 파일을 처리할 때 부분적으로 읽어오는 방식
            for byte_block in iter(lambda: f.read(chunk_size), b""):
                sha256_hash.update(byte_block)
        else:
            # 작은 파일을 처리할 때 파일 전체를 한 번에 읽어오는 방식
            file_content = f.read()
            sha256_hash.update(file_content)
    
    # Suffix를 해시 업데이트
    sha256_hash.update(suffix.encode('utf-8', errors='ignore'))
    
    return sha256_hash.hexdigest()