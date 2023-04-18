#for 128-bit
#key = '2b7e151628aed2a6abf7158809cf4f3c'#bytes.fromhex('2b7e151628aed2a6abf7158809cf4f3c')
#for 192-bit
#key = bytes.fromhex('8e73b0f7da0e6452c810f32b809079e562f8ead2522c6b7b')


# for 256-bit
#key = bytes.fromhex('603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4')

key_matrix = [
    [0x43, 0x126, 0x21  ,0x22],
    [0x174, 0x210, 0x166, 0x106],
    [0x171, 0x247, 0x21, 0x88],
    [0x9, 0x207, 0x244, 0x243]
 ]
# substitute box
s_box = [
    [99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103, 43, 254, 215, 171, 118],
    [202, 130, 201, 125, 250, 89, 71, 240, 173, 212, 162, 175, 156, 164, 114, 192],
    [183, 253, 147, 38, 54, 63, 247, 204, 52, 165, 229, 241, 113, 216, 49, 21],
    [4, 199, 35, 195, 24, 150, 5, 154, 7, 18, 128, 226, 235, 39, 178, 117],
    [9, 131, 44, 26, 27, 110, 90, 160, 82, 59, 214, 179, 41, 227, 47, 132],
    [83, 209, 0, 237, 32, 252, 177, 91, 106, 203, 190, 57, 74, 76, 88, 207],
    [208, 239, 170, 251, 67, 77, 51, 133, 69, 249, 2, 127, 80, 60, 159, 168],
    [81, 163, 64, 143, 146, 157, 56, 245, 188, 182, 218, 33, 16, 255, 243, 210],
    [205, 12, 19, 236, 95, 151, 68, 23, 196, 167, 126, 61, 100, 93, 25, 115],
    [96, 129, 79, 220, 34, 42, 144, 136, 70, 238, 184, 20, 222, 94, 11, 219],
    [224, 50, 58, 10, 73, 6, 36, 92, 194, 211, 172, 98, 145, 149, 228, 121],
    [231, 200, 55, 109, 141, 213, 78, 169, 108, 86, 244, 234, 101, 122, 174, 8],
    [186, 120, 37, 46, 28, 166, 180, 198, 232, 221, 116, 31, 75, 189, 139, 138],
    [112, 62, 181, 102, 72, 3, 246, 14, 97, 53, 87, 185, 134, 193, 29, 158],
    [225, 248, 152, 17, 105, 217, 142, 148, 155, 30, 135, 233, 206, 85, 40, 223],
    [140, 161, 137, 13, 191, 230, 66, 104, 65, 153, 45, 15, 176, 84, 187, 22]
]
# modsat substitute box 
inv_s_box = [
    [82, 9, 106, 213, 48, 54, 165, 56, 191, 64, 163, 158, 129, 243, 215, 251],
    [124, 227, 57, 130, 155, 47, 255, 135, 52, 142, 67, 68, 196, 222, 233, 203],
    [84, 123, 148, 50, 166, 194, 35, 61, 238, 76, 149, 11, 66, 250, 195, 78],
    [8, 46, 161, 102, 40, 217, 36, 178, 118, 91, 162, 73, 109, 139, 209, 37],
    [114, 248, 246, 100, 134, 104, 152, 22, 212, 164, 92, 204, 93, 101, 182, 146],
    [108, 112, 72, 80, 253, 237, 185, 218, 94, 21, 70, 87, 167, 141, 157, 132],
    [144, 216, 171, 0, 140, 188, 211, 10, 247, 228, 88, 5, 184, 179, 69, 6],
    [208, 44, 30, 143, 202, 63, 15, 2, 193, 175, 189, 3, 1, 19, 138, 107],
    [58, 145, 17, 65, 79, 103, 220, 234, 151, 242, 207, 206, 240, 180, 230, 115],
    [150, 172, 116, 34, 231, 173, 53, 133, 226, 249, 55, 232, 28, 117, 223, 110],
    [71, 241, 26, 113, 29, 41, 197, 137, 111, 183, 98, 14, 170, 24, 190, 27],
    [252, 86, 62, 75, 198, 210, 121, 32, 154, 219, 192, 254, 120, 205, 90, 244],
    [31, 221, 168, 51, 136, 7, 199, 49, 177, 18, 16, 89, 39, 128, 236, 95],
    [96, 81, 127, 169, 25, 181, 74, 13, 45, 229, 122, 159, 147, 201, 156, 239],
    [160, 224, 59, 77, 174, 42, 245, 176, 200, 235, 187, 60, 131, 83, 153, 97],
    [23, 43, 4, 126, 186, 119, 214, 38, 225, 105, 20, 99, 85, 33, 12, 125]
]

mix_column_matrix = [
    [0x2, 0x3, 0x1, 0x1],
    [0x1, 0x2, 0x3, 0x1],
    [0x1, 0x1, 0x2, 0x3],
    [0x3, 0x1, 0x1, 0x2]
]

inv_mix_column_matrix = [
    [0xe, 0xb, 0xd, 0x9],
    [0x9, 0xe, 0xb, 0xd],
    [0xd, 0x9, 0xe, 0xb],
    [0xb, 0xd, 0x9, 0xe]
]


class AES:

    def __init__(self, code):
        self.code = code # brug værdi self til at arbejde med resten af programmet
        #self.x = sympy.symbols('x')
        self.key = []
        self.add_round_key(key_matrix) # start_nøgle
        round = 0
        # gør at vi får alle subkeys
        for i in range(10):
            self.key_expansion(round)
            round += 1

    def define_state(self, plaintext):
        """tager noget tekst og laver det om til en block"""
        plaintext = ' '.join(format(ord(x), 'b') for x in plaintext) # formatere ord til tal
        split = plaintext.split()
        words = []
        a = 0
        # laver en liste med talene fra teksten 
        for i in split:
            text = self.binary_len_eight("0b" + i)
            text = text[2:]
            num_1 = text[:4]
            num_2 = text[4:]
            words.append(str(self.get_number(int("0b" + num_1, 2))) + str(self.get_number(int("0b" + num_2, 2))))
        state_list = []
        
        # laver blocks ud fra tal listen words 
        # hvis ordet er for langt bliver det sat ind i flere blocke
        # hvis ordet er for kort blivr det padet med 0
        while len(words) > 0:
            state_matrix = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
            ]
            b = 0
            for row in state_matrix:
                a = 0
                for col in state_matrix:
                    try:
                        state_matrix[a][b] = "0x" + words[0]
                        words.pop(0)
                    except:
                        pass  
                    a += 1
                b += 1
            state_list.append(state_matrix)
        return state_list

    def get_text_from_state(self, state_list):
        """tager en block og laver den om til tekst"""
        text = ""
        for state in state_list:
            b = 0
            state = self.hexadecimal(state)
            text_list = []
            for row in state:
                a = 0
                for col in row:
                    try:
                        text_list.append(int(state[a][b],0))
                    except:
                        pass
                    a += 1
                b += 1
            for number in text_list:
                text += chr(number) # laver tal om til tekst
        return text


    def string_hex_to_int(self, state):
        """laver string hexadcimal tal til tal"""
        for row in state:
            a = 0
            for col in row:
                try:
                    row[a] = int(col, 0)
                except:
                    pass
                a += 1
        return state

    def encrypt_data(self, plaintext):
        """kryptere tekst"""
        state_list = self.define_state(plaintext) # laver state
        cipher_list = []
        for state in state_list:
            # 10 runders kryptering
            round = 1
            for i in range(9):
                state = self.substitute_bytes(state, s_box)
                state = self.shift_rows(state)
                state = self.mix_coulmn(state, mix_column_matrix) 
                state = self.round_key(state, round)
                round += 1
            state = self.substitute_bytes(state, s_box)
            state = self.shift_rows(state)
            state = self.round_key(state, round)
            cipher_list.append(state)
        cipher = self.get_text_from_state(cipher_list) # visser den krypterde tekst
        return cipher
    
    
    def decrypt_data(self, cipher_text):
        """dekryptere tekst"""
        state_list = self.define_state(cipher_text) # laver state
        plaintext_list = []
        for state in state_list:
            # 10 runders dekryptering
            round = 10
            state = self.round_key(state, round)
            state = self.inverse_shift_rows(state)
            state = self.substitute_bytes(state, inv_s_box) 
            for i in range(9):
                round -= 1
                state = self.round_key(state, round)
                state = self.mix_coulmn(state, inv_mix_column_matrix)
                state = self.inverse_shift_rows(state)
                state = self.substitute_bytes(state, inv_s_box) 
            plaintext_list.append(state)
        text = self.get_text_from_state(plaintext_list)
        return text


    def show_state(self, state, hex_=True):
        """visser state"""
        state_show = state[:]
        if not hex_:
            for row in state_show:
                a = 0
                for col in row:
                    try:
                        row[a] = int(col, 0)
                    except:
                        row[a] = col
                    a += 1
        elif hex_:
            state_show = self.hexadecimal(state_show)
        for row in state_show:
            print(row)

       


    def hexadecimal(self, state, true_state=True):
        """gør tal til hexadecimal tal"""
        if true_state:
            for row in state: 
                a = 0
                for col in row:
                    byte = row[a]
                    try:
                        hex_byte = hex(byte)
                    except:
                        hex_byte = hex(int(byte, 0))
                    row[a] = hex_byte
                    a += 1
        elif not true_state:
            a = 0
            for i in state:
                state[a] = hex(i)
                a += 1

        return state
        

    def check_zero(self, original_byte):
        """tjeker om hexadecimal talet skal have et 0"""
        hexadecimal = len(original_byte)
        if hexadecimal == 3:
            original_byte = original_byte[:2] + '0' + original_byte[2:]
            
        return original_byte
    
    def get_number(self, col_number):
        """hexadecimal tal kan have bogstaver i så den her finder værdien som de bogstaver har"""
        # bliver brugt når der kommer bogstaver i hexadecimal talene 
        number_list = [('a', 10), ('b', 11), ('c', 12), ('d', 13), ('e', 14), ('f', 15)]
        col_number = str(col_number)
        for letter, number in number_list:
            if str(number) == col_number:
                col_number = str(letter)
            elif letter == str(col_number):
                col_number = int(number)
            
        
        try: 
            col_number = int(col_number)
        except:
            col_number = str(col_number)
        return col_number

    def substitute_bytes(self, state, s_box):
        """Her bliver bytes byttede ud med andre bytes"""
        state = self.hexadecimal(state)
        for row in state:
            a = 0 #for hvilken kolonne tallet er i
            for col in row:
                original_byte = row[a] # får et elemnt fra listen
                original_byte = self.check_zero(original_byte)
                row_number = self.get_number(original_byte[2])# får første del a hexadecimal tallet
                col_number = self.get_number(original_byte[3])# får anden del a hexadecimal tallet
                row[a] = s_box[row_number][col_number]# udskifter elementet fra listen du fra s-boksens row og col
                a += 1
        return state

    def shift_rows(self, state):
        """skifter placering af elementerne i rows"""
        b = 0 # får hvilken row tallet er i
        for row in state:
            a = 0 # for hvilken kolonne tallet er i
            switch_state = row[:] # laver en kopi af row som ikke blive ændret 
            for col in row:
                curent_number = switch_state[a]
                switch_number = a - b # hvor tallet skal stå
                # gør at tallet bliver placeret inde i listen når switch number bliver mindre end 1
                if switch_number < 0:
                    switch_number += len(state) 
                row[switch_number] = curent_number
                a += 1
            b += 1  
        return state
    
    
    def inverse_shift_rows(self, state):
        """skifter placering af elementerne i rows bare omvendt"""
        b = 0
        for row in state:
            a = len(state) - 1
            switch_state = row[:]
            for col in row:
                curent_number = switch_state[a]
                switch_number = a + b
                if switch_number > 0:
                    switch_number -= len(state) 
                row[switch_number] = curent_number
                a -= 1
            b += 1   
        return state

    def binary_len_eight(self, number):
        
        check_number = str(number[2:])
        if len(check_number) < 8:
            range_amount = 8 - len(check_number)
            for i in range(range_amount):
                check_number = "0" + str(check_number)
            number = "0b" + check_number
        return number

    def galois_mult(self, a, b):
        """
        Multiplication in the Galois field GF(2^8).
        """
        # jeg tog koden herfra: https://github.com/hlilje/aes-python/blob/master/aes.py
        p = 0
        hi_bit_set = 0
        for i in range(8):
            if b & 1 == 1: p ^= a
            hi_bit_set = a & 0x80
            a <<= 1
            if hi_bit_set == 0x80: a ^= 0x1b
            b >>= 1
        return p % 256

    def mix_coulmn(self, state, mix_list):
        """laver mix coulmn"""
        b = 0
        for row in state:
            a = 0
            col_list = []
            for col in row:
                col_list.append(state[a][b]) # får tal fra state
                a += 1
            # giver de nye værdier
            state[0][b] = self.galois_mult(col_list[0], mix_list[0][0]) ^ self.galois_mult(col_list[1], mix_list[0][1]) ^ \
                self.galois_mult(col_list[2], mix_list[0][2]) ^ self.galois_mult(col_list[3], mix_list[0][3])
            
            state[1][b] = self.galois_mult(col_list[0], mix_list[1][0]) ^ self.galois_mult(col_list[1], mix_list[1][1]) ^ \
                self.galois_mult(col_list[2], mix_list[1][2]) ^ self.galois_mult(col_list[3], mix_list[1][3])
            
            state[2][b] = self.galois_mult(col_list[0], mix_list[2][0]) ^ self.galois_mult(col_list[1], mix_list[2][1]) ^ \
                self.galois_mult(col_list[2], mix_list[2][2]) ^ self.galois_mult(col_list[3], mix_list[2][3])
            
            state[3][b] = self.galois_mult(col_list[0], mix_list[3][0]) ^ self.galois_mult(col_list[1], mix_list[3][1]) ^ \
                self.galois_mult(col_list[2], mix_list[3][2]) ^ self.galois_mult(col_list[3], mix_list[3][3])
            b += 1
        return state


        
    def show_word(self, hex=False):
        """visser ordne fra nøglen"""
        a = 0
        key = self.key[:]
        if hex:
            for i in key:
                key[a] = self.hexadecimal(i)
                a += 1
            a = 0

        for subkey in key:
            for word in subkey:
                print("word", str(a) + ":", word)
                a += 1
    
    def show_subkey(self, hex=False): 
        """visser subkeys fra nøglen"""
        a = 0
        key = self.key[:]
        if hex:
            for i in key:
                key[a] = self.hexadecimal(i)
                a += 1
            a = 0
        for i in key:
            print("SubKey:", a, i)
            a += 1

    def rotword(self, col):
        safe_col = col[:]
        a = 0
        for i in col:
            number = a - 1
            if a < 0:
                number += len(col)
            col[number] = safe_col[a]
            a += 1
        return col

    
    def sub_word(self, col):
        a = 0
        for i in col:
            try:
                num = self.check_zero(str(hex(i)))
            except:
                num = self.check_zero(str(hex(int(i), 2)))
            s_row = self.get_number(num[2])
            s_col = self.get_number(num[3])
            col[a] = s_box[int(s_row)][int(s_col)]
            a += 1
        return col

    def rcon(self, col, round):
        r = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]
        r_list = [r[round], 0, 0, 0]
        for i in range(4):
            col[i] ^= r_list[i]
        return col

    def new_subkey(self, state, rcon):
        new_state = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        for i in range(4):
            new_state[i][0] = (rcon[i] ^ state[i][0])
        
        for i in range(3):
            for j in range(4):
                new_state[j][i+1] = new_state[j][i] ^ state[j][i+1]
            
       
            
        
        return new_state

    def key_expansion(self, round):
        state = self.key[len(self.key)-1]
        new_col = [0, 0, 0, 0]
        a = 0
        for number in new_col:
            new_col[a] = state[a][3]
            a += 1
        rot_col = self.rotword(new_col[:])
        sub_col = self.sub_word(rot_col[:])
        rcon_col = self.rcon(sub_col[:], round)
        subkey = self.new_subkey(state, rcon_col)
        self.add_round_key(subkey)
        

    def add_round_key(self, state):
        subkey = []
        b = 0
        for row in state:
            word = []
            a = 0
            for col in row:
                word.append(state[a][b])
                a += 1
            b += 1
            subkey.append(word)
        self.key.append(subkey)

    def round_key(self, state, round):
        b = 0
        new_state = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        round_matrix = self.string_hex_to_int(self.key[round])
        state = self.string_hex_to_int(state)
        for row in state:
            a = 0
            for col in state:
                state_number = state[a][b]
                key_number = round_matrix[b][a]
                new_state[a][b] = (key_number ^ state_number) % 256
                a += 1
            b += 1
        return new_state

if __name__ == "__main__":
    aes = AES("test")
    while True:
        plaintext = str(input("\nSkriv noget og så kryptere jeg det: "))
        cipher = aes.encrypt_data(plaintext)
        print("\nden krypterde tekst er:", cipher, '\n')
        wait = input("tryk på enter så dekryptere jeg teksten\n")
        text = aes.decrypt_data(cipher)
        print("den dekrypterde tekst er:", text)

