import os

this_dir = os.path.dirname(__file__)

BIOS_FILE = os.path.join(this_dir, '../roms/bios.rom')

MAX_MEMORY_BYTES = 0xFFFF
MAX_CART_BYTES = 0x8000


LICENCEE_MAP = {
    '00': 'none',
    '01': 'Nintendo R&D1',
    '08': 'Capcom',
    '13': 'Electronic Arts',
    '18': 'Hudson Soft',
    '19': 'b-ai',
    '20': 'kss',
    '22': 'pow',
    '24': 'PCM Complete',
    '25': 'san-x',
    '28': 'Kemco Japan',
    '29': 'seta',
    '30': 'Viacom',
    '31': 'Nintendo',
    '32': 'Bandai',
    '33': 'Ocean/Acclaim',
    '34': 'Konami',
    '35': 'Hector',
    '37': 'Taito',
    '38': 'Hudson',
    '39': 'Banpresto',
    '41': 'Ubi Soft',
    '42': 'Atlus',
    '44': 'Malibu',
    '46': 'angel',
    '47': 'Bullet-Proof',
    '49': 'irem',
    '50': 'Absolute',
    '51': 'Acclaim',
    '52': 'Activision',
    '53': 'American sammy',
    '54': 'Konami',
    '55': 'Hi tech entertainment',
    '56': 'LJN',
    '57': 'Matchbox',
    '58': 'Mattel',
    '59': 'Milton Bradley',
    '60': 'Titus',
    '61': 'Virgin',
    '64': 'LucasArts',
    '67': 'Ocean',
    '69': 'Electronic Arts',
    '70': 'Infogrames',
    '71': 'Interplay',
    '72': 'Broderbund',
    '73': 'sculptured',
    '75': 'sci',
    '78': 'THQ',
    '79': 'Accolade',
    '80': 'misawa',
    '83': 'lozc',
    '86': 'tokuma shoten i*',
    '87': 'tsukuda ori*',
    '91': 'Chunsoft',
    '92': 'Video system',
    '93': 'Ocean/Acclaim',
    '95': 'Varie',
    '96': 'Yonezawa\'s pal',
    '97': 'Kaneko',
    '99': 'Pack in soft',
    'A4': 'Konami (Yu-Gi-Oh!)'
}

MBC_MAP = {
    0x00: 'ROM ONLY',
    0x01: 'MBC1',
    0x02: 'MBC1+RAM',
    0x03: 'MBC1+RAM+BATTERY',
    0x05: 'MBC2',
    0x06: 'MBC2+BATTERY',
    0x08: 'ROM+RAM',
    0x09: 'ROM+RAM+BATTERY',
    0x0B: 'MMM01',
    0x0C: 'MMM01+RAM',
    0x0D: 'MMM01+RAM+BATTERY',
    0x0F: 'MBC3+TIMER+BATTERY',
    0x10: 'MBC3+TIMER+RAM+BATTERY',
    0x11: 'MBC3',
    0x12: 'MBC3+RAM',
    0x13: 'MBC3+RAM+BATTERY',
    0x19: 'MBC5',
    0x1A: 'MBC5+RAM',
    0x1B: 'MBC5+RAM+BATTERY',
    0x1C: 'MBC5+RUMBLE',
    0x1D: 'MBC5+RUMBLE+RAM',
    0x1E: 'MBC5+RUMBLE+RAM+BATTERY',
    0x20: 'MBC6',
    0x22: 'MBC7+SENSOR+RUMBLE+RAM+BATTERY',
    0xFC: 'POCKET CAMERA',
    0xFD: 'BANDAI TAMA5',
    0xFE: 'HuC3',
    0xFF: 'HuC1+RAM+BATTERY'
}

ROM_SIZE_MAP = {
    0x00: '32KByte (no ROM banking)',
    0x01: '64KByte (4 banks)',
    0x02: '128KByte (8 banks)',
    0x03: '256KByte (16 banks)',
    0x04: '512KByte (32 banks)',
    0x05: '1MByte (64 banks) - only 63 banks used by MBC1',
    0x06: '2MByte (128 banks) - only 125 banks used by MBC1',
    0x07: '4MByte (256 banks)',
    0x08: '8MByte (512 banks)',
    0x52: '1.1MByte (72 banks)',
    0x53: '1.2MByte (80 banks)',
    0x54: '1.5MByte (96 banks)'
}

RAM_SIZE_MAP = {
    0x00: 'None',
    0x01: '2 KBytes',
    0x02: '8 Kbytes',
    0x03: '32 KBytes (4 banks of 8KBytes each)',
    0x04: '128 KBytes (16 banks of 8KBytes each)',
    0x05: '64 KBytes (8 banks of 8KBytes each)'
}
