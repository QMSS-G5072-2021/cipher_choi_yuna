from cipher_yc4021 import cipher_yc4021
import pytest
def cipher(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
    
def test_cipher_word():
    example = 'Halloween'
    expected = 'MfqqtBjjs'
    actual = cipher(example, 5)
    assert actual == expected
