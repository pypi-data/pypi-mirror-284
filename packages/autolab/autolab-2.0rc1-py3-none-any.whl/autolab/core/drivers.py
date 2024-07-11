# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:38:15 2019

@author: qchat
"""
import os
import sys
import inspect
import importlib
from typing import Type, List
from types import ModuleType

from . import paths, server


# =============================================================================
# DRIVERS INSTANTIATION
# =============================================================================

def get_driver(driver_name: str, connection: str, **kwargs) -> Type:
    ''' Returns a driver instance using configuration provided in kwargs '''
    if driver_name == 'autolab_server':
        driver_instance = server.Driver_REMOTE(**kwargs)
    else:
        assert driver_name in list_drivers(), f"Driver {driver_name} not found in autolab's drivers"
        driver_lib = load_driver_lib(driver_name)
        driver_instance = get_connection_class(driver_lib, connection)(**kwargs)

    return driver_instance


def load_driver_lib(driver_name: str) -> ModuleType:
    ''' Returns a driver library that contains Driver, Driver_XXX, Module_XXX '''
    # Loading preparation
    driver_path = get_driver_path(driver_name)

    # Laod library
    driver_lib = load_lib(driver_path)

    return driver_lib


def load_lib(lib_path: str) -> ModuleType:
    ''' Return an instance of the python script located at lib_path '''
    lib_name = os.path.basename(lib_path).split('.')[0]

    # Save current working directory path
    curr_dir = os.getcwd()

    # Go to the driver's directory (in case it contains absolute imports)
    os.chdir(os.path.dirname(lib_path))

    # Load the module
    spec = importlib.util.spec_from_file_location(lib_name, lib_path)
    lib = importlib.util.module_from_spec(spec)

    # Come back to previous working directory
    os.chdir(curr_dir)

    spec.loader.exec_module(lib)

    return lib


def load_driver_utilities_lib(driver_utilities_name: str) -> ModuleType:
    ''' Returns a driver library that contains Driver, Driver_XXX, Module_XXX '''
    # Loading preparation
    if os.path.exists(driver_utilities_name):
        driver_path = get_driver_path(driver_utilities_name.replace('_utilities', ''))
    else:
        driver_path = os.path.join(paths.AUTOLAB_FOLDER, 'core', 'default_driver.py')

    # Load library
    driver_lib = load_utilities_lib(driver_path)

    return driver_lib


def load_utilities_lib(lib_path: str) -> ModuleType:
    ''' Return an instance of the python script located at lib_path '''
    lib_name = os.path.basename(lib_path).split('.')[0]

    # Save current working directory path
    curr_dir = os.getcwd()

    # Go to the driver's directory (in case it contains absolute imports)
    os.chdir(os.path.dirname(lib_path))

    # Load the module
    lib_name = lib_name + '_utilities'
    spec = importlib.util.spec_from_file_location(
        lib_name, os.path.join(os.path.dirname(lib_path), f'{lib_name}.py'))
    lib = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(lib)

    # Come back to previous working directory
    os.chdir(curr_dir)

    return lib


# =============================================================================
# DRIVERS LIST HELP
# =============================================================================

def list_drivers() -> List[str]:
    ''' Returns the list of available drivers '''
    # To be sure that the list is up to date
    update_drivers_paths()
    return sorted(list(DRIVERS_PATHS))


# =============================================================================
# DRIVERS INSPECTION
# =============================================================================

def get_module_names(driver_lib: ModuleType) -> List[str]:
    ''' Returns the list of the driver's Module(s) name(s) (classes Module_XXX) '''
    return [name.split('_')[1]
            for name, obj in inspect.getmembers(driver_lib, inspect.isclass)
            if obj.__module__ is driver_lib.__name__
            and name.startswith('Module_')]


def get_connection_names(driver_lib: ModuleType) -> List[str]:
    ''' Returns the list of the driver's connection types (classes Driver_XXX) '''
    return [name.split('_')[1]
            for name, obj in inspect.getmembers(driver_lib, inspect.isclass)
            if obj.__module__ is driver_lib.__name__
            and name.startswith('Driver_')]


def get_driver_category(driver_name: str) -> str:
    ''' Returns the driver's category from class Driver '''
    for filename in ('', '_utilities'):

        driver_utilities_path = os.path.join(
            os.path.dirname(get_driver_path(driver_name)), f'{driver_name}{filename}.py')
        category = 'Unknown'

        if os.path.exists(driver_utilities_path):
            try:
                driver_utilities = load_lib(driver_utilities_path)
            except Exception as e:
                print(f"Can't load {driver_name}: {e}", file=sys.stderr)
            else:
                if hasattr(driver_utilities, 'category'):
                    category = driver_utilities.category
                    break

    return category


def get_driver_class(driver_lib: ModuleType) -> Type:
    ''' Returns the class Driver of the provided driver library '''
    assert hasattr(driver_lib, 'Driver'), f"Class Driver missing in driver {driver_lib.__name__}"
    assert inspect.isclass(driver_lib.Driver), f"Class Driver missing in driver {driver_lib.__name__}"
    return driver_lib.Driver


def get_connection_class(driver_lib: ModuleType, connection: str) -> Type:
    ''' Returns the class Driver_XXX of the provided driver library and connection type '''
    if connection in get_connection_names(driver_lib):
        return getattr(driver_lib, f'Driver_{connection}')

    driver_instance = create_default_driver_conn(driver_lib, connection)
    if driver_instance is not None:
        print(f'Warning, {connection} not find in {driver_lib.__name__} but will try to connect using default connection')
        return driver_instance

    assert connection in get_connection_names(driver_lib), f"Invalid connection type {connection} for driver {driver_lib.__name__}. Try using one of this connections: {get_connection_names(driver_lib)}"


def create_default_driver_conn(driver_lib: ModuleType, connection: str) -> Type:
    """ Create a default connection class when not provided in Driver.
    Will be used to try to connect to an instrument. """
    Driver = getattr(driver_lib, f'Driver')

    if connection == 'DEFAULT':
        class Driver_DEFAULT(Driver):
            def __init__(self):
                Driver.__init__(self)

        return Driver_DEFAULT

    if connection == 'VISA':
        class Driver_VISA(Driver):
            def __init__(self, address='GPIB0::2::INSTR', **kwargs):
                import pyvisa as visa

                self.TIMEOUT = 15000  # ms

                rm = visa.ResourceManager()
                self.controller = rm.open_resource(address)
                self.controller.timeout = self.TIMEOUT

                Driver.__init__(self)

            def close(self):
                try: self.controller.close()
                except: pass

            def query(self, command):
                result = self.controller.query(command)
                result = result.strip('\n')
                return result

            def write(self, command):
                self.controller.write(command)

            def read(self):
                return self.controller.read()

        return Driver_VISA

    if connection == 'GPIB':
        class Driver_GPIB(Driver):
            def __init__(self, address=23, board_index=0, **kwargs):
                import Gpib

                self.inst = Gpib.Gpib(int(board_index), int(address))
                Driver.__init__(self)

            def query(self, query):
                self.write(query)
                return self.read()

            def write(self, query):
                self.inst.write(query)

            def read(self, length=1000000000):
                return self.inst.read().decode().strip('\n')

            def close(self):
                """WARNING: GPIB closing is automatic at sys.exit() doing it twice results in a gpib error"""
                #Gpib.gpib.close(self.inst.id)
                pass

        return Driver_USB

    if connection == 'USB':
        class Driver_USB(Driver):
            def __init__(self, **kwargs):
                import usb
                import usb.core
                import usb.util

                dev = usb.core.find(idVendor=0x104d, idProduct=0x100a)
                dev.reset()
                dev.set_configuration()
                interface = 0
                if dev.is_kernel_driver_active(interface) is True:
                    dev.detach_kernel_driver(interface)  # tell the kernel to detach
                    usb.util.claim_interface(dev, interface)  # claim the device

                cfg = dev.get_active_configuration()
                intf = cfg[(0,0)]
                self.ep_out = usb.util.find_descriptor(intf, custom_match=lambda e: usb.util.endpoint_direction(e.bEndpointAddress) == usb.util.ENDPOINT_OUT)
                self.ep_in = usb.util.find_descriptor(intf, custom_match=lambda e: usb.util.endpoint_direction(e.bEndpointAddress) == usb.util.ENDPOINT_IN)

                assert self.ep_out is not None
                assert self.ep_in is not None

                Driver.__init__(self)

            def write(self, query):
                self.string = query + '\r\n'
                self.ep_out.write(self.string)

            def read(self):
                rep = self.ep_in.read(64)
                const = ''.join(chr(i) for i in rep)
                const = const[:const.find('\r\n')]
                return const

        return Driver_USB

    if connection == 'SOCKET':
        class Driver_SOCKET(Driver):

            def __init__(self, address='192.168.0.8', **kwargs):

                import socket

                self.ADDRESS = address
                self.PORT = 5005
                self.BUFFER_SIZE = 40000

                self.controller = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.controller.connect((self.ADDRESS, int(self.PORT)))

                Driver.__init__(self)

            def write(self, command):
                self.controller.send(command.encode())
                self.controller.recv(self.BUFFER_SIZE)

            def query(self, command):
                self.controller.send(command.encode())
                data = self.controller.recv(self.BUFFER_SIZE)
                return data.decode()

            def close(self):
                try: self.controller.close()
                except: pass
                self.controller = None

        return Driver_SOCKET

    if connection == 'TEST':
        class Controller: pass
        class Driver_TEST(Driver):
            def __init__(self, *args, **kwargs):
                try:
                    Driver.__init__(self)
                except:
                    Driver.__init__(self, *args, **kwargs)

                self.controller = Controller()
                self.controller.timeout = 5000

            def write(self, value):
                pass
            def read(self):
                return '1'
            def read_raw(self):
                return b'1'
            def query(self, value):
                self.write(value)
                return self.read()

        return Driver_TEST

    return None


def get_module_class(driver_lib: ModuleType, module_name: str) -> Type:
    ''' Returns the class Module_XXX of the provided driver library and module_name'''
    assert module_name in get_module_names(driver_lib)
    return getattr(driver_lib, f'Module_{module_name}')


def explore_driver(instance: Type, _print: bool = True) -> str:
    ''' Displays the list of the methods available in this instance '''
    methods = get_instance_methods(instance)
    s = 'This instance contains the following functions:\n'

    for method in methods:
        s += f' - {method[0]}({",".join(method[1])})\n'

    if _print:
        print(s)
        return None
    return s


def get_instance_methods(instance: Type) -> Type:
    ''' Returns the list of all the methods (and their args) in that class '''
    methods = []

    # LEVEL 1
    for name, _ in inspect.getmembers(instance, inspect.ismethod):
        if name != '__init__':
            attr = getattr(instance, name)
            args = list(inspect.signature(attr).parameters)
            methods.append([name, args])

    # LEVEL 2
    for key, val in vars(instance).items():
        try:  # explicit to avoid visa and inspect.getmembers issue
            for name, _ in inspect.getmembers(val, inspect.ismethod):
                if name != '__init__':
                    attr = getattr(getattr(instance, key), name)
                    args = list(inspect.signature(attr).parameters)
                    methods.append([f'{key}.{name}', args])
        except: pass

    return methods


def get_class_args(clas: Type) -> dict:
    ''' Returns the dictionary of the optional arguments required by a class
    with their default values '''
    signature = inspect.signature(clas)
    return {k: v.default for k, v in signature.parameters.items() if (
        v.default is not inspect.Parameter.empty)}


# =============================================================================
# DRIVERS PATHS
# =============================================================================

def get_driver_path(driver_name: str) -> str:
    ''' Returns the config associated with driver_name '''
    assert isinstance(driver_name, str), "drive_name must be a string."
    assert driver_name in DRIVERS_PATHS, f'Driver {driver_name} not found.'
    return DRIVERS_PATHS[driver_name]['path']


def load_drivers_paths() -> dict:
    ''' Returns a dictionary with:
        - key: name of the driver
        - value: path of the driver python script
    '''
    drivers_paths = {}
    for source_name, source_path in paths.DRIVER_SOURCES.items():
        if not os.path.isdir(source_path):
            print(f"Warning, can't found driver folder: {source_path}")
            continue
        for driver_name in os.listdir(source_path):
            temp_path = os.path.join(source_path, driver_name)
            if (os.path.isdir(temp_path)
                    and f'{driver_name}.py' in os.listdir(temp_path)):
                ## Before, raised error if two identical drivers in different folders, I thought of putting a warning message instead but there was too much printing, now don't say that overwrite path (don't overwrite file).
                # if driver_name in drivers_paths.keys():
                #     print(f"Two drivers where found with the name '{driver_name}', will use path {source_name}")
                # assert driver_name not in drivers_paths.keys(), f"Two drivers where found with the name '{driver_name}'. Each driver must have a unique name."
                drivers_paths[driver_name] = {
                    'path': os.path.join(temp_path, f'{driver_name}.py'),
                    'source': source_name}

    return drivers_paths


def update_drivers_paths():
    ''' Update list of available driver '''
    global DRIVERS_PATHS
    DRIVERS_PATHS = load_drivers_paths()
