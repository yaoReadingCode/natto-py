# -*- coding: utf-8 -*-
'''Internal-use functions for string- and byte-conversion for supporting Python
2 and 3.'''
import re
import sys

REGEXTYPE = type(re.compile(''))

def string_support(py3enc):
    '''Create byte-to-string and string-to-byte conversion functions for
    internal use.

    :param py3enc: Encoding used by Python 3 environment.
    :type py3enc: str
    '''
    if sys.version < '3':
        def bytes2str(b):
            '''Identity, returns the argument string (bytes).'''
            return b
        def str2bytes(s):
            '''Identity, returns the argument string (bytes).'''
            return s
    else:
        def bytes2str(b):
            '''Transforms bytes into string (Unicode).'''
            return b.decode(py3enc)
        def str2bytes(u):
            '''Transforms Unicode into string (bytes).'''
            return u.encode(py3enc)
    return (bytes2str, str2bytes)
    
def re_unicode_support(py2enc):
    '''Create byte-to-Unicode and Unicode-to-byte conversion functions for
    use in tokenizing text in boundary constraint parsing.

    :param py2enc: Encoding used by Python 2 environment.
    :type py2enc: str
    '''
    if sys.version < '3':
        def sentence2unicode(patt, sentence):
            '''Decodes sentence (str) as Unicode, as needed.'''
            if REGEXTYPE == type(patt) and (patt.flags & re.U):
                return sentence.decode(py2enc)
            else:
                return sentence
        def token2str(patt):
            '''Defines post-processing function as needed.'''
            if REGEXTYPE == type(patt) and (patt.flags & re.U):
                def _fn(token):
                    '''Transforms Unicode token into string (bytes).'''
                    return token.encode(py2enc)
            else:
                def _fn(token):
                    '''Identity. Returns the str token.'''
                    return token
            return _fn
    else:
        def sentence2unicode(patt, sentence):
            '''Identity, returns the argument sentence.'''
            return sentence
        def token2str(patt):
            '''Defines Identity function.'''
            def _fn(token):
                '''Identity. Returns the str token.'''
                return token
            return _fn
    return (sentence2unicode, token2str)

'''
Copyright (c) 2015, Brooke M. Fujita.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

 * Redistributions of source code must retain the above
   copyright notice, this list of conditions and the
   following disclaimer.

 * Redistributions in binary form must reproduce the above
   copyright notice, this list of conditions and the
   following disclaimer in the documentation and/or other
   materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''
