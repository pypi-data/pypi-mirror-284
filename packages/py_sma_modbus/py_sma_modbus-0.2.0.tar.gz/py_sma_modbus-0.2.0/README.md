# py-sma-modbus

This project is based on [maluramichael py-sma-modbus](https://github.com/maluramichael/py-sma-modbus) and [StefanLSA py-sma-modbus2](https://github.com/StefanLSA/py-sma-modbus2) with the goal to make it more slim and available as a package.

If you prefer to use the functionality through a cli, I encourage you to use one of the above mentioned projects.
This implementation is intended to be used as part of a larger code-base.

The solution is tested on my local sma inverter for some registers.
I cannot guarantee full functionality and use this package, as always, on your own risk.

## Example

```python
from py_sma_modbus.modbus import Modbus
from py_sma_modbus.registers import Register

wr = Modbus(ipAdress="ip-address of the inverter, e.g. 192.168.178.12", ipPort=502, modbusUnit=3)

wr.poll_register(30535)
wr.poll_register(30531)

responses: list[Register] = wr.run()

for response in responses:
    print(response.value)
```
