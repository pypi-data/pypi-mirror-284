# -*- coding: utf-8 -*-
import re
from collections import namedtuple
from common.entity.timeline import Timeline

TIME_SEG = r'[\d半一两二三四五六七八九十]\d{0,3}十?\+?\-?.?[多|年|月|周|天|日|时]\d{0,2}[月|周|天|日]?半?余?\+?前'
PRE_TIME_SEG = r'入院前[\d半一两二三四五六七八九十]\d{0,3}十?\+?\-?.?[多|年|月|周|天|日|时]\d{0,2}[月|周|天|日]?半?余?\+?'
CHINESE_TIME_THESE_DAYS = r'[近昨今当前][天日早晚]'
CHINESE_TIME_SEG = r'[同今去前]年[一二三四五六七八九十]{0,2}\d{0,2}月'
TIME_STAMP = r'(?:\d{4}[年|\-|.|/]\d{1,2}[月|\-|.|/]\d{1,2}日?|\d{4}[年|\-|.|/]\d{1,2}月?|\d{1,2}[月]\d{1,2}日?)'
TIME_RANGE_HALF = r'(?:\d{4}[年|\-|.|/]\d{1,2}[月|\-|.|/]\d{1,2}日?|\d{4}[年|\-|.|/]\d{1,2}月?|\d{1,2}[月|.|\-]\d{1,2}日?)'
SPECIAL_DOT_TIME_STAMP = r'(\d{1,2}[\-|.]\d{1,2}|\d{4})'
ABBR_TIME_STAMP = r'2\d[-.]\d\d[-.]\d\d'
TIME_STAMP_RANGE = TIME_RANGE_HALF + '[-~至]' + TIME_RANGE_HALF
TIME_STAMP_COMPACT = r'20\d{6}'
TIME_STAMP_COMPACT_RANGE = r'\d{4}[-~至]\d{4}'
TIME_YEAR = r'20\d{2}年[初中底末尾终]?'
NOW = r'^[今现为].[2,8]院$'
FROM = r'^.{0,2}自?.{2,6}来$'
MIN_SEG_LEN = 6
BEST_LEN = 15

# 常见的单字和复姓列表
common_surnames = [
    "李", "王", "张", "刘", "陈", "杨", "黄", "赵", "周", "吴",
    "徐", "孙", "马", "朱", "胡", "林", "郭", "何", "高", "罗",
    "郑", "梁", "谢", "宋", "唐", "许", "韩", "冯", "邓", "曹",
    "彭", "曾", "肖", "田", "董", "袁", "潘", "于", "蒋", "蔡",
    "余", "杜", "叶", "程", "苏", "魏", "吕", "丁", "任", "沈",
    "姚", "卢", "姜", "崔", "钟", "谭", "陆", "汪", "范", "金",
    "石", "廖", "贾", "夏", "韦", "傅", "方", "白", "邹", "孟",
    "熊", "秦", "邱", "江", "尹", "薛", "闫", "段", "雷", "侯",
    "龙", "史", "陶", "黎", "贺", "顾", "毛", "郝", "龚", "邵",
    "万", "钱", "严", "赖", "覃", "洪", "武", "莫", "孔", "汤",
    "习", "尤", "苗", "俞", "鲍", "章", "施", "窦", "岑", "乐",
    "成", "詹", "欧阳", "司马", "端木", "上官",  # 复姓
]


def any_match(string, match_list):
    result = []
    for match in match_list:
        if string.find(match) != -1:
            result.append(match)
    return result


def any_match_bool(string, match_list):
    for match in match_list:
        if string.find(match) != -1:
            return True
    return False


def extract_digit(string):
    result = ""
    for ch in string:
        if ch.isdigit():
            result += ch
    return result


def find_all(string, substring):
    positions = []
    start = string.find(substring)

    while start != -1:
        positions.append(start)

        # 更新起始位置为当前子串后面的位置
        start += len(substring)
        next_pos = string[start:].find(substring)
        if next_pos == -1:
            break
        start = next_pos + start

    return positions


# 去掉所有的空格、回车等特殊符号
def remove_special_symbols(string):
    return string.replace("\n", "").replace("\r", "").replace("\b", "").replace("\t", "").replace(" ", "").replace('',
                                                                                                                   '')


def remove_bracket(string):
    return string.replace("(", "").replace(")", "").replace("（", "").replace("）", "")


def has_chinese(sentence):
    for ch in sentence:
        if is_chinese(ch):
            return True
    return False


# ---------------------------功能:判断字符是不是汉字-------------------------------
def is_chinese(char):
    if '\u4e00' <= char <= '\u9fff':
        return True
    return False


def handle_short_sentence(segment_list):
    temp_split_pos_list = []
    i = 0
    while i < len(segment_list) - 1:
        cur_seg_begin, cur_seg_end = segment_list[i]
        next_seg_begin, next_seg_end = segment_list[i + 1]
        if cur_seg_end - cur_seg_begin < BEST_LEN and next_seg_end - next_seg_begin < BEST_LEN:
            temp_split_pos_list.append((cur_seg_begin, next_seg_end))
            i += 2
        else:
            temp_split_pos_list.append((cur_seg_begin, cur_seg_end))
            i += 1
    if i < len(segment_list):
        temp_split_pos_list.append(segment_list[i])
    return temp_split_pos_list


def fetch_text(text, begin, end):
    return text[begin: end]


def fetch_index_and_text(text, begin, end):
    return begin, text[begin: end]


def split_text(text, pattern="。", admission_time=None, fetch_func=fetch_text):
    if text == '-' or text == '——':
        return []
    split_pos_list = []
    begin = 0
    for match in re.finditer(pattern, text):
        pos = match.start()
        split_pos_list.append((begin, pos))
        begin = pos + 1
    split_pos_list.append((begin, len(text)))
    split_text_list = []
    for begin, end in split_pos_list:
        if begin >= end:
            continue
        split_text_list.append(fetch_func(text, begin, end))
    return split_text_list


def locate_two_word(content, word1, word2, keep_order=True):
    word1_index_list = find_all(content, word1)
    word2_index_list = find_all(content, word2)

    if not word1_index_list or not word2_index_list:
        return None

    index_tuple_list = []
    for word1_index in word1_index_list:
        for word2_index in word2_index_list:
            index_tuple_list.append((word1_index, word2_index))

    index_tuple_list.sort(key=lambda ele: abs(ele[0] - ele[1]))
    if keep_order:
        for index_tuple in index_tuple_list:
            if index_tuple[0] < index_tuple[1]:
                return index_tuple
    return index_tuple_list[0]


def cut_from_back_to_front(text, length):
    if length <= len(text):
        return text[-length:]
    return text


def is_chinese_name(name):
    # 正则表达式检查全部为中文字符
    if not re.match(r'^[\u4e00-\u9fa5]+$', name):
        return False

    # 检查名字长度为2到4个汉字
    if len(name) < 2 or len(name) > 4:
        return False

    # 检查是否以常见姓氏开头
    if any(name.startswith(surname) for surname in common_surnames):
        return True

    return False

START_WITH_WORDS = ['', ' ', '患者', '患儿', '病人', '住院期间', '期间']
PREFIX_WORDS = ['于', '(', '（']
FREQUENCY_LIST = ['次', '颗', '个', '粒', '片', '声', '年', '月', '周', '天', '时', '分', '秒', '小', '碗', '瓶', '餐', '万', '千', '百', '串', '点', '椎', '只', '数']
SYMBOL_LIST = [')', ' ', '、', '）', ':', '：', '(', '（', '/']


def search_special_dot_time(seg):
    def locate_by_keywords(text, keywords, locate_func):
        for keyword in keywords:
            pos = locate_func(text, keyword)
            if pos == -1:
                continue
            if pos < len(text) and text[pos].isdigit():
                return keyword, pos
        return None, -1

    keyword, location = locate_by_keywords(seg, START_WITH_WORDS,
                                  lambda text, keyword: len(keyword) if text.startswith(keyword) else -1)
    if location == -1:
        keyword, location = locate_by_keywords(seg, PREFIX_WORDS, lambda text, keyword: text.find(keyword) + len(keyword))
    if location == -1:
        return None
    fragment = seg[location: location + MIN_SEG_LEN]
    match = re.search(SPECIAL_DOT_TIME_STAMP, fragment)

    if not match or match.span()[0] != 0:
        return None
    next_ch_pos = match.span()[1]
    if next_ch_pos < len(fragment):
        next_ch = fragment[next_ch_pos]
        check_flag = False
        if keyword == '(' or keyword == '（':
            if next_ch in SYMBOL_LIST:
                check_flag = True
        else:
            if next_ch in SYMBOL_LIST or (is_chinese(next_ch) and next_ch not in FREQUENCY_LIST):
                check_flag = True

        if not check_flag:
            if (keyword == '' or keyword == ' ') and any_match_bool(seg, ['：', ':']):
                return TimeMatch(location, match.group())
            return None

    return TimeMatch(location, match.group())


TimeMatch = namedtuple('TimeMatch', ['timePos', 'timeText'])


def parse_match(match):
    if match:
        return TimeMatch(match.span()[0], match.group())
    return None


SEARCH_TIME_FUNC_DICT = {
    '时间范围': [
        lambda seg: parse_match(re.search(TIME_STAMP_RANGE, seg)),
        lambda seg: parse_match(re.search(TIME_STAMP_COMPACT_RANGE, seg))
    ],
    '时间戳': [
        lambda seg: parse_match(re.search(TIME_STAMP, seg)),
        lambda seg: parse_match(re.search(TIME_STAMP_COMPACT, seg)),
        search_special_dot_time,
        lambda seg: parse_match(re.search(TIME_YEAR, seg)),
        lambda seg: parse_match(re.search(ABBR_TIME_STAMP, seg))
    ],
    '时间段': [
        lambda seg: parse_match(re.search(TIME_SEG, seg)),
        lambda seg: parse_match(re.search(PRE_TIME_SEG, seg)),
        lambda seg: parse_match(re.search(CHINESE_TIME_THESE_DAYS, seg)),
        lambda seg: parse_match(re.search(CHINESE_TIME_SEG, seg))
    ],
    # '入院时间': [
    #     lambda seg: parse_match(re.search(NOW, seg)),
    # ],
    # '模糊时间': [
    #     lambda seg: parse_match(re.search(FROM, seg)),
    # ]
}


def search_time(seg):
    for time_type, search_time_func_list in SEARCH_TIME_FUNC_DICT.items():
        best_time_match = None
        for search_func in search_time_func_list:
            time_match = search_func(seg)
            if not time_match:
                continue
            if time_match.timePos <= 5:
                return time_type, time_match

            if not best_time_match or time_match.timePos < best_time_match.timePos:
                best_time_match = time_match
        if best_time_match:
            return time_type, best_time_match
    return None, None


def cut_by_time(text, admission_time):
    seg_list = split_text(text, "。|,|，|；|\n", fetch_func=fetch_index_and_text)
    results = []

    for start_index, seg in seg_list:
        last_timeline = results[-1][0] if results else None
        timeline = None
        time_type, time_match = search_time(seg)
        if time_match:
            timeline = Timeline(time_match.timeText, time_type, admission_time, last_timeline)
            timeline.start_index = time_match.timePos + start_index
            timeline.end_index = timeline.start_index + len(time_match.timeText)
            timeline.content = seg
        if timeline and timeline.base_time_convert:
            results.append((timeline, [seg]))
        else:
            if results:
                results[-1][1].append(seg)
            else:
                results.append((None, [seg]))
    return results