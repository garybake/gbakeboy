import logging
from utils import hex2int as h2i


class Cpu:

    def __init__(self, memory):
        self.mem = memory

        # registers are private (8 bit)
        self._A = 0
        self._F = 0
        self._B = 0
        self._C = 0
        self._D = 0
        self._E = 0
        self._H = 0
        self._L = 0
        self._SP = 0
        self._PC = 0

        # self.set_register_8('F', h2i("B0"))  # Why?
        self.set_register_16('AF', h2i("01B0"))
        self.set_register_16('BC', h2i("0013"))
        self.set_register_16('DE', h2i("00D8"))
        self.set_register_16('HL', h2i("014D"))
        self.set_register_16('SP', h2i("FFFE"))
        self.set_register_16('PC', 0)
        logging.debug("default registers set")
        self.print_registers()

    def print_registers(self):
        logging.debug("AF: \t{0:X}".format(self._get_AF()))
        logging.debug("BC: \t{0:X}".format(self._get_BC()))
        logging.debug("DE: \t{0:X}".format(self._get_DE()))
        logging.debug("HL: \t{0:X}".format(self._get_HL()))
        logging.debug("SP: \t{0:X}".format(self._get_SP()))
        logging.debug("PC: \t{0:X}".format(self._get_PC()))

    def execute(self):
        # get the instruction opcode from the PC
        instr = self.mem.read_byte(self._get_PC())
        args = []

        # decoding
        instructions = {
            0x31: {
                'fn': self._LD_16_SP_nn,
                'immediate_16': True,
                'cycles': 12,
                'flags': [],
                'PC': 3
            }
        }
        logging.debug('Command: {}'.format(hex(instr)))
        command = instructions[instr]
        logging.debug('Command: {}'.format(command['fn'].__name__))

        # fetch additional
        if command['immediate_16']:
            args.append(self.mem.read_word(self._get_PC()+1))
        elif command['immediate_8']:
            args.append(self.mem.read_byte(self._get_PC()+1))

        # execute the command
        fn = command['fn']
        fn(args)
        logging.debug('Args: {}'.format(hex(args[0])))

        # increment PC
        self._set_PC(self._get_PC()+command['PC'])

        # set flags
        # _set_flags[command['flags']]

    def set_register_8(self, reg, val):
        """
        set register: reg: str, val: int
        """
        logging.debug('set_register_8: ' + reg)
        # create dict with registers as key and functions as vals (sort of a jump table)
        fns = {
            'A': self._set_A,
            'B': self._set_B,
            'C': self._set_C,
            'D': self._set_D,
            'E': self._set_E,
            'F': self._set_F,  # Delete Me
            'H': self._set_H,
            'L': self._set_L
        }
        fns[reg](val)

    def set_register_16(self, reg, val):
        fns = {
            'AF': self._set_AF,
            'BC': self._set_BC,
            'DE': self._set_DE,
            'HL': self._set_HL,
            'SP': self._set_SP,
            'PC': self._set_PC
        }
        fns[reg](val)

    def get_register_8(self, reg):
        """
        get value of register
        """
        fns = {
            'A': self._get_A(),
            'F': self._get_F(),
            'B': self._get_B(),
            'C': self._get_C(),
            'D': self._get_D(),
            'E': self._get_E(),
            'H': self._get_H(),
            'L': self._get_L()
        }
        fn = fns[reg]
        return fn()

    def get_register_16(self, reg):
        fns = {
            'AF': self._get_AF(),
            'BC': self._get_BC(),
            'DE': self._get_DE(),
            'HL': self._get_HL(),
            'SP': self._get_SP(),
            'PC': self._get_PC()
        }
        fn = fns[reg]
        return fn()

    def set_flag(self, flag):
        """
        set a flag ('Z','N','H','C')
        Z - zero
        N - Previous op was add
        H - half carry (4th bit carried over)
        C - full carry (8th bit carried over)
        """
        flgs = {
            'Z': 0b10000000,
            'N': 0b01000000,
            'H': 0b00100000,
            'C': 0b00010000,
        }
        self._set_F(self._get_F & flgs[flag])

    # commands

    # LD nn,n (1)
    def LD_nn_n(nn, n):
        pass

    # LD r1,r2 (2)
    def LD_r1_r2(r1, r2):
        pass

    # LD A, n (3)
    def LD_A_n(A, n):
        pass

    # LD n, A (4)
    def LD_n_A(n, A):
        pass

    # LD A, (C) (5)
    def LD_A_C(A, C):
        pass

    # LD (C), A (6)
    def LD_C_A(C, A):
        pass

    # LD A, (HLD) (7)
    def LD_A_HLD():
        pass

    # LD A, (HL-) (8)
    def LD_A_HL():
        pass

    # LDD A, (HL) (9)
    def LDD_A_HL():
        pass

    # LD (HLD), A (10)
    def LD_HLD_A():
        pass

    # LD (HL-), A (11)
    def LDD_HL_A():
        pass

    # LD (HL), A (12)
    def LDD_HL_A():
        pass

    # LD A, (HLI) (13)
    def LD_A_HLI():
        pass

    # LD A, (HL+) (14)
    def LD_A_HLP():
        pass

    # LDI A, (HL) (15)
    def LDI_A_HL():
        pass

    # LD (HLI), A (16)
    def LD_HLI_A():
        pass

    # LD (HL+), A (17)
    def LDI_HLP_A():
        pass

    # LDI (HL), A (18)
    def LDI_HL_A():
        pass

    # 8-bit setters
    def _set_A(self, val):
        self._A = val

    def _set_B(self, val):
        self._B = val

    def _set_C(self, val):
        self._C = val

    def _set_D(self, val):
        self._D = val

    def _set_E(self, val):
        self._E = val

    # Delete me
    def _set_F(self, val):
        self._F = val

    def _set_H(self, val):
        self._H = val

    def _set_L(self, val):
        self._L = val

    # 16-bit setters
    def _set_AF(self, val):
        self._A = val & 0b0000000011111111
        self._F = (val & 0b1111111100000000) >> 8

    def _set_BC(self, val):
        self._B = val & 0b0000000011111111
        self._C = (val & 0b1111111100000000) >> 8

    def _set_DE(self, val):
        self._D = val & 0b0000000011111111
        self._E = (val & 0b1111111100000000) >> 8

    def _set_HL(self, val):
        self._H = val & 0b0000000011111111
        self._L = (val & 0b1111111100000000) >> 8

    def _set_SP(self, val):
        self._SP = val

    def _set_PC(self, val):
        self._PC = val

    # 8-bit getters
    def _get_A(self):
        return self._A

    def _get_B(self):
        return self._B

    def _get_C(self):
        return self._C

    def _get_D(self):
        return self._D

    def _get_E(self):
        return self._E

    def _get_H(self):
        return self._H

    def _get_L(self):
        return self._L

    # 16-bit getters
    def _get_AF(self):
        return ((self._A << 8) | self._F)

    def _get_BC(self):
        return ((self._B << 8) | self._C)

    def _get_DE(self):
        return ((self._D << 8) | self._E)

    def _get_HL(self):
        return ((self._H << 8) | self._L)

    def _get_SP(self):
        return self._SP

    def _get_PC(self):
        return self._PC

    def _LD_16_SP_nn(self, args):
        nn = args[0]
        self._set_SP(nn)
