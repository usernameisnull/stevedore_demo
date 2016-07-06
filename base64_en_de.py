# encoding: utf-8
"""
    把一个zip文件通过base64.encode变成一段字符串，
    再通过base64.decode变回zip文件
    受到get_pip。py的启发，get_pip.py是用的b85编码
    但是因为这个只有py3才有，这里用的py2，所以用b64
"""
import base64
import os


def simple_formatter(source, each_line_characters=79, separator='\n'):
    """
    用于把zip文件编码出来的字符串进行格式化输出
    :param each_line_characters: 每一行的字符数
    :param source: 原始字符串
    :param separator: 分隔符
    :return: 字符串
    """
    start = 0
    end = each_line_characters
    length = len(source)
    result = []
    while end < length + each_line_characters:
        result.append(source[start: end])
        start += each_line_characters
        end += each_line_characters
    return separator.join(result)


def encode_zip_to_string(file_path):
    """
    把zip文件转为一段字符串
    :param file_path: 文件所在的位置，包括文件名
    :return: 字符串
    """
    if not os.path.exists(file_path):
        raise Exception("%s not exists!" % file_path)
    with open(file_path, 'rb') as f:
        binary_out = f.read()
    return base64.b64encode(binary_out)


def decode_string_to_zip(s, sep, sep_to, zip_path):
    """
    将字符串转为zip文件
    :param s: 字符串
    :param zip_path: 生成的zip文件位置
    :param sep: s中包含的分隔符
    :param sep_to: 将s中的分隔符替换为sep_to
    :return:
    """
    # if not os.path.exists(zip_path):
    #     raise Exception("%s not exists " % zip_path)
    try:
        with open(zip_path, 'wb') as f:
            f.write(base64.b64decode(s.replace(sep, sep_to)))
    except Exception as exc_info:
        print '*'*80
        print ("Error when generate zip file, detail: %s" % str(exc_info))
        print '*'*80
        return

if __name__ == '__main__':
    out_str = simple_formatter(encode_zip_to_string('scheduler.zip'))
    print out_str
    decode_string_to_zip(out_str, '\n', '', 'algorithm/scheduler.zip')



