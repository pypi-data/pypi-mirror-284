from typing import List

import jieba
import langid
import textstat
from hanziconv import HanziConv

from lanq.model.model import Model
from lanq.model.rule.util import *
from lanq.model.rule.base import BaseRule, ResModel


@Model.rule_register('QUALITY_SIGNAL_FLUENCY', ['zh_all'])
class CommonAntiCrawlerZH(BaseRule):
    threshold = 0.8

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        res = ResModel()
        assert len(input_data) == 1
        line_num = 50
        content_lines = [line.strip() for line in input_data[0].split("\n") if len(line.strip())]
        max_jieba_ratio = 0
        for line in content_lines:
            line = get_real_text(line)
            char_num = len(line)
            word_num = 0
            if len(line) > line_num:
                seg_list = jieba.cut(line, cut_all=True)
                for word in seg_list:
                    if len(word) == 1:
                        word_num += 1
                max_jieba_ratio = max(max_jieba_ratio, word_num / char_num)
        if max_jieba_ratio > cls.threshold:
            res.error_status = True
            res.error_reason = "Contain anti crawling text."
        return res


@Model.rule_register('QUALITY_SIGNAL_COMPLETENESS', ['default'])
class CommonBracketUnmatch(BaseRule):
    """check whether bracket matches"""

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        assert len(input_data) == 1
        res = ResModel()
        bracket_types = [("[", "]"), ("{", "}"), ("【", "】"), ("《", "》")]
        for open_bracket, close_bracket in bracket_types:
            if input_data[0].count(open_bracket) != input_data[0].count(close_bracket):
                res.error_status = True
                res.error_reason = "Number of parentheses is inconsistent."
        return res


@Model.rule_register('QUALITY_SIGNAL_EFFECTIVENESS', ['en_all'])
class CommonChaosEN(BaseRule):
    """check whether content has English messy code"""

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        res = ResModel()
        af_en = delete_punc_en(input_data[0])
        af_ch = delete_punc_ch(af_en)
        str_len = len(af_ch)
        language = langid.classify(input_data[0])[0]
        if language == "en":
            seg_len = len(list(jieba.cut(af_ch)))
            if str_len == 0 or seg_len == 0 or get_tokens(input_data[0], language) < 50:
                return res
            if str_len / seg_len > 1.2:
                return res
            else:
                res.error_status = True
                res.error_reason = 'Contain English garbled characters.'
                return res
        else:
            return res


@Model.rule_register('QUALITY_SIGNAL_EFFECTIVENESS', ['zh_all'])
class CommonChaosSymbol(BaseRule):
    """check whether content has a lot of meaningless words"""
    pattern = r'[0-9a-zA-Z\u4e00-\u9fa5]'

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        assert len(input_data) == 1
        res = ResModel()
        s = re.sub(cls.pattern, '', input_data[0])
        str_len = len(input_data[0])
        symbol_len = len(s)
        if str_len == 0 or symbol_len == 0:
            return res
        if symbol_len / str_len > 0.5:
            res.error_status = True
            res.error_reason = 'Contain a large amount of non textual content.'
        return res


@Model.rule_register('QUALITY_SIGNAL_EFFECTIVENESS', ['zh_all'])
class CommonChaosZH(BaseRule):
    """check whether content has Chinese messy code"""
    pattern = r'[a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ\n\s]'

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        assert len(input_data) == 1
        res = ResModel()
        lan = langid.classify(input_data[0])[0]
        if lan != 'zh':
            return res
        s = normalize(input_data[0])
        s = re.sub(cls.pattern, '', s)
        s_simplified = HanziConv.toSimplified(s)
        str_len = len(s)
        seg_len = len(list(jieba.cut(s_simplified)))
        num_bytes = len(input_data[0].encode('utf-8'))
        tokens_len = int(num_bytes * 0.248)
        if str_len == 0 or seg_len == 0 or tokens_len < 50:
            return res
        if str_len / seg_len <= 1.1:
            res.error_status = True
            res.error_reason = 'Contain Chinese garbled characters.'
        return res


@Model.rule_register('QUALITY_SIGNAL_UNDERSTANDABILITY', ['default'])
class CommonCheckPhoto(BaseRule):
    """check whether content has photo"""
    pattern = '!\[\]\(http[s]?://.*?jpeg "\n"\)'  # noqa F402

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        assert len(input_data) == 1
        res = ResModel()
        matches = re.findall(cls.pattern, input_data[0])
        if matches:
            res.error_status = True
            res.error_reason = matches
        return res


@Model.rule_register('QUALITY_SIGNAL_COMPLETENESS', ['default'])
class CommonColonEnd(BaseRule):
    """check whether the last char is ':'"""

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        assert len(input_data) == 1
        res = ResModel()
        if len(input_data[0]) <= 0:
            return res
        if input_data[0][-1] == ':':
            res.error_status = True
            res.error_reason = 'Ends with a colon.'
        return res


@Model.rule_register('QUALITY_SIGNAL_EFFECTIVENESS', ['default'])
class CommonContentNull(BaseRule):
    """check whether content is null"""

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        assert len(input_data) == 1
        res = ResModel()
        count = len(input_data[0].strip())
        if count == 0:
            res.error_status = True
            res.error_reason = 'Content is empty.'
        return res


@Model.rule_register('QUALITY_SIGNAL_SIMILARITY', ['default'])
class CommonDocRepeat(BaseRule):
    """check whether content repeats"""

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        assert len(input_data) == 1
        res = ResModel()
        repeat_score = base_rps_frac_chars_in_dupe_ngrams(6, input_data[0])
        if repeat_score >= 80:
            res.error_status = True
            res.error_reason = 'Repeatability of text is too high, with ratio： ' + str(repeat_score)
        return res


@Model.rule_register('QUALITY_SIGNAL_UNDERSTANDABILITY', ['zh_all'])
class CommonEllipsisRatio(BaseRule):
    """check whether ratio of line end with ellipsis is bigger than 75%"""

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        assert len(input_data) == 1
        res = ResModel()
        lines = input_data[0].split("\n")
        non_empty_lines = 0
        ellipsis_lines = 0
        for line in lines:
            if line.strip() != "":
                non_empty_lines += 1
                if (
                        line.strip().endswith("。。。")
                        or line.strip().endswith("…")
                        or line.strip().endswith("。。。。。。")
                        or line.strip().endswith("……")
                ):
                    ellipsis_lines += 1
        if non_empty_lines != 0:
            ellipsis_ratio = ellipsis_lines / non_empty_lines
            if ellipsis_ratio > 0.75:
                res.error_status = True
                res.error_reason = "Proportion of ellipsis ending lines exceeds 75%."
        return res


@Model.rule_register('QUALITY_SIGNAL_UNDERSTANDABILITY', ['zh_all'])
class CommonEmojiCharacters(BaseRule):
    """check whether content contains emoji characters"""
    pattern = r"U\+26[0-F][0-D]|U\+273[3-4]|U\+1F[3-6][0-4][0-F]|U\+1F6[8-F][0-F]"

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        assert len(input_data) == 1
        res = ResModel()
        matches = re.search(cls.pattern, input_data[0])
        if matches:
            res.error_status = True
            res.error_reason = "Contains emoji symbols."
        return res


@Model.rule_register('QUALITY_SIGNAL_UNDERSTANDABILITY', ['default'])
class CommonEnterMore(BaseRule):
    """check whether content has more than 8 continuous enter"""
    pattern = r'\n{8,}|\r{8,}'

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        assert len(input_data) == 1
        res = ResModel()
        matches = re.findall(cls.pattern, input_data[0])
        if matches:
            res.error_status = True
            res.error_reason = 'Contain 8 continuous enter.'
        return res


@Model.rule_register('QUALITY_SIGNAL_UNDERSTANDABILITY', ['default'])
class CommonEnterRatioMore(BaseRule):
    """check whether enter / content is more than 25%"""

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        assert len(input_data) == 1
        res = ResModel()
        enter_count = input_data[0].count('\n')
        count = len(input_data[0])
        if count == 0:
            return res
        ratio = enter_count / count * 100
        if ratio >= 25:
            res.error_status = True
            res.error_reason = 'Enter exceeds 25% of text.'
        return res


@Model.rule_register('QUALITY_SIGNAL_UNDERSTANDABILITY', ['default'])
class CommonHtmlEntity(BaseRule):
    """check whether content has html entity"""

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        assert len(input_data) == 1
        res = ResModel()
        entities = [
            "nbsp",
            "lt",
            "gt",
            "amp",
            "quot",
            "apos",
            "hellip",
            "ndash",
            "mdash",
            "lsquo",
            "rsquo",
            "ldquo",
            "rdquo",
        ]
        full_entities_1 = [f"&{entity}；" for entity in entities]
        full_entities_2 = [f"&{entity};" for entity in entities]
        full_entities_3 = [f"＆{entity};" for entity in entities]
        full_entities_4 = [f"＆{entity}；" for entity in entities]
        full_entities = (
                full_entities_1 + full_entities_2 + full_entities_3 + full_entities_4
        )
        # half_entity_1 = [f"{entity}；" for entity in entities]
        half_entity_2 = [f"＆{entity}" for entity in entities]
        half_entity_3 = [f"&{entity}" for entity in entities]
        # half_entity_4 = [f"{entity};" for entity in entities]
        half_entities = half_entity_2 + half_entity_3
        # maked_entities = [f"{entity}" for entity in entities]
        all_entities = full_entities + half_entities

        pattern = '|'.join(all_entities)
        matches = re.findall(pattern, input_data[0])
        if matches:
            res.error_status = True
            res.error_reason = matches
        return res


@Model.rule_register('QUALITY_SIGNAL_UNDERSTANDABILITY', ['default'])
class CommonImgHtmlTag(BaseRule):
    """check whether content has img or html tag"""
    pattern = r"(<img[^>]*>)|<p[^>]*>(.*?)<\/p>|<o:p[^>]*>(.*?)<\/o:p>"

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        assert len(input_data) == 1
        res = ResModel()
        matches = re.findall(cls.pattern, input_data[0])
        if matches:
            res.error_status = True
            res.error_reason = matches
        return res


@Model.rule_register('QUALITY_SIGNAL_EFFECTIVENESS', ['zh_all'])
class CommonInvalidWeb(BaseRule):
    """check whether the content is invalid"""

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        assert len(input_data) == 1
        res = ResModel()
        invalid_list = [
            "404 - Page not found\nThe requested page does not exist (or has been deleted).\nIf you typed a" +
            " URL by hand, or used a bookmark, please double check the address that you used.\nIf you see this " +
            "page, and the error persists, please contact Customer Care and provide details about the action you " +
            "tried to perform."]
        for item in invalid_list:
            if item in input_data[0]:
                res.error_status = True
                res.error_reason = "Content is 404."
        return res


@Model.rule_register('QUALITY_SIGNAL_UNDERSTANDABILITY', ['default'])
class CommonInvisibleChar(BaseRule):
    """check whether content has invisible char"""
    pattern = r"[\u2000-\u200F\u202F\u205F\u3000\uFEFF\u00A0\u2060-\u206F\uFEFF\xa0]"

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        assert len(input_data) == 1
        res = ResModel()
        matches = re.findall(cls.pattern, input_data[0])
        if matches:
            res.error_status = True
            res.error_reason = matches
        return res


@Model.rule_register('QUALITY_SIGNAL_UNDERSTANDABILITY', ['zh_all'])
class CommonJointSpecialSymbol(BaseRule):
    """check if there are special symbols composed of multiple symbols spliced together"""
    pattern = r"&#247;|\? :"

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        assert len(input_data) == 1
        res = ResModel()
        matches = re.findall(cls.pattern, input_data[0])
        if matches:
            res.error_status = True
            res.error_reason = "Contain special symbol composed of multiple symbols."
        return res


@Model.rule_register('QUALITY_SIGNAL_EFFECTIVENESS', [])
class CommonLanguageMixed(BaseRule):
    """check whether content is mixed in Chinese and English"""

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        assert len(input_data) == 1
        res = ResModel()
        s = normalize(input_data[0])
        en_len = len(re.findall(r'[a-zA-Z]', s))
        zh_len = len(re.findall(r'[\u4e00-\u9fa5]', s))
        count_len = len(s)
        if count_len == 0:
            return res
        if en_len / count_len >= 0.5 and zh_len / count_len >= 0.1:
            res.error_status = True
            res.error_reason = 'Mixed Chinese and English.'
        return res


@Model.rule_register('QUALITY_SIGNAL_SECURITY', ['zh_all'])
class CommonLicenseKey(BaseRule):
    """check if the content contains license key"""
    pattern = r"(License|破解)|" + "|".join([
        "[A-Z0-9]{47}",
        "[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}",
        "[A-Z0-9]{4}-\d{8}-[A-Z0-9]{4}"
    ])

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        assert len(input_data) == 1
        res = ResModel()
        match = re.search(cls.pattern, input_data[0], re.I)
        if match:
            res.error_status = True
            res.error_reason = "Contain license key."
        return res


@Model.rule_register('QUALITY_SIGNAL_FLUENCY', ['en_all'])
class CommonNoPunc(BaseRule):
    """check whether content has paragraph without punctuations"""

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        assert len(input_data) == 1
        res = ResModel()
        paragraphs = input_data[0].split('\n')
        max_word_count = 0
        for paragraph in paragraphs:
            if len(paragraph) == 0:
                continue
            sentences = re.split(r'[-–.!?,;•、。！？，；·]', paragraph)
            for sentence in sentences:
                words = sentence.split()
                word_count = len(words)
                if word_count > max_word_count:
                    max_word_count = word_count
        text_stat_res = textstat.flesch_reading_ease(input_data[0])
        if int(max_word_count) > 56 and text_stat_res < 20:
            res.error_status = True
            res.error_reason = 'Paragraph without punctuation.'
        return res


@Model.rule_register('QUALITY_SIGNAL_UNDERSTANDABILITY', ['default'])
class CommonSpaceMore(BaseRule):
    """check whether content has more than 500 consecutive spaces"""
    pattern = r' {500,}'

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        assert len(input_data) == 1
        res = ResModel()
        matches = re.findall(cls.pattern, input_data[0])
        if matches:
            res.error_status = True
            res.error_reason = 'Contain 500 consecutive spaces.'
        return res


@Model.rule_register('QUALITY_SIGNAL_UNDERSTANDABILITY', ['default'])
class CommonSpecialCharacter(BaseRule):
    pattern = r"[�□]|\{\/U\}"

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        assert len(input_data) == 1
        res = ResModel()
        matches = re.findall(cls.pattern, input_data[0])
        if matches:
            res.error_status = True
            res.error_reason = matches
        return res


@Model.rule_register('QUALITY_SIGNAL_UNDERSTANDABILITY', ['zh_all'])
class CommonSpecialMark(BaseRule):
    """check if the content contains special mark"""
    pattern = r'keyboard_arrow_(left|right)'

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        assert len(input_data) == 1
        res = ResModel()
        matches = re.findall(cls.pattern, input_data[0])
        if matches:
            res.error_status = True
            res.error_reason = "Contain special element tags"
        return res


@Model.rule_register('QUALITY_SIGNAL_UNDERSTANDABILITY', ['zh_all'])
class CommonUnconvertedSymbol(BaseRule):
    """check if the content contains special symbols for conversion failure"""
    pattern = r'u200e'

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        assert len(input_data) == 1
        res = ResModel()
        matches = re.findall(cls.pattern, input_data[0])
        if matches:
            res.error_status = True
            res.error_reason = "Contain special symbols for conversion failure."
        return res


@Model.rule_register('QUALITY_SIGNAL_SIMILARITY', ['zh_all'])
class CommonUnderscoreLength(BaseRule):
    """check whether the content contains underscores whose length is longer than 15"""

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        assert len(input_data) == 1
        res = ResModel()
        max_underscore_count = 0
        for char in input_data[0]:
            if char == '_':
                underscore_count += 1
                if underscore_count > max_underscore_count:
                    max_underscore_count = underscore_count
            else:
                underscore_count = 0
        if max_underscore_count >= 15:
            res.error_status = True
            res.error_reason = "The length of the underline is greater than 15."
        return res


@Model.rule_register('QUALITY_SIGNAL_EFFECTIVENESS', ['default'])
class CommonUrlOnly(BaseRule):
    """check whether content is all urls"""
    pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'  # noqa

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        assert len(input_data) == 1
        res = ResModel()
        if len(input_data[0].strip()) == 0:
            return res

        s = re.sub(cls.pattern, '', input_data[0])
        count = len(s.strip())
        if count == 0:
            res.error_status = True
            res.error_reason = 'Content only has URL.'
        return res


@Model.rule_register('QUALITY_SIGNAL_FLUENCY', ['en_all'])
class CommonWordStuck(BaseRule):
    """check whether words are stuck"""

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        assert len(input_data) == 1
        res = ResModel()
        words = re.findall(r'[a-zA-Z]+', input_data[0])
        max_word_len = 0
        for word in words:
            if len(word) > max_word_len:
                max_word_len = len(word)
        if max_word_len > 45:
            res.error_status = True
            res.error_reason = 'English words are stuck.'
        return res

@Model.rule_register("QUALITY_SIGNAL_RELEVANCE", [])
class CommonWatermark(BaseRule):
    """check whether english prompt produce chinese prediction"""
    key_list = []

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        res = ResModel()
        assert len(input_data) == 1
        matches = re.findall('|'.join(cls.key_list), input_data[0])
        if matches:
            res.error_status = True
            res.error_reason = matches
        return res

@Model.rule_register('QUALITY_SIGNAL_RELEVANCE', [])
class CommonAdvertisement(BaseRule):
    """check whether content has advertisement"""
    key_list = ['deadlinesOrder', 'Kindly click on ORDER NOW to receive an']

    @classmethod
    def eval(cls, input_data: List[str]) -> ResModel:
        res = ResModel()
        matches = re.findall('|'.join(cls.key_list), input_data[0])
        if matches:
            res.error_status = True
            res.error_reason = matches
        return res