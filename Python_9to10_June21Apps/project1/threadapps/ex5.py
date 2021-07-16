from threading import  Thread
class A(Thread):
    def run(self):
        if self.isDaemon():
            print('Daemon thread is running')
        else:
            print('Foreground thread is running')

ob1=A()
ob2=A()
ob1.setDaemon(True)
ob1.start()
ob2.start()