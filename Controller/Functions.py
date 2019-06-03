import os
import re
import sys
from uuid import uuid4

patterns = {
    '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
    '[đ]': 'd',
    '[èéẻẽẹêềếểễệ]': 'e',
    '[ìíỉĩị]': 'i',
    '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
    '[ùúủũụưừứửữự]': 'u',
    '[ỳýỷỹỵ]': 'y'
}

def convert(text):
    """
    Convert from 'Tieng Viet co dau' thanh 'Tieng Viet khong dau'
    text: input string to be converted
    Return: string converted
    """
    output = text
    for regex, replace in patterns.items():
        output = re.sub(regex, replace, output)
        # deal with upper case
        output = re.sub(regex.upper(), replace.upper(), output)
    return output
def splitTitle(title):
    title = convert(title)
    words = re.findall(r"[\w']+", title)
    for index, word in enumerate(words):
        words[index] = word.lower()
    return "-".join(words)

def cutContent(content):
    clearHtmlTag = re.compile('<.*?>')
    cleanContent = re.sub(clearHtmlTag, '', content)
    try:
        cuttedContent =cleanContent[0:200]
    except BaseException:
        return cleanContent
    lastSpace = cuttedContent.rfind(' ')

    return cuttedContent[0:lastSpace]+'...'
def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(path, filename)

    return wrapper

if __name__ == "__main__":
    print(cutContent('Chỉ là em muốn ôm chặt anh lúc này, giữ chặt anh lúc này, không buông tay. Vậy là kết thúc, ta cũng không thể nào đi chung đôi. Vậy là em sai, sai từ ngay lúc đầu, vì yêu anh quá đậm sâu, để giờ đây nặng mang u sầu. Từng ngày trôi qua là những nỗi đau không phai nhoà. Có dối lòng tỏ ra mạnh mẽ, mà sao trái tim em đau thế này. Dành tất cả thanh xuân để thương một người, giờ chỉ còn là giấc mơ. Thật lòng ngỡ bên nhau trăm năm cớ sao mọi chuyện đi quá xa xăm. Anh đ...'))