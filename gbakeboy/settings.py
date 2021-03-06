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

OLD_LICENCEE_MAP = {
    0x00: 'none',
    0x01: 'nintendo',
    0x08: 'capcom',
    0x09: 'hot-b',
    0x0A: 'jaleco',
    0x0B: 'coconuts',
    0x0C: 'elite systems',
    0x13: 'electronic arts',
    0x18: 'hudsonsoft',
    0x19: 'itc entertainment',
    0x1A: 'yanoman',
    0x1D: 'clary',
    0x1F: 'virgin',
    0x24: 'pcm complete',
    0x25: 'san-x',
    0x28: 'kotobuki systems',
    0x29: 'seta',
    0x30: 'infogrames',
    0x31: 'nintendo',
    0x32: 'bandai',
    0x33: 'GBC - see above',
    0x34: 'konami',
    0x35: 'hector',
    0x38: 'capcom',
    0x39: 'banpresto',
    0x3C: '*entertainment i',
    0x3E: 'gremlin',
    0x41: 'ubi soft',
    0x42: 'atlus',
    0x44: 'malibu',
    0x46: 'angel',
    0x47: 'spectrum holoby',
    0x49: 'irem',
    0x4A: 'virgin',
    0x4D: 'malibu',
    0x4F: 'u.s. gold',
    0x50: 'absolute',
    0x51: 'acclaim',
    0x52: 'activision',
    0x53: 'american sammy',
    0x54: 'gametek',
    0x55: 'park place',
    0x56: 'ljn',
    0x57: 'matchbox',
    0x59: 'milton bradley',
    0x5A: 'mindscape',
    0x5B: 'romstar',
    0x5C: 'naxat soft',
    0x5D: 'tradewest',
    0x60: 'titus',
    0x61: 'virgin',
    0x67: 'ocean',
    0x69: 'electronic arts',
    0x6E: 'elite systems',
    0x6F: 'electro brain',
    0x70: 'infogrames',
    0x71: 'interplay',
    0x72: 'broderbund',
    0x73: 'sculptered soft',
    0x75: 'the sales curve',
    0x78: 't*hq',
    0x79: 'accolade',
    0x7A: 'triffix entertainment',
    0x7C: 'microprose',
    0x7F: 'kemco',
    0x80: 'misawa entertainment',
    0x83: 'lozc',
    0x86: 'tokuma shoten intermedia',
    0x8B: 'bullet-proof software',
    0x8C: 'vic tokai',
    0x8E: 'ape',
    0x8F: 'i_max',
    0x91: 'chun soft',
    0x92: 'video system',
    0x93: 'tsuburava',
    0x95: 'varie',
    0x96: 'yonezawas pal',
    0x97: 'kaneko',
    0x99: 'arc',
    0x9A: 'nihon bussan',
    0x9B: 'tecmo',
    0x9C: 'imagineer',
    0x9D: 'banpresto',
    0x9F: 'nova',
    0xA1: 'hori electric',
    0xA2: 'bandai',
    0xA4: 'konami',
    0xA6: 'kawada',
    0xA7: 'takara',
    0xA9: 'technos japan',
    0xAA: 'broderbund',
    0xAC: 'toei animation',
    0xAD: 'toho',
    0xAF: 'namco',
    0xB0: 'acclaim',
    0xB1: 'ascii or nexoft',
    0xB2: 'bandai',
    0xB4: 'enix',
    0xB6: 'hal',
    0xB7: 'snk',
    0xB9: 'pony canyon',
    0xBA: '*culture brain o',
    0xBB: 'sunsoft',
    0xBD: 'sony imagesoft',
    0xBF: 'sammy',
    0xC0: 'taito',
    0xC2: 'kemco',
    0xC3: 'squaresoft',
    0xC4: 'tokuma shoten intermedia',
    0xC5: 'data east',
    0xC6: 'tonkin house',
    0xC8: 'koei',
    0xC9: 'ufl',
    0xCA: 'ultra',
    0xCB: 'vap',
    0xCC: 'use',
    0xCD: 'meldac',
    0xCE: '*pony canyon or',
    0xCF: 'angel',
    0xD0: 'taito',
    0xD1: 'sofel',
    0xD2: 'quest',
    0xD3: 'sigma enterprises',
    0xD4: 'ask kodansha',
    0xD6: 'naxat soft',
    0xD7: 'copya systems',
    0xD9: 'banpresto',
    0xDA: 'tomy',
    0xDB: 'ljn',
    0xDD: 'ncs',
    0xDE: 'human',
    0xDF: 'altron',
    0xE0: 'jaleco',
    0xE1: 'towachiki',
    0xE2: 'uutaka',
    0xE3: 'varie',
    0xE5: 'epoch',
    0xE7: 'athena',
    0xE8: 'asmik',
    0xE9: 'natsume',
    0xEA: 'king records',
    0xEB: 'atlus',
    0xEC: 'epic/sony records',
    0xEE: 'igs',
    0xF0: 'a wave',
    0xF3: 'extreme entertainment',
    0xFF: 'ljn'
}
