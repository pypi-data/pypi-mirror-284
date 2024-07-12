import pymodbus.framer

from gravity_controller_operator.controllers_super import ControllerInterface, \
    RelayControllerInterface
from pymodbus.client import ModbusSerialClient
from pymodbus import Framer
from abc import abstractmethod


class WBMR6LVControllerABC(ControllerInterface):
    controller = None
    slave_id = None

    def get_phys_dict(self, *args, **kwargs):
        """ Получить состояние входов или выходов с контроллера.
        Перед возвратом привести в вид словаря,
        где ключ - это номер реле или di, значение - 0 или 1.
        """
        controller_response = self.get_phys_points_states()
        if "error" in controller_response:
            return controller_response
        response_dict = {i: x for i, x in enumerate(controller_response)}
        return response_dict

    @abstractmethod
    def get_phys_points_states(self):
        return []


class WBMR6LVControllerDI(WBMR6LVControllerABC):
    map_keys_amount = 7
    starts_with = 0
    spec_addr = {0: 7, 1: 0, 2: 1, 3: 0, 4: 3, 5: 4, 6: 5}

    def __init__(self, controller, slave_id):
        self.controller = controller
        self.slave_id = slave_id
        self.init_dict()
        self.update_dict()

    def get_phys_points_states(self):
        response = None
        while not response:
            response = self.controller.read_discrete_inputs(
                self.starts_with, self.map_keys_amount,
                slave=self.slave_id).bits
            # if not response:
            #    response = {"error": "None response from controller"}
        return response


class WBMR6LVControllerRelay(WBMR6LVControllerABC, RelayControllerInterface):
    map_keys_amount = 6
    starts_with = 0

    def __init__(self, controller, slave_id):
        self.controller = controller
        self.slave_id = slave_id
        self.init_dict()
        self.update_dict()

    def get_phys_points_states(self):
        list_l = []
        for i in range(self.map_keys_amount):
            response = None
            while not response:
                response = self.controller.read_coils(
                    self.starts_with, self.map_keys_amount,
                    slave=self.slave_id).bits
            list_l.append(response[0])
        return list_l

    def change_phys_relay_state(self, num, state: bool):
        res = self.controller.write_coil(num, state)
        while not res:
            res = self.controller.write_coil(num, state, slave=self.slave_id)


class WBMR6LV:
    model = "wb_mr6lv"

    def __init__(self, device, slave_id, baudrate=9600, stopbits=2, bytesize=8,
                 name="WBMR6LV"):
        self.controller_interface = ModbusSerialClient(
            device,
            framer=Framer.RTU,
            baudrate=baudrate,
            stopbits=stopbits,
            bytesize=bytesize,
        )
        self.relay_interface = WBMR6LVControllerRelay(
            self.controller_interface,
            slave_id=slave_id)
        self.di_interface = WBMR6LVControllerDI(
            self.controller_interface,
            slave_id=slave_id)
