from math import floor, sin


# Function for MD5 round 1 operation: F = (x & y) | (~x & z)
def md5_round_1(x, y, z):
    return (x & y) | (~x & z)

# Function for MD5 round 2 operation: G = (x & z) | (y & ~z)
def md5_round_2(x, y, z):
    return (x & z) | (y & ~z)

# Function for MD5 round 3 operation: H = x ^ y ^ z
def md5_round_3(x, y, z):
    return x ^ y ^ z

# Function for MD5 round 4 operation: I = y ^ (x | ~z)
def md5_round_4(x, y, z):
    return y ^ (x | ~z)

def rotate_left(x, n):
    """
    Rotate the bits of the integer `x` to the left by `n` positions.

    Args:
        x (int): The integer to be rotated.
        n (int): The number of positions to rotate the bits.

    Returns:
        int: The result of rotating `x` to the left by `n` positions.
    """
    return (x << n) | (x >> (32 - n))
def modular_add(a, b):
    """
    Perform modular addition of two integers `a` and `b` modulo 2^32.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The result of (a + b) modulo 2^32.
    """
    return (a + b) % (1 << 32)


class MD5():

    def __init__(self):
        self.buffers = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]
        # Initialize T table as per MD5 specifications
        self.T = [int(2**32 * abs(sin(i + 1))) for i in range(64)]

    def md5(self, msg):
        msg = self.pad_msg_to_arr(msg)
        converted_msg = self.convert_msg(msg)
        return converted_msg

    # Correct assignment of shift amounts for each round
    def convert_msg(self, msg):
        msg_buffer = self.buffers[:]

        # Process each 512-bit chunk of the message
        for offset in range(0, len(msg), 64):
            # Convert chunk into sixteen 32-bit words
            block = [int.from_bytes(msg[offset + (x * 4):offset + (x * 4) + 4], 'little') for x in range(16)]

            A, B, C, D = msg_buffer

            # Define shift amounts for each round
            s = [
                [7, 12, 17, 22],  # Round 1 shifts
                [5, 9, 14, 20],  # Round 2 shifts
                [4, 11, 16, 23],  # Round 3 shifts
                [6, 10, 15, 21]  # Round 4 shifts
            ]

            # Main loop
            for i in range(64):
                if i < 16:
                    f = (B & C) | (~B & D)
                    k = i
                    shift = s[0][i % 4]
                elif 16 <= i < 32:
                    f = (D & B) | (~D & C)
                    k = (5 * i + 1) % 16
                    shift = s[1][i % 4]
                elif 32 <= i < 48:
                    f = B ^ C ^ D
                    k = (3 * i + 5) % 16
                    shift = s[2][i % 4]
                else:  # 48 <= i < 64
                    f = C ^ (B | ~D)
                    k = (7 * i) % 16
                    shift = s[3][i % 4]

                temp = D
                D = C
                C = B
                B = B + rotate_left((A + f + self.T[i] + block[k]) & 0xFFFFFFFF, shift)
                A = temp

            # Add this chunk's hash to result so far:
            msg_buffer = [(sum(x) & 0xFFFFFFFF) for x in zip(msg_buffer, [A, B, C, D])]

        # Produce the final hash value (big-endian) as a 128-bit number
        result = sum(x << (32 * i) for i, x in enumerate(msg_buffer))

        # Convert result to hex format
        return '{:032x}'.format(result)
    def pad_msg_to_arr(self, msg):

        """
        Pad the input message to ensure its length is congruent to 448 modulo 512 in bits.
        Additionally, append a 64-bit representation of the original message length.

        Args:
            msg (str): The input message to be padded.

        Returns:
            bytearray: The padded message as a byte array.
        """
        msg_arr = bytearray(msg, 'ascii')
        bits_len = (8 * len(msg_arr)) & 0xffffffffffffffff
        msg_arr.append(0x80)
        while len(msg_arr) % 64 != 56:
            msg_arr.append(0)
        msg_arr += bits_len.to_bytes(8, byteorder='little')
        return msg_arr

md5 = MD5()

if __name__ == '__main__':
    print(md5.md5("wxtwxt123123"))
    print(md5.md5("avl456456"))