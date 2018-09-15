class Student:

    class __impl:
        # Implementation of the singleton interface
        def spam(self):
            return id(self)

    # storage for the instance reference
    __instance = None

    def __init__(self):
        # Check whether we already have an instance
        if Student.__instance is None:
            # Create and rememeber instance
            Student.__instance = Student.__impl()
        

    def __getattr__(self, attr):
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        return setattr(self.__instance, attr, value)

    def setUsername(self,username):
        self.username = username