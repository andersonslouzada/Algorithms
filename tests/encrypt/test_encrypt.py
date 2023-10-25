import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(1, 'abcdef')

    assert encrypt_message('abcdef', 0) == 'fedcba'
    assert encrypt_message('abcdef', 1) == 'a_fedcb'
    assert encrypt_message('abcdef', 2) == 'fedc_ba'
    assert encrypt_message('abcdef', 3) == 'cba_fed'
    assert encrypt_message('abcdef', 4) == 'fe_dcba'
    assert encrypt_message('abcdef', 5) == 'edcba_f'
