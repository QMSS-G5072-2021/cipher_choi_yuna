from cipher_yc4021 import cipher_yc4021
    
def test_cipher_word():
    example = 'Halloween'
    expected = 'MfqqtBjjs'
    actual = cipher(example, 5)
    assert actual == expected
