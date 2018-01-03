import logging
from .utils import hex2int as h2i
from .utils import print_bin_16, print_bin_8


class Cpu:

    def __init__(self, memory):
        self.mem = memory

        # registers are 8 bit
        self.A = 0
        self.F = 0
        self.B = 0
        self.C = 0
        self.D = 0
        self.E = 0
        self.H = 0
        self.L = 0
        self.SP = 0
        self.PC = 0

        # self.set_register_8('F', h2i("B0"))  # Why?
        self.set_register_16('AF', h2i("01B0"))
        self.set_register_16('BC', h2i("0013"))
        self.set_register_16('DE', h2i("00D8"))
        self.set_register_16('HL', h2i("014D"))
        self.set_register_16('SP', h2i("FFFE"))
        self.set_register_16('PC', 0)
        logging.debug("default registers set")
        self.print_registers()

        self.instructions = {
            0x21: {  # 33
                'fn': self.LD_16_HL_nn,
                'immediate_16': True,
                'cycles': 12,
                'flags': [],
                'PC': 3
            },
            0x31: {  # 49
                'fn': self.LD_16_SP_nn,
                'immediate_16': True,
                'cycles': 12,
                'flags': [],
                'PC': 3
            },
            0x32: {  # 50
                'fn': self.LD_16_A_iHL_dec,
                'immediate_16': True,
                'cycles': 12,
                'flags': [],
                'PC': 3
            },
            0xAF: {  # 175
                'fn': self.XOR_A_n,
                'register': 'A',
                'cycles': 4,
                'flags': ['Z'],
                'PC': 1
            }
        }

    def print_registers(self):
        AF = self.get_AF()
        BC = self.get_BC()
        DE = self.get_DE()
        HL = self.get_HL()
        SP = self.get_SP()
        PC = self.get_PC()

        logging.debug("AF: \t{0:X} \t {1}".format(AF, print_bin_16(AF)))
        logging.debug("BC: \t{0:X} \t {1}".format(BC, print_bin_16(BC)))
        logging.debug("DE: \t{0:X} \t {1}".format(DE, print_bin_16(DE)))
        logging.debug("HL: \t{0:X} \t {1}".format(HL, print_bin_16(HL)))
        logging.debug("SP: \t{0:X} \t {1}".format(SP, print_bin_16(SP)))
        logging.debug("PC: \t{0:X} \t {1}".format(PC, print_bin_16(PC)))

    def get_next_instruction(self):
        """
        Get the instruction opcode from the PC
        """
        return self.mem.read_byte(self.get_PC())

    def get_additional_instructions(self, command):
        """
        Get arguments for the instruction
        """
        args = []
        if command.get('immediate_16', False):
            args.append(self.mem.read_word(self.get_PC()+1))
        elif command.get('immediate_8', False):
            args.append(self.mem.read_byte(self.get_PC()+1))
        elif command.get('register', False):
            args.append(command['register'])
        return args

    def execute_command(self, command, args):
        """
        Execute the supplied command using the args
        """
        fn = command['fn']
        fn(args)

    def increment_pc(self, offset):
        """
        Increment the program counter by the offset
        """
        self.set_PC(self.get_PC()+offset)

    # def set_flags(self, flags):
    #     """
    #     Set the flags based on the result of the operation
    #     """
    #     for flag in flags:
    #         self.set_flag(flag)

    def set_flag_Z(self):
        flags = self.get_F
        mask = 1 << 8
        flags |= mask
        self.set_F(flags)

    def reset_flag_Z(self):
        pass

    def execute(self):
        """
        Execute the next instruction
        """
        instr = self.get_next_instruction()
        # logging.debug(hex(instr))
        command = self.instructions[instr]
        args = self.get_additional_instructions(command)
        logging.debug('Command: {} {} {}'.format(hex(instr), command['fn'].__name__, args))

        self.execute_command(command, args)
        self.increment_pc(command['PC'])
        # self.set_flags(command['flags'])
        return command['cycles']

    def set_register_8(self, reg, val):
        """
        set register: reg: str, val: int
        """
        logging.debug('set_register_8: ' + reg)
        # create dict with registers as key and functions as vals (sort of a jump table)
        fns = {
            'A': self.set_A,
            'B': self.set_B,
            'C': self.set_C,
            'D': self.set_D,
            'E': self.set_E,
            'F': self.set_F,  # Delete Me
            'H': self.set_H,
            'L': self.set_L
        }
        fns[reg](val)

    def set_register_16(self, reg, val):
        fns = {
            'AF': self.set_AF,
            'BC': self.set_BC,
            'DE': self.set_DE,
            'HL': self.set_HL,
            'SP': self.set_SP,
            'PC': self.set_PC
        }
        fns[reg](val)

    def get_register_8(self, reg):
        """
        get value of register
        """
        fns = {
            'A': self.get_A,
            'F': self.get_F,
            'B': self.get_B,
            'C': self.get_C,
            'D': self.get_D,
            'E': self.get_E,
            'H': self.get_H,
            'L': self.get_L
        }
        return fns[reg]()

    def get_register_16(self, reg):
        fns = {
            'AF': self.get_AF,
            'BC': self.get_BC,
            'DE': self.get_DE,
            'HL': self.get_HL,
            'SP': self.get_SP,
            'PC': self.get_PC
        }
        return fns[reg]()

    def set_flag(self, flag):
        """
        set a flag ('Z','N','H','C')
        Z - zero
        N - Previous op was add
        H - half carry (4th bit carried over)
        C - full carry (8th bit carried over)
        """
        logging.debug('setting flag: {}'.format(flag))
        flgs = {
            'Z': 0b10000000,
            'N': 0b01000000,
            'H': 0b00100000,
            'C': 0b00010000,
        }
        # TODO: check this
        self.set_F(self.get_F() & flgs[flag])

    # 8-bit setters
    def set_A(self, val):
        self.A = val

    def set_B(self, val):
        self.B = val

    def set_C(self, val):
        self.C = val

    def set_D(self, val):
        self.D = val

    def set_E(self, val):
        self.E = val

    # Delete me
    def set_F(self, val):
        self.F = val

    def set_H(self, val):
        self.H = val

    def set_L(self, val):
        self.L = val

    # 16-bit setters
    def set_AF(self, val):
        self.A = (val & 0b1111111100000000) >> 8
        self.F = val & 0b0000000011111111

    def set_BC(self, val):
        self.B = (val & 0b1111111100000000) >> 8
        self.C = val & 0b0000000011111111

    def set_DE(self, val):
        self.D = (val & 0b1111111100000000) >> 8
        self.E = val & 0b0000000011111111

    def set_HL(self, val):
        self.H = (val & 0b1111111100000000) >> 8
        self.L = val & 0b0000000011111111

    def set_SP(self, val):
        self.SP = val

    def set_PC(self, val):
        self.PC = val

    # 8-bit getters
    def get_A(self):
        return self.A

    def get_B(self):
        return self.B

    def get_C(self):
        return self.C

    def get_D(self):
        return self.D

    def get_E(self):
        return self.E

    def get_F(self):
        return self.F

    def is_flag_zero(self):
        pass

    def get_H(self):
        return self.H

    def get_L(self):
        return self.L

    # 16-bit getters
    def get_AF(self):
        return ((self.A << 8) | self.F)

    def get_BC(self):
        return ((self.B << 8) | self.C)

    def get_DE(self):
        return ((self.D << 8) | self.E)

    def get_HL(self):
        return ((self.H << 8) | self.L)

    def get_SP(self):
        return self.SP

    def get_PC(self):
        return self.PC

    # Instructions

    def LD_16_HL_nn(self, args):
        """
        Load 16 bit value into HL
        """
        nn = args[0]
        self.set_HL(nn)

    def LD_16_SP_nn(self, args):
        """
        Load value into SP
        """
        nn = args[0]
        self.set_SP(nn)

    def LD_16_A_iHL_dec(self, args):
        """
        Load register ‘A‘ to the memory address pointed to by ‘HL‘ (write 0 to 0x9FFF),
        and then decrement the value of ‘HL‘ (from 0x9FFF to 0x9FFE).
        """
        a_val = self.get_A()
        mem_address = self.get_HL()
        self.mem.write_byte(mem_address, a_val)
        self.set_register_16('HL', mem_address - 1)

    def XOR_A_n(self, args):
        """
        XOR A with another register
        Store the result in A
        (XOR with self is 0)
        """
        register = args[0]

        result = self.get_A() ^ self.get_register_8(register)
        if result == 0:
            self.set_flag('Z')
        self.set_A(result)
