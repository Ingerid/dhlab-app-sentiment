import pytest
import dhlab as dh
from sentiment import count_and_score_target_words

@pytest.fixture
def dummy_corpus():
    urnlist = [
        "URN:NBN:no-nb_digavis_nordhordland_null_null_20100120_37_6_1",
        "URN:NBN:no-nb_digavis_aandalsnesavis_null_null_20080429_83_49_1",
        "URN:NBN:no-nb_digavis_tidenskrav_null_null_20010302_92_52_1",
        "URN:NBN:no-nb_digavis_tronderavisa_null_null_19961114_0_264_1",
        "URN:NBN:no-nb_digavis_hamararbeiderblad_null_null_19850530_61_120_1",
        "URN:NBN:no-nb_digavis_aftenposten_null_null_19820505_123_201_1"
    ]
    corpus = dh.Corpus.from_identifiers(urnlist)
    return corpus


def test_count_and_score_target_words(dummy_corpus):
    # given
    word = "tannlege"
    # when
    result = count_and_score_target_words(dummy_corpus, word)
    # then
    assert "sentimentscore" in result.columns

