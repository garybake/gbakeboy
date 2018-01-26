import logging
from .utils import hex2int as h2i
from .utils import print_bin_16, print_bin_8, get_bit_value, twos_comp_8, hex_array


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
            0x0C: {  # 12
                'fn': self.INC_C,
                'cycles': 4,
                'PC': 1
            },
            0x0E: {  # 14
                'fn': self.LD_C_8,
                'immediate_8': True,
                'cycles': 8,
                'PC': 2
            },
            0x11: {  # 17
                'fn': self.LD_DE_16,
                'immediate_16': True,
                'cycles': 12,
                'PC': 3
            },
            0x1A: {  # 26
                'fn': self.LD_A_DE_8,
                'cycles': 8,
                'PC': 1
            },
            0x20: {  # 32
                'fn': self.JR_NZ_8,
                'immediate_8': True,
                'cycles': 12,  # TODO or 18
                'PC': 2
            },
            0x21: {  # 33
                'fn': self.LD_16_HL_nn,
                'immediate_16': True,
                'cycles': 12,
                'PC': 3
            },
            0x31: {  # 49
                'fn': self.LD_16_SP_nn,
                'immediate_16': True,
                'cycles': 12,
                'PC': 3
            },
            0x32: {  # 50
                'fn': self.LD_16_A_iHL_dec,
                'immediate_16': True,
                'cycles': 8,
                'PC': 1
            },
            0x3E: {  # 62
                'fn': self.LD_A_8,
                'immediate_8': True,
                'cycles': 8,
                'PC': 2
            },
            0x77: {  # 119
                'fn': self.LD_HL_A,
                'immediate_8': True,
                'cycles': 8,
                'PC': 1
            },
            0xAF: {  # 175
                'fn': self.XOR_A_n,
                'register': 'A',
                'cycles': 4,
                'PC': 1
            },
            0xCB: {  # 203
                'fn': self.PREFIX_CB,
                'immediate_8': True,
                'cycles': 4,
                'PC': 2
            },
            0xE0: {  # 224
                'fn': self.LDH_A_8,
                'immediate_8': True,
                'cycles': 12,
                'PC': 2
            },
            0xE2: {  # 226
                'fn': self.LD_C_A,
                'cycles': 8,
                'PC': 1
            }
        }

        # TODO fix CP cycles and remove PC?
        self.cb_prefix_instructions = {
            0x7C: {  # 124
                'fn': self.CB_Bit_7_H,
                'register': 'A',
                'cycles': 8,
                'PC': 2
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
        return self.mem.read_byte(self.get_PC(), verbose=False)

    def get_additional_instructions(self, command):
        """
        Get arguments for the instruction
        """
        args = []
        if command.get('immediate_16', False):
            args.append(self.mem.read_word(self.get_PC()+1, verbose=False))
        elif command.get('immediate_8', False):
            args.append(self.mem.read_byte(self.get_PC()+1, verbose=False))
        elif command.get('register', False):
            args.append(command['register'])
        return args

    def execute_command(self, command, args):
        """
        Execute the supplied command using the args
        """
        fn = command['fn']
        return fn(args)

    def increment_pc(self, offset):
        """
        Increment the program counter by the offset
        """
        self.set_PC(self.get_PC()+offset)

    def execute(self):
        """
        Execute the next instruction
        """
        instr = self.get_next_instruction()
        logging.debug(hex(instr))
        command = self.instructions[instr]
        args = self.get_additional_instructions(command)
        logging.debug('Command: {} {} {}'.format(hex(instr), command['fn'].__name__, hex_array(args)))

        extra = self.execute_command(command, args)
        if extra is not "KEEP_PC":
            self.increment_pc(command['PC'])
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

    def set_flags(self, flags):
        """
        Apply a set of flags ('Z','N','H','C')
        Z - zero
        N - Previous op was add
        H - half carry (4th bit carried over)
        C - full carry (8th bit carried over)
        """
        reg_F = 0
        # TODO Assuming flags from previous result are reset
        if flags:
            logging.debug('setting flags: {}'.format(flags))

            flgs = {
                'Z': 0b10000000,
                'N': 0b01000000,
                'H': 0b00100000,
                'C': 0b00010000,
            }
            for flag in flags:
                reg_F = reg_F | flgs[flag]
        self.set_F(reg_F)

    def get_flag(self, flag):
        """
        Get flag value
        Z - zero
        N - Previous op was add
        H - half carry (4th bit carried over)
        C - full carry (8th bit carried over)
        """

        flgs = {
            'Z': 7,
            'N': 6,
            'H': 5,
            'C': 4,
        }

        flag_value = get_bit_value(self.F, flgs[flag])
        logging.debug('Flag {} is {}'.format(flag, flag_value))
        return flag_value == 1

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

    def INC_C(self, args):
        """
        0x0C
        Increment C
        set Z 0 H -
        """
        flags = []

        # Half carry check
        if (((1 & 0xf) + (self.get_C() & 0xf)) & 0x10) == 0x10:
            flags.append('H')

        new_c = self.get_C() + 1

        if new_c > 0xFF:
            new_c = 0
            # TODO Is this how INC raises the Z flag?
            flags.append('Z')

        self.set_C(new_c)
        self.set_flags(flags)

    def LD_C_8(self, args):
        """
        0x0E
        Load 8 bit into C
        """
        nn = args[0]
        self.set_C(nn)
        self.set_flags(False)

    def LD_DE_16(self, args):
        """
        0x11
        Load 16 bit num to DE
        """
        nn = args[0]
        self.set_DE(nn)
        self.set_flags(False)

    def LD_A_DE_8(self, args):
        """
        0x1A
        Load from memory pointed at by DE
        into A
        """
        mem_loc = self.get_DE()
        mem_val = self.mem.read_byte(mem_loc)
        self.set_A(mem_val)

    def JR_NZ_8(self, args):
        """
        0x20
        Jump if zero flag is set
        """
        is_Z_flag_set = self.get_flag('Z')
        if not is_Z_flag_set:
            address_for_next = self.get_PC() + 2
            jump_offset = twos_comp_8(args[0] + 0x100)

            jump_two = address_for_next + jump_offset
            logging.debug('Jumping to: {}'.format(hex(jump_two)))
            self.PC = jump_two
            return "KEEP_PC"
        return

    def LD_16_HL_nn(self, args):
        """
        0x21
        Load 16 bit value into HL
        """
        nn = args[0]
        self.set_HL(nn)
        self.set_flags(False)

    def LD_16_SP_nn(self, args):
        """
        0x31
        Load value into SP
        """
        nn = args[0]
        self.set_SP(nn)
        self.set_flags(False)

    def LD_16_A_iHL_dec(self, args):
        """
        0x32
        Load register ‘A‘ to the memory address pointed to by ‘HL‘ (write 0 to 0x9FFF),
        and then decrement the value of ‘HL‘ (from 0x9FFF to 0x9FFE).
        """
        self.LD_HL_A(args)
        mem_address = self.get_HL()
        self.set_register_16('HL', mem_address - 1)

    def LD_A_8(self, args):
        """
        0x3e
        Load 8 bit into A
        """
        nn = args[0]
        self.set_A(nn)
        self.set_flags(False)

    def LD_HL_A(self, args):
        """
        0x77
        Load A to (HL)
        """
        a_val = self.get_A()
        mem_address = self.get_HL()
        self.mem.write_byte(mem_address, a_val)
        self.set_flags(False)

    def XOR_A_n(self, args):
        """
        0xAF
        XOR A with another register
        Store the result in A
        (XOR with self is 0)
        TODO: Determine register from args
        """
        register = args[0]

        result = self.get_A() ^ self.get_register_8(register)
        if result == 0:
            self.set_flags(['Z'])
        self.set_A(result)

    def PREFIX_CB(self, args):
        """
        0xCB
        For instructions with a prefix of CB
        """
        nn = args[0]
        prefix_func = self.cb_prefix_instructions[nn]['fn']
        prefix_func()

    # CP Prefix instructions

    def CB_Bit_7_H(self):
        """
        0xCB 0x7C
        Get 7th bit of H
        Set Z flag if zero
        """
        H_bit7 = get_bit_value(self.H, 7)
        if H_bit7:
            self.set_flags([])
        else:
            self.set_flags(['Z'])

    def LDH_A_8(self, args):
        """
        0xE0
        LD A, ($FF00+nn)
        Load A to address ($FF00 + nn)
        """
        nn = args[0]
        a_val = self.A
        offset = 0xFF00
        mem_address = offset + nn
        self.mem.write_byte(mem_address, a_val)
        self.set_flags(False)

    def LD_C_A(self, args):
        """
        0xE2
        LD ($FF00+C), A
        Load A to address ($FF00 + C)
        """
        a_val = self.A
        offset = 0xFF00
        mem_address = offset + self.C
        self.mem.write_byte(mem_address, a_val)
        self.set_flags(False)
