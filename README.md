# 作業6 - 加密與解密文字
題目:
本次作業要求同學使用霍夫曼編碼對一個單字進行加密，以及對已經加密後的單字進行解密，題目有兩個問題。
Q1. generate_huffman_codes函式中會將dfs函式列出的每個字元代表的霍夫曼碼轉換成字典(huffman_codes = {})，這個函式中有三個參數，一個是hf，即講義第17頁的陣列，一個是node，代表現在走訪的節點，而current_code代表每個字元的編碼，初始設為空字串。
當走訪的是樹葉節點(node.ch，代表字元所在的節點)，則把這個字元的霍夫曼碼寫入字典(提示: huffman_codes[...] = ...)。
如果條件不成立(還在中間節點)，則要使用遞迴法，找出每個字元代表的霍夫曼碼，向左走訪的節點要將current_code加入0，向右走訪的節點要將current_code加入1。最後要回傳huffman_codes字典。
提示: 在使用遞迴法時，Python有個字典函式update()，它可以將新的項目放進字典裡面。
Q2. encode_message函式會加密文字，其中message參數是要加密的文字，huffman_codes就是第一題生出來的霍夫曼編碼字典，請完成加密程序並回傳encoded_message。
Q3. decode_message函式會加密文字，其中encoded_message參數是要加密過文字，root是霍夫曼樹的根節點(tmp[0])，hf即講義第17頁的陣列，請完成解密程序並回傳decoded_message。
