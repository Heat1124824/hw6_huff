class Node:
    def __init__(self, id, ch, w, t, le, ri):
        self.id = id
        self.ch = ch  # 文字
        self.w = w  # 權重總和
        self.t = t
        self.le = le  # 左側子節點
        self.ri = ri  # 右側子節點


def dfs(hf, code, id, level):
    if hf[id].t == False:
        code[level] = '0'
        dfs(hf, code, hf[id].le, level + 1)
        code[level] = '1'
        dfs(hf, code, hf[id].ri, level + 1)
    else:
        print(hf[id].ch, " ", end='')
        for i in range(level):
            print(code[i], end='')
        print()


def generate_huffman_codes(hf, node, current_code=""):
    huffman_codes = {}
    if node.ch is not None:
        huffman_codes[node.ch] = current_code
    else:
        huffman_codes.update(generate_huffman_codes(hf, hf[node.le], current_code + '0'))
        huffman_codes.update(generate_huffman_codes(hf, hf[node.ri], current_code + '1'))
        
    return huffman_codes


def encode_message(message, huffman_codes):
    encoded_message = ""
    for char in message:
        encoded_message += huffman_codes[char]
    return encoded_message


def decode_message(encoded_message, root, hf):
    decoded_message = ""
    current_node = root
    for bit in encoded_message:
        if bit == '0':
            current_node = hf[current_node.le]
        else:
            current_node = hf[current_node.ri]
        if current_node.ch is not None:
            decoded_message += current_node.ch
            current_node = root
    return decoded_message


def main():
    # c = ['p', 'l', 'i', 't', 'o']
    # w = [6, 4, 5, 7, 8]

    c = ['m', 'd', 'e', 'r', 'a']
    w = [3, 2, 5, 9, 6]

    hf = [0] * 101
    code = [0] * 10

    tmp = []
    num = len(c)
    for i in range(len(c)):
        hf[i] = Node(i, c[i], w[i], True, 0, 0)
        tmp.append(hf[i])
    tmp = sorted(tmp, key=lambda x: x.w)
    while len(tmp) > 1:
        a = tmp[0]
        del tmp[0]
        b = tmp[0]
        del tmp[0]
        n = Node(num, None, a.w + b.w, 0, a.id, b.id)
        hf[num] = n
        tmp.append(n)
        tmp = sorted(tmp, key=lambda x: x.w)
        num = num + 1

    root = tmp[0]
    dfs(hf, code, root.id, 0)

    huffman_codes = generate_huffman_codes(hf, root)

    # message = "pilot"
    message = "dream"
    encoded_message = encode_message(message, huffman_codes)
    print("Encoded Message:", encoded_message)
    decoded_message = decode_message(encoded_message, root, hf)
    print("Decoded Message:", decoded_message)


if __name__ == "__main__":
    main()
