from typing import Any


class Registers:
    def __init__(self, ports: int = 1):
        self.AR = 0
        self.IP = 0
        self.IO = 0
        self.Ports = [0 for i in range(ports)]
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass
    def AR_write(self, value: int):
        self.AR = value
    def IP_write(self, value: int):
        self.IP = value
    def IO_write(self, value: int):
        self.IO = value
    
        
def test_registers():
    r = Registers()
    assert r.AR == 0
    assert r.IP == 0
    assert r.IO == 0
    r.AR_write(1)
    assert r.AR == 1
    r.IP_write(2)
    assert r.IP == 2
    r.IO_write(3)
    assert r.IO == 3
