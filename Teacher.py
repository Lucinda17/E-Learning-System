class Teacher:
    #initialize variable
    name=""
    username=""
    password=""
    subjects=[]

    class __impl:
        #implementation of Singleton interface
        def spam(self):
            return id(self)
        #Return Singleton instance's ID

        #storage for the instance reference
        __instance=None

    def __init__(self):
        # Check whether we already have an instance
        if Student.__instance is None:
            # Create and remember instance
            Student.__instance = Student.__impl()
        

    def __getattr__(self, attr):
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        return setattr(self.__instance, attr, value)
