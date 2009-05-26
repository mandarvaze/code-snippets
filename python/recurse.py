#!/usr/bin/env python
#
#       recurse.py
#
#       Copyright 2009 Mandar Vaze (mandarvaze@gmail.com)
#
#       Redistribution and use in source and binary forms, with or without
#       modification, are permitted provided that the following conditions are
#       met:
#
#       * Redistributions of source code must retain the above copyright
#         notice, this list of conditions and the following disclaimer.
#       * Redistributions in binary form must reproduce the above
#         copyright notice, this list of conditions and the following disclaimer
#         in the documentation and/or other materials provided with the
#         distribution.
#       * Neither the name of the  nor the names of its
#         contributors may be used to endorse or promote products derived from
#         this software without specific prior written permission.
#
#       THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#       "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#       LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#       A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#       OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#       SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#       LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#       DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#       THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#       (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#       OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Input is a series of different values connected by semi-colon
# Recurse thru the string and generate a list in a global 'retval'
# Needed this as part of an application
# Uploaded to GIT for reference - to myself in future - and others


retval = []

def sepData(input):    
    found = False

    seploc = input.find(';')
    if seploc != -1:
        val = input[0:seploc]
        if len(val):
            retval.append(val)
        if seploc < len(input):
            otherval = input[seploc+1:]
            sepData(otherval)
        return
    if len(input):
        retval.append(input)
    return

def main():
    input = ';123;2314;1231;112233'

    #Other test cases
    # Uncomment as needed, and comment the original :)
    #input = ';'
    #input = '123'
    #input = ';123'
    #input = ';123;2314;1231;112233;'
    #input = '123;2314;1231;112233;'
    
    print 'Initial Value : ' + input + "\n"
    sepData(input)
    values = retval
    print values

if __name__ == '__main__': main()

