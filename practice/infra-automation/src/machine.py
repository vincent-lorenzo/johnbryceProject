import logging

class Machine:
    def __init__(self, name, os, cpu, ram):
        self.name = name
        self.os = os
        self.cpu = cpu
        self.ram = ram

        logging.info(f"machine created: {self.name}, os: {self.os}, cpu: {self.cpu}, ram: {self.ram}GB")

    def to_dict(self):
        return {
            "name": self.name,
            "os": self.os,
            "cpu": self.cpu,
            "ram": self.ram
        }