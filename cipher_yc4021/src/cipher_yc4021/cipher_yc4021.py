def cipher(text, shift, encrypt=True):
    """
    Concatenates two pandas categoricals.

    Parameters
    ----------
    text : str
      The text that will be encrypted/decrypted.
    shift : int
      The number of positions you move right or lift. 
     encrypt : bool
      A boolean that defines whether you are encrypting or decrypting text. 

    Returns
    -------
    str
      The ending result will be a string. 

    Examples
    --------
    >>> from cipher_yc4021 import cipher_yc4021
    >>> text = 'Halloween'
    >>> shift = 5
    >>> cipher(text, shift, encrypt = True)
    'MfqqtBjjs'
    >>> from cipher_yc4021 import cipher_yc4021
    >>> text = 'gzssD'
    >>> shift = 5
    >>> cipher(text, shift, encrypt = False)
    'bunny'
    """
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
