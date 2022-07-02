class Super:
    var1 = None     # public data member
    _var2 = None    # protected data member
    __var3 = None   # private data member

    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

    def _displayProtectedMembers(self):
        print("Protected Data Member: ", self._var2)    # accessing protected data members

    def __displayPrivateMembers(self):
        print("Private Data Member: ", self.__var3)     # accessing private data members

    def accessPrivateMembersParent(self):
        print("Private Data Member Parent: ", self.__var3)
        self.__displayPrivateMembers()      # accessing private data members parent

    def accessProtectedMembersParent(self):
        print("Protected Data Member Parent: ", self._var2)
        self._displayProtectedMembers()     # accessing protected data members parent

    def displayPublicMembersParent(self):
        print("Public Data Member: ", self.var1)    # accessing public data members


class Sub(Super):
    def __init__(self, var1, var2, var3):
        Super.__init__(self, var1, var2, var3)

    def accessProtectedMembers(self):
        self._displayProtectedMembers()     # accessing protected member functions of super class

    # def accessPrivateMembers(self):
    #     self.__displayPrivateMembers()      # Throws attribute error while accessing private func

obj = Sub("Geeks", 4, "Geeks !")

obj.displayPublicMembersParent()
obj.accessProtectedMembersParent()
obj.accessPrivateMembersParent()
obj.accessProtectedMembers()
# obj.accessPrivateMembers()    # Throws attribute error


print("accessing public member:", obj.var1)
print("accessing protected member:", obj._var2)   # Object can access protected member
# print(obj.__var3)    # object can not access private member, so it will generate Attribute error