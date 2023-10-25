import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(1, 'Anderson')

    assert encrypt_message('Anderson', 0) == 'nosrednA'
    assert encrypt_message('Anderson', 1) == 'A_nosredn'
    assert encrypt_message('Anderson', 2) == 'nosred_nA'
    assert encrypt_message('Anderson', 3) == 'dnA_nosre'
    assert encrypt_message('Anderson', 4) == 'nosr_ednA'
    assert encrypt_message('Anderson', 5) == 'rednA_nos'
    assert encrypt_message('Anderson', 6) == 'no_srednA'
    assert encrypt_message('Anderson', 7) == 'osrednA_n'
