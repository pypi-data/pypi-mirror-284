from concurrent import futures
from concurrent.futures import ThreadPoolExecutor
from typing import Union
import string
import sys
import os
import base64
import copyreg
import functools
import hashlib
import http.client as http_client
import json
import logging
from pathlib import Path
import pickle
import random
import re
import ssl
from io import BytesIO
from socket import gethostbyname
from typing import Any
from urllib.parse import unquote, quote, urljoin
from urllib.parse import urlparse
import tldextract
import ipaddress
import queue
from rich.progress import Progress
import faker
import requests
import urllib3
from requests_cache import CachedSession
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.ssl_ import create_urllib3_context
from requests.structures import CaseInsensitiveDict
from requests.utils import to_native_string
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad,unpad


def tobytes(s, encoding="UTF-8"):
    """
    convert to bytes
    """
    if isinstance(s, bytes):
        return s
    elif isinstance(s, bytearray):
        return bytes(s)
    elif isinstance(s,str):
        return s.encode(encoding)
    elif isinstance(s, memoryview):
        return s.tobytes()
    else:
        return bytes([s])


class UniqueQueue(queue.Queue):
    def __init__(self, maxsize=0):
        super().__init__(maxsize)
        self.queue_set = set()

    def put(self, item, block=True, timeout=None):
        """
        一个对象重复put将会忽略
        """
        hash_item = item
        if isinstance(item, dict):
            hash_item = tuple(item.items())
        if hash_item not in self.queue_set:  # 如果元素不在队列中，则添加
            self.queue_set.add(hash_item)
            super().put(item, block, timeout)


def uuencode(binary_data):
    """
    类似java中的UUEncoder实现
    """
    if isinstance(value, str):
        value = value.encode('utf-8')
    # 分块将二进制数据进行 uuencode 编码
    chunk_size = 45
    # At most 45 bytes at once
    encoded_data = ''
    for i in range(0, len(binary_data), chunk_size):
        chunk = binary_data[i:i+chunk_size]
        encoded_chunk = binascii.b2a_uu(chunk)
        encoded_data += encoded_chunk.decode('utf-8')
    return 'begin 644 encoder.buf\n' + encoded_data + 'end\n'


def base64decode(value: str, encoding='utf-8', errors='strict') -> str:
    """
    python3 返回的是bytes
    Decodes string value from Base64 to plain format
    >>> base64decode('Zm9vYmFy')
    'foobar'

    'ignore'：忽略无法解码的字符。直接跳过无法处理的字符，继续解码其他部分。
    'replace'：使用特定字符替代无法解码的字符，默认使用 '�' 代替。例如，b'\xe4\xb8\x96\xe7\x95\x8c'.decode('utf-8', errors='replace') 输出 '世界�'。
    'strict'：默认行为，如果遇到无法解码的字符，抛出 UnicodeDecodeError 异常。
    'backslashreplace'：使用 Unicode 转义序列替代无法解码的字符。例如，b'\xe4\xb8\x96\xe7\x95\x8c'.decode('ascii', errors='backslashreplace') 输出 '\\xe4\\xb8\\x96\\xe7\\x95\\x8c'。
    'xmlcharrefreplace'：使用 XML 实体替代无法解码的字符。例如，b'\xe4\xb8\x96\xe7\x95\x8c'.decode('ascii', errors='xmlcharrefreplace') 输出 '&#19990;&#30028;'。
    'surrogateescape'：将无法解码的字节转换为 Unicode 符号 '�' 的转义码。例如，当解码 Latin-1 字符串时，b'\xe9'.decode('latin-1', errors='surrogateescape') 输出 '\udce9'。

    """
    return str(base64.b64decode(value), encoding=encoding, errors=errors)


def base64encode(value) -> str:
    """
    python3 返回的是bytes
    Encodes string value from plain to Base64 format
    >>> base64encode('foobar')
    'Zm9vYmFy'
    """
    if isinstance(value, str):
        value = value.encode('utf-8')

    return str(base64.b64encode(value), encoding='utf-8')

def base64_urlencode(value) -> str:
    """
    base64encode + urlencode
    """

    return url_encode(base64encode(value))


def base64_urldecode(value: str, encoding='utf-8', errors='strict') -> str:
    """
    urldecode + base64decode
    """
    return base64decode(url_decode(value), encoding=encoding, errors=errors)



def urlsafe_base64encode(value) -> str:
    """
    base64.urlsafe_b64encode
    """
    if isinstance(value, str):
        value = value.encode('utf-8')

    return str(base64.urlsafe_b64encode(value), encoding='utf-8')


def urlsafe_base64decode(value: str, encoding='utf-8', errors='strict') -> str:
    """
    base64.urlsafe_b64decode
    """
    return str(base64.urlsafe_b64decode(value), encoding=encoding, errors=errors)



def base64pickle(value):
    """
    Serializes (with pickle) and encodes to Base64 format supplied (binary) value
    >>> base64pickle('foobar')
    'gAJVBmZvb2JhcnEALg=='
    """

    retVal = None

    try:
        retVal = base64encode(pickle.dumps(value, pickle.HIGHEST_PROTOCOL))
    except:
        warnMsg = "problem occurred while serializing "
        warnMsg += "instance of a type '%s'" % type(value)
        print(warnMsg)

        try:
            retVal = base64encode(pickle.dumps(value))
        except:
            retVal = base64encode(pickle.dumps(str(value), pickle.HIGHEST_PROTOCOL))

    return retVal


def base64unpickle(value):
    """
    Decodes value from Base64 to plain format and deserializes (with pickle) its content
    >>> base64unpickle('gAJVBmZvb2JhcnEALg==')
    'foobar'
    pickle存在安全漏洞
    python sqlmap.py --pickled-options "Y29zCnN5c3RlbQooUydkaXInCnRSLg=="
    """

    retVal = None

    def _(self):
        if len(self.stack) > 1:
            func = self.stack[-2]
            if '.' in repr(func) and " 'lib." not in repr(func):
                raise Exception("abusing reduce() is bad, Mkay!")
        self.load_reduce()

    def loads(str):
        file = BytesIO(str)
        unpickler = pickle.Unpickler(file)
        # unpickler.dispatch[pickle.REDUCE] = _
        dispatch_table = copyreg.dispatch_table.copy()
        dispatch_table[pickle.REDUCE] = _
        return unpickler.load()

    try:
        retVal = loads(base64decode(value))
    except TypeError:
        retVal = loads(base64decode(str(value)))

    return retVal


def rsa_encrypt(data, public_key, block_size=None):
    """rsa encrypt
    需要考虑分段使用公钥加密
    单次加密串的长度最大为(key_size / 8 - 11)
    加密的 plaintext 最大长度是 证书key位数 / 8 - 11, 例如1024 bit的证书，被加密的串最长 1024 / 8 - 11=117,  2048bit证书加密长度是214
    解决办法是分块加密，然后分块解密就行了，
    因为 证书key固定的情况下，加密出来的串长度是固定的。
    PEM有带上-----XXX----，DER则是base64或者二进制
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    rsa_key = RSA.importKey(base64.b64decode(public_key))
    cipher = PKCS1_v1_5.new(rsa_key)

    # 分段加密
    if not block_size:
        # 计算最大加密块大小
        block_size = (rsa_key.size_in_bits() // 8) - 11

    encrypted_chunks = []
    for i in range(0, len(data), block_size):
        chunk = data[i:i + block_size]
        encrypted_chunk = cipher.encrypt(chunk)
        encrypted_chunks.append(encrypted_chunk)

    return base64.b64encode(b''.join(encrypted_chunks)).decode('utf-8')


def rsa_decrypt(data, private_key, block_size=None):
    """rsa decrypt"""
    if isinstance(data, str):
        data = data.encode('utf-8')
    encrypted_data = base64.b64decode(data)
    rsa_key = RSA.importKey(base64.b64decode(private_key))
    cipher = PKCS1_v1_5.new(rsa_key)
    # 分段解密
    if not block_size:
        # 计算最大解密块大小
        block_size = rsa_key.size_in_bytes()
    decrypted_chunks = []
    for i in range(0, len(encrypted_data), block_size):
        chunk = encrypted_data[i:i + block_size]
        decrypted_chunk = cipher.decrypt(chunk, None)
        decrypted_chunks.append(decrypted_chunk)

    return b''.join(decrypted_chunks).decode('utf-8')


def des_encrypt(plaintext: str, key:str, mode=DES.MODE_ECB, padding='pkcs7'):
    """des encrypt
    默认使用ECB模式，padding默认使用pkcs7
    密钥长度不要超过8位，超过8位会报错
    返回的结果是base64编码
    """
    cipher = DES.new(key.encode(), mode)
    padded_plaintext = pad(plaintext.encode(), DES.block_size, style=padding)
    ciphertext = cipher.encrypt(padded_plaintext)
    ciphertext = base64encode(ciphertext)
    return ciphertext

def des_decrypt(ciphertext, key: str, mode=DES.MODE_ECB, padding='pkcs7'):
    """des decrypt
    输入的ciphertext是base64编码
    默认使用ECB模式，padding默认使用pkcs7
    密钥长度不要超过8位，超过8位会报错
    """
    if isinstance(ciphertext, str):
        ciphertext = base64.b64decode(ciphertext)
    cipher = DES.new(key.encode(), mode)
    plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(plaintext, DES.block_size, style=padding)
    return plaintext.decode('utf-8')



def get_redirect_target(self, resp):
    """hook requests.Session.get_redirect_target method"""
    if resp.is_redirect:
        location = resp.headers['location']
        location = location.encode('latin1')
        encoding = resp.encoding if resp.encoding else 'utf-8'
        return to_native_string(location, encoding)
    return None


def patch_redirect():
    requests.Session.get_redirect_target = get_redirect_target


def remove_ssl_verify():
    ssl._create_default_https_context = ssl._create_unverified_context


def patch_getproxies():
    # 高版本python已经修复了这个问题
    # https://bugs.python.org/issue42627
    # https://www.cnblogs.com/davyyy/p/14388623.html
    if os.name == 'nt':
        import urllib.request
        old_getproxies_registry = urllib.request.getproxies_registry
        def hook():
            proxies = old_getproxies_registry()
            if 'https' in proxies:
                proxies['https'] = proxies['https'].replace('https://', 'http://')
            return proxies
        urllib.request.getproxies_registry = hook


urllib3.disable_warnings()
remove_ssl_verify()
patch_redirect()
patch_getproxies()

def str_md5(data) -> str:
    if isinstance(data, str):
        data = data.encode('utf-8')
    return hashlib.md5(data).hexdigest()


def str_sha1(data) -> str:
    if isinstance(data, str):
        data = data.encode('utf-8')
    return hashlib.sha1(data).hexdigest()


def file_md5(file_path) -> str:
    md5lib = hashlib.md5()
    with open(file_path, 'rb') as f:
        md5lib.update(f.read())
    return md5lib.hexdigest()


def file_sha1(file_path):
    sha1 = hashlib.sha1()
    with open(file_path, 'rb') as f:
        sha1.update(f.read())
    return sha1.hexdigest()


def file_sha256(file_path):
    sha1 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        sha1.update(f.read())
    return sha1.hexdigest()


def url_encode_all(string: str) -> str:
    """
    对所有字符都进行url编码
    @param string:
    @return:
    """
    return "".join("%{0:0>2}".format(format(ord(char), "x")) for char in string)


def url_decode(string: str) -> str:
    """
    解码url
    @param string:
    @return:
    """
    return unquote(string)


def url_encode(string: str) -> str:
    """
    url编码
    @param string:
    @return:
    """
    return quote(string)


class BaseUrlSession(requests.Session):
    """A Session with a URL that all requests will use as a base.
    .. note::
        The base URL that you provide and the path you provide are **very**
        important.
    Let's look at another *similar* example
    .. code-block:: python
        >>> from requests_toolbelt import sessions
        >>> s = sessions.BaseUrlSession(
        ...     base_url='https://example.com/resource/')
        >>> r = s.get('/sub-resource/', params={'foo': 'bar'})
        >>> print(r.request.url)
        https://example.com/sub-resource/?foo=bar
    The key difference here is that we called ``get`` with ``/sub-resource/``,
    i.e., there was a leading ``/``. This changes how we create the URL
    because we rely on :mod:`urllib.parse.urljoin`.
    To override how we generate the URL, sub-class this method and override the
    ``create_url`` method.
    Based on implementation from
    https://github.com/kennethreitz/requests/issues/2554#issuecomment-109341010

    作者一直没在requests上加这个功能, urljoin容易有缺陷
    https://stackoverflow.com/questions/42601812/python-requests-url-base-in-session
    """

    base_url = None

    def __init__(self, base_url=None):
        if base_url:
            self.base_url = base_url
        super(BaseUrlSession, self).__init__()

    def request(self, method, url, *args, **kwargs):
        """Send the request after generating the complete URL."""
        url = self.create_url(url)
        return super(BaseUrlSession, self).request(
            method, url, *args, **kwargs
        )

    def prepare_request(self, request, *args, **kwargs):
        """Prepare the request after generating the complete URL."""
        request.url = self.create_url(request.url)
        return super(BaseUrlSession, self).prepare_request(
            request, *args, **kwargs
        )

    def create_url(self, url):
        """Create the URL based off this partial path."""
        return urljoin(self.base_url.rstrip("/") + "/", url.lstrip("/"))


class RequestsSession(requests.Session):
    """
    在请求之前修改或添加请求头信息
    Referer、Origin 还要判session有没有赋值
    """

    def prepare_request(self, request, *args, **kwargs):
        parsed_url = urlparse(request.url)
        if 'Referer' not in request.headers and 'Referer' not in self.headers:
            request.headers['Referer'] = f"{parsed_url.scheme}://{parsed_url.netloc}/"
        if 'Origin' not in request.headers and 'Origin' not in self.headers:
            request.headers['Origin'] = f"{parsed_url.scheme}://{parsed_url.netloc}"

        return super(RequestsSession, self).prepare_request(request, *args, **kwargs)


class CustomSslContextHttpAdapter(HTTPAdapter):
    # https://github.com/urllib3/urllib3/issues/2653
    # openssl 3.0 bug --> (Caused by SSLError(SSLError(1, '[SSL: UNSAFE_LEGACY_RENEGOTIATION_DISABLED] unsafe legacy renegotiation disabled (_ssl.c:1006)')))
    """"Transport adapter" that allows us to use a custom ssl context object with the requests."""

    def init_poolmanager(self, connections, maxsize, block=False):
        ctx = create_urllib3_context()
        ctx.load_default_certs()
        ctx.check_hostname = False # ValueError: Cannot set verify_mode to CERT_NONE when check_hostname is enabled
        ctx.options |= 0x4  # ssl.OP_LEGACY_SERVER_CONNECT
        self.poolmanager = urllib3.PoolManager(ssl_context=ctx)



def requests_session(proxies=False, max_retries=1, timeout=None, debug=False, base_url=None, user_agent=None, use_cache=None):
    """
    返回一个requests创建的session, 添加伪造的ua, 初始化请求头
    @return:
    """
    if use_cache:
        if use_cache == True:
            session = CachedSession()
        else:
            session = CachedSession(**use_cache)
    elif base_url:
        session = BaseUrlSession(base_url)
    else:
        session = RequestsSession()

    fake = faker.Faker('zh_CN')
    session.headers.update({
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'User-Agent': user_agent or fake.chrome(),
        'X-Forwarded-For': fake.ipv4(),
    })
    session.verify = False
    session.mount('http://', HTTPAdapter(max_retries=max_retries))
    session.mount('https://', CustomSslContextHttpAdapter(max_retries=max_retries))

    if timeout is not None:
        session.request = functools.partial(session.request, timeout=timeout)

    if proxies:
        if isinstance(proxies, dict):
            session.proxies = proxies
        elif isinstance(proxies, int):
            session.proxies = {"http": "http://127.0.0.1:" + str(proxies), "https": "http://127.0.0.1:" + str(proxies)}
        else:
            proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
            session.proxies = proxies

    if debug:
        http_client.HTTPConnection.debuglevel = 1
        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True

    return session


ORIGIN_CIPHERS = 'ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+HIGH:RSA+3DES'


class DESAdapter(HTTPAdapter):
    """
    https://blog.csdn.net/god_zzZ/article/details/123010576
    反爬虫检测TLS指纹
    https://ja3er.com/json
    """

    def __init__(self, *args, **kwargs):
        # 在请求中重新启用 3DES 支持的 TransportAdapter
        CIPHERS = ORIGIN_CIPHERS.split(":")
        random.shuffle(CIPHERS)
        # print("1:", CIPHERS)
        CIPHERS = ":".join(CIPHERS)
        # print("2:", CIPHERS)
        self.COPHERS = CIPHERS + ":!aNULL:!eNULL:!MD5"
        super(DESAdapter, self).__init__(*args, **kwargs)

    # 在一般情况下，当我们实现一个子类的时候，__init__的第一行应该是super().__init__(*args, **kwargs)，
    # 但是由于init_poolmanager和proxy_manager_for是复写了父类的两个方法，
    # 这两个方法是在执行super().__init__(*args, **kwargs)的时候就执行的。
    # 所以，我们随机设置 Cipher Suits 的时候，需要放在super().__init__(*args, **kwargs)的前面。
    def init_poolmanager(self, *args, **kwargs):
        context = create_urllib3_context(ciphers=self.COPHERS)
        kwargs["ssl_context"] = context
        return super(DESAdapter, self).init_poolmanager(*args, **kwargs)

    def proxy_manager_for(self, *args, **kwargs):
        context = create_urllib3_context(ciphers=self.COPHERS)
        kwargs["ssl_context"] = context


def extract_dict(text, sep, sep2="="):
    """根据分割方式将字符串分割为字典

    :param text: 分割的文本
    :param sep: 分割的第一个字符 一般为'\n'
    :param sep2: 分割的第二个字符，默认为'='
    :return: 返回一个dict类型，key为sep2的第0个位置，value为sep2的第一个位置
        只能将文本转换为字典，若text为其他类型则会出错
    """
    _dict = CaseInsensitiveDict([l.split(sep2, 1) for l in text.split(sep)])
    return _dict


def httpraw(raw: str, ssl: bool = False, **kwargs):
    """
    代码来源Pocsuite, 修复postData只发送一行的bug
    发送原始HTTP封包请求,如果你在参数中设置了例如headers参数，将会发送你设置的参数
    请求头需要用: 补上空格隔开

    :param raw:原始封包文本
    :param ssl:是否是HTTPS
    :param kwargs:支持对requests中的参数进行设置
    :return:requests.Response
    """
    raw = raw.strip()
    # Clear up unnecessary spaces
    raws = list(map(lambda x: x.strip(), raw.splitlines()))
    try:
        method, path, protocol = raws[0].split(" ")
    except Exception:
        raise Exception("Protocol format error")
    post = None
    _json = None
    if method.upper() == "POST":
        index = 0
        for i in raws:
            index += 1
            if i.strip() == "":
                break
        if len(raws) == index:
            raise Exception
        tmp_headers = raws[1:index - 1]
        tmp_headers = extract_dict('\n'.join(tmp_headers), '\n', ": ")
        postData = '\r\n'.join(raws[index:])
        try:
            json.loads(postData)
            _json = postData
        except ValueError:
            post = postData
    else:
        tmp_headers = extract_dict('\n'.join(raws[1:]), '\n', ": ")
    netloc = "http" if not ssl else "https"
    host = tmp_headers.get("Host", None)
    if host is None:
        raise Exception("Host is None")
    del tmp_headers["Host"]
    if 'Content-Length' in tmp_headers:
        del tmp_headers['Content-Length']
    url = "{0}://{1}".format(netloc, host + path)

    kwargs.setdefault('allow_redirects', True)
    kwargs.setdefault('data', post)
    kwargs.setdefault('headers', tmp_headers)
    kwargs.setdefault('json', _json)

    with requests_session() as session:
        return session.request(method=method, url=url, **kwargs)


requests.httpraw = httpraw


def removesuffix(self: str, suffix: str) -> str:
    return self[:-len(suffix)] if self.endswith(suffix) else self


def removeprefix(self: str, prefix: str) -> str:
    if self.startswith(prefix):
        return self[len(prefix):]
    else:
        return self[:]


def match1(text, *patterns):
    """Scans through a string for substrings matched some patterns (first-subgroups only).

    Args:
        text: A string to be scanned.
        patterns: Arbitrary number of regex patterns.

    Returns:
        When only one pattern is given, returns a string (None if no match found).
        When more than one pattern are given, returns a list of strings ([] if no match found).
    """

    if len(patterns) == 1:
        pattern = patterns[0]
        match = re.search(pattern, text)
        if match:
            return match.group(1)
        else:
            return None
    else:
        ret = []
        for pattern in patterns:
            match = re.search(pattern, text)
            if match:
                ret.append(match.group(1))
        return ret


def str_to_bool(value: Any) -> bool:
    """Return whether the provided string (or any value really) represents true. Otherwise false.
    Just like plugin server stringToBoolean.
    Replace distutils.strtobool
    """
    if not value:
        return False

    val = str(value).lower()
    if val in ('y', 'yes', 't', 'true', 'on', '1'):
        return True
    elif val in ('n', 'no', 'f', 'false', 'off', '0'):
        return False
    else:
        raise ValueError("invalid truth value %r" % (val,))


def cut_list(obj, size):
    return [obj[i:i + size] for i in range(0, len(obj), size)]


def url2ip(url, with_port=False):
    """
    works like turning 'http://baidu.com' => '180.149.132.47'
    """

    url_prased = urlparse(url)
    if url_prased.port:
        ret = gethostbyname(url_prased.hostname), url_prased.port
    elif not url_prased.port and url_prased.scheme == 'https':
        ret = gethostbyname(url_prased.hostname), 443
    else:
        ret = gethostbyname(url_prased.hostname), 80

    return ret if with_port else ret[0]


def get_middle_text(text, prefix, suffix, index=0):
    """
    获取中间文本的简单实现

    :param text:要获取的全文本
    :param prefix:要获取文本的前部分
    :param suffix:要获取文本的后半部分
    :param index:从哪个位置获取
    :return:
    """
    try:
        index_1 = text.index(prefix, index)
        index_2 = text.index(suffix, index_1 + len(prefix))
    except ValueError:
        # logger.log(CUSTOM_LOGGING.ERROR, "text not found pro:{} suffix:{}".format(prefix, suffix))
        return ''
    return text[index_1 + len(prefix):index_2]


def touch(filepath, mode=0o666, exist_ok=True):
    return Path(filepath, mode=mode, exist_ok=exist_ok).touch()


def read_text(filepath: Union[Path, str], mode='r', encoding='utf-8', not_exists_ok: bool = False, errors=None) -> str:
    """
    errors-->
    'ignore'：忽略无法解码的字符。直接跳过无法处理的字符，继续解码其他部分。
    'replace'：使用特定字符替代无法解码的字符，默认使用 '�' 代替。例如，b'\xe4\xb8\x96\xe7\x95\x8c'.decode('utf-8', errors='replace') 输出 '世界�'。
    'strict'：默认行为，如果遇到无法解码的字符，抛出 UnicodeDecodeError 异常。
    'backslashreplace'：使用 Unicode 转义序列替代无法解码的字符。例如，b'\xe4\xb8\x96\xe7\x95\x8c'.decode('ascii', errors='backslashreplace') 输出 '\\xe4\\xb8\\x96\\xe7\\x95\\x8c'。
    'xmlcharrefreplace'：使用 XML 实体替代无法解码的字符。例如，b'\xe4\xb8\x96\xe7\x95\x8c'.decode('ascii', errors='xmlcharrefreplace') 输出 '&#19990;&#30028;'。
    'surrogateescape'：将无法解码的字节转换为 Unicode 符号 '�' 的转义码。例如，当解码 Latin-1 字符串时，b'\xe9'.decode('latin-1', errors='surrogateescape') 输出 '\udce9'。
    """
    if isinstance(filepath, Path):
        filepath = str(filepath)
    if mode == 'rb':
        encoding = None
    if not_exists_ok and not Path(filepath).is_file():
        return ''
    with open(filepath, mode, encoding=encoding, errors=errors) as f:
        content = f.read()
    return content


def read_json(filepath: Union[Path, str], encoding='utf-8', not_exists_ok: bool = False) -> dict:
    if isinstance(filepath, Path):
        filepath = str(filepath)
    if not_exists_ok and not Path(filepath).is_file():
        return {}
    with open(filepath, 'r', encoding=encoding) as f:
        return json.load(f)


def read_lines(filepath: Union[Path, str], encoding='utf-8', not_exists_ok: bool = False) -> list:
    if isinstance(filepath, Path):
        filepath = str(filepath)
    lines = []
    if not_exists_ok and not Path(filepath).is_file():
        return lines
    with open(filepath, 'r', encoding=encoding) as f:
        # lines = f.readlines()
        # lines = [line.rstrip() for line in lines]  只会创建一个生成器 不会有性能问题
        for line in f:
            line = line.rstrip()
            if line:
                lines.append(line)
    return lines


def write_text(filepath: Union[Path, str], content, mode='w', encoding='utf-8'):
    if isinstance(filepath, Path):
        filepath = str(filepath)
    if mode == 'wb':
        encoding = None
    if content is None:
        raise ValueError('content must not be None')
    with open(filepath, mode, encoding=encoding) as f:
        f.write(content)


def write_lines(filepath: Union[Path, str], lines, mode='w', encoding='utf-8'):
    if isinstance(filepath, Path):
        filepath = str(filepath)
    if lines is None:
        raise ValueError('lines must not be None')
    with open(filepath, mode, encoding=encoding) as f:
        for l in lines:
            f.write(l + '\n')


def write_json(filepath: Union[Path, str], json_obj: dict, encoding='utf-8'):
    if isinstance(filepath, Path):
        filepath = str(filepath)
    if json_obj is None:
        raise ValueError('json_obj must not be None')
    with open(filepath, 'w', encoding=encoding) as f:
        json.dump(json_obj, f, indent=4, ensure_ascii=False)


def splitlines(string: str) -> list:
    """
    提供多行字符串，用换行分隔成list，trim并且去重，不包括空行
    """
    data = []
    for l in string.splitlines():
        l = l.strip()
        if l and l not in data:
            data.append(l)
    return data


def get_resource_dir(basedir=None):
    if not basedir:
        basedir = sys._getframe(1).f_code.co_filename
    current_dir = resource_folder = getattr(sys, '_MEIPASS', os.path.dirname(basedir))

    while True:
        resource_folder = os.path.join(current_dir, "resource")

        if os.path.exists(resource_folder) and os.path.isdir(resource_folder):
            break

        # 到达根目录 (盘符根目录) 时停止搜索
        if len(current_dir) <= 3:
            break

        current_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

    return resource_folder


def get_resource(filename):
    if Path(filename).exists():
        return filename
    resource_path = get_resource_dir(sys._getframe(1).f_code.co_filename) + "/" + filename
    if Path(resource_path).exists():
        return str(Path(resource_path).absolute())
    if Path('~/'+filename).expanduser().exists():
        return str(Path('~/'+filename).expanduser().absolute())


def get_maindomain(subdomain):
    # get the main domain from subdomain
    tld = tldextract.extract(subdomain)
    if tld.suffix != '':
        domain = f'{tld.domain}.{tld.suffix}'
    else:
        domain = tld.domain
    return domain


def rand_base(length, letters=string.ascii_lowercase + string.digits):
    """从可选字符集生成给定长度字符串的随机序列(默认为字母和数字)
    """
    return ''.join(random.choice(letters) for i in range(length))


def is_private_ip(ip):
    """
    判断IP地址是否是内网IP，如果传入的不是有效IP则也会返回False
    """
    try:
        ip_obj = ipaddress.ip_address(ip)
        return ip_obj.is_private
    except ValueError:
        return False


def is_internal_url(url):
    """
    判断URL是否是内网IP对应的URL
    """
    # 提取URL中的IP地址
    parsed_url = urlparse(url)
    netloc = parsed_url.netloc.split(':')[0]
    ip = netloc if netloc else parsed_url.hostname
    # 判断IP地址是否是内网IP
    return is_private_ip(ip)


def is_wildcard_dns(domain):
    """
    传入主域名
    判断域名是否有泛解析
    """
    import dns
    nonexistent_domain = rand_base(8) + '.' + domain
    try:
        answers = dns.resolver.resolve(nonexistent_domain, 'A')
        ip_list = [j for i in answers.response.answer for j in i.items]
        return True
    except Exception as e:
        return False


def is_valid_ip(ip: str) -> bool:
    """
    判断是否是有效的IP地址，支持IPv4Address、IPv6Address
    """
    try:
        ip_address = ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def is_wildcard_dns_batch(domain_list: iter, thread_num: int = 10, show_progress: bool = True) -> dict:
    """
    多线程批量判断域名是否泛解析
    传入域名或者URL列表、，支持解析成主域名
    """
    result = {}
    with ThreadPoolExecutor(max_workers=thread_num) as executor:

        future_map = {}
        for domain in domain_list:
            if domain.startswith(('http://', 'https://')):
                domain = urlparse(domain).hostname

            if is_valid_ip(domain):
                result[domain] = False
            else:
                main_domain = get_maindomain(domain)
                if main_domain not in result:
                    result[main_domain] = False
                    future_map[executor.submit(is_wildcard_dns, main_domain)] = main_domain

        if show_progress:
            with Progress() as progress:
                task_id = progress.add_task("[red]is_wildcard_dns_batch", total=len(future_map))
                for future in futures.as_completed(future_map):
                    result[future_map[future]] = future.result()
                    progress.update(task_id, advance=1)
        else:
            for future in futures.as_completed(future_map):
                result[future_map[future]] = future.result()

    return result




def string_to_bash_variable(string):
    # 定义不允许出现在bash变量名中的字符
    invalid_chars = ['.', '/', '-', '=', '`', "'", '"']
    # 将字符串中的非法字符替换成下划线
    bash_var = ''.join(['_' if c in invalid_chars else c for c in string])
    # 如果变量以数字开头，则在前面添加下划线
    if bash_var[0].isdigit():
        bash_var = '_' + bash_var
    # 将变量名转换为合法的bash变量名（只包含字母、数字和下划线）
    bash_var = ''.join([c if c.isalnum() or c == '_' else '' for c in bash_var])

    return bash_var