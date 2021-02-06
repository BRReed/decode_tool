import base64


def get_encoded_msg():
    """Gets encoded message from user

    Returns:
        string: encoded message from user input
    """
    print("Enter text you would like to decode:\n")
    e_msg = input(">")
    return e_msg

def get_decode_method():
    """User selects decode method

    Returns:
        int: based on user input, each valid int is equal to a decode method
    """
    de_methods = [1, 2, 3]
    while True:
        print("Choose decode method:")
        print("Type '1' for base64")
        print("Type '2' for hexadecimal")
        print("Type '3' for octal")
        try:
            de_method = int(input(">"))
            if de_method in de_methods:
                return de_method
            else:
                print('That is not a valid selection, try again')
                continue
        except ValueError:
            print('Enter a whole number')

def de_base64(msg):
    """Decode a base64 string

    Args:
        msg (string): string to be decoded written in base64
    Returns:
        (string): decoded text
    """
    try:
        msg_ascii = msg.encode('ascii')
        msg_bytes = base64.b64decode(msg_ascii)
        msg_decoded = msg_bytes.decode('ascii')
        return msg_decoded
    except:
        print('Invalid base64-encoded string')

def de_hex(msg):
    """Decode a hexadecimal string

    Args:
        msg (string): string to be decoded written in hex
    Returns:
        (string): decoded text
    """
    try:
        return bytes.fromhex(msg).decode('utf-8')
    except (UnicodeDecodeError, ValueError):
        print('Invalid hexadecimal-encoded string')

def de_octal(msg):
    """Decode an octal string

    Args:
        msg (string): string to be decoded writtin in octal

    Returns:
        string: decoded text
    """
    try:
        msglist = msg.split(' ')
        characters = []
        for octal in msglist:
            n = int(octal, base=8)
            characters.append(n)
        d_msg = ''
        for c in characters:
            d_msg += ''.join(chr(c))
        return d_msg
    except ValueError:
        print('Invalid octal-encoded message')

def main():
    e_msg = get_encoded_msg()
    d_method = get_decode_method()
    if d_method == 1:
        print(de_base64(e_msg))
    if d_method == 2:
        print(de_hex(e_msg))
    if d_method == 3:
        print(de_octal(e_msg))

if __name__ == "__main__":
    main()