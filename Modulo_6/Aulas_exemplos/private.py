class MyClass:
    def method1(self) -> None:
        print("method1")
        self.__method2()
    def __method2(self) -> None:
        print("method2")
