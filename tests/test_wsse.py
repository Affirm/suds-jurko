# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the (LGPL) GNU Lesser General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library Lesser General Public License for more details at
# ( http://www.gnu.org/licenses/lgpl.html ).
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
# written by: Jurko Gospodnetić ( jurko.gospodnetic@pke.hr )

"""
Implemented using the 'pytest' testing framework.
"""

if __name__ == "__main__":
    import __init__
    __init__.runUsingPyTest(globals())


from suds.wsse import UsernameToken


class TestUsernameToken:

    username_token = None

    def setup(self):
        self.username_token = UsernameToken(
            username=b"foouser",
            password=b"barpasswd",
        )

    def test_setnonce_null(self):
        self.setup()
        self.username_token.setnonce()
        assert self.username_token.nonce != None

    def test_setnonce_text(self):
        self.setup()
        self.username_token.setnonce(b"affirm")
        assert self.username_token.nonce == b"affirm"
