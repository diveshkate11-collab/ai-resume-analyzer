from app.ai_engine.ats.section_checker import SectionChecker
from app.ai_engine.ats.keyword_matcher import KeywordMatcher
from app.ai_engine.ats.formatting_checker import FormattingChecker
from app.ai_engine.ats.grammar_checker import GrammarChecker


class ATSScorer:
    """
    Calculates ATS score.
    """

    @staticmethod
    def calculate(text: str) -> dict:

        section = SectionChecker.check(text)
        keywords = KeywordMatcher.match(text)
        formatting = FormattingChecker.check(text)
        grammar = GrammarChecker.check(text)

        score = 0

        # Sections (40 Marks)
        score += sum(section.values()) * 10

        # Keywords (30 Marks)
        score += min(keywords["count"] * 5, 30)

        # Formatting (20 Marks)
        if not formatting["empty"]:
            score += 10

        if not formatting["too_short"]:
            score += 10

        # Grammar (10 Marks)
        score += grammar["grammar_score"] // 10

        return {
            "ats_score": score,
            "section": section,
            "keywords": keywords,
            "formatting": formatting,
            "grammar": grammar,
        }