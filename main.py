import random
from rubric import *
from Aes import *
from dna import *
from chaos import *
from ImageCryptography import *


def rubrick(image_path):
    master_key = 0x2b7e151628aed2a6abf7158809cf4f3c
    aes = AES(master_key)
    image = read_image(image_path)
    dict_key = create_key(image, ITER_MAX=1, aes=aes)
    save_key(dict_key)
    en_image = encrypt_image(image, aes=aes)
    save_image(en_image, "ENCRYPT/rub_enc_img.jpeg")
    key_path = "./key.json"
    #encrypted_image = read_image(image_path)
    encrypted_image = en_image
    de_img = decrypt_image(encrypted_image,key_path, aes)
    save_image(de_img, "DECRYPT/rub_dec_img.jpg")
    return


def dna(image_path):
    file_path = image_selector(image_path)
    key,m,n = securekey(file_path)
    update_lorentz(key)
    blue,green,red=decompose_matrix(file_path)
    blue_e,green_e,red_e=dna_encode(blue,green,red)
    Mk_e = key_matrix_encode(key,blue)
    blue_final, green_final, red_final = xor_operation(blue_e,green_e,red_e,Mk_e)
    x,y,z=gen_chaos_seq(m,n)
    fx,fy,fz=sequence_indexing(x,y,z)
    blue_scrambled,green_scrambled,red_scrambled = scramble(fx,fy,fz,blue_final,red_final,green_final)
    b,g,r=dna_decode(blue_scrambled,green_scrambled,red_scrambled)
    img=recover_image(b,g,r,file_path)
    decrypt(img,fx,fy,fz,file_path,Mk_e,blue,green,red)
    return

def chaos(image_path):
    key = 20
    img = cv2.imread(image_path)
    ArnoldCatEncryption(image_path, key)
    ArnoldCatDecryption("ENCRYPT/cao_enc_img.png", key)
    return


def HE(image_path):
    bitlen = 128
    public_key, private_key = Paillier.generate_keys(bitlen)
    img_path = image_path
    original_img = Image.open(img_path)
    img_array = ImgEncrypt(public_key, original_img)
    saveEncryptedImg(img_array, "he_enc_img.pkl")
    adjusted_img_array = homomorphicBrightness(public_key, img_array, factor=10)
    saveEncryptedImg(adjusted_img_array, "adj_encrypted_image.pkl")
    decrypted_adjusted_img = ImgDecrypt(public_key, private_key, adjusted_img_array)
    decrypted_adjusted_img.save("DECRYPT/he_dec_img.tiff")
    print("Decrypted and Adjusted Image:")
    decrypted_adjusted_img.show()


def main():
    image_path = "iris.jpeg"
    imagepath = "house.tiff"
    image_path_ = "exa.png"
    imagePath = "lena512rgb.tiff"
    program_choice = 4 #random.randint(1, 4)
    if program_choice == 1:
        rubrick(image_path)
    elif program_choice == 2:
        dna(imagepath)
    elif program_choice == 3:
        chaos(image_path_)
    else:
        HE(imagePath)

    print("Encryption complete!")


if __name__ == "__main__":
    main()
