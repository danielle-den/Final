import cv2,gzip,bz2, lzma, numpy as np


# Load image
image = cv2.imread("mario.bmp")


def gzip_compress():
    image_bytes = cv2.imencode('.bmp', image)[1].tobytes()

    for i in range(0, 10):
        # Compress images
        compressed_data = gzip.compress(image_bytes,i)
        print("Compressed size: ", len(compressed_data))

        # Decompress images and revert to nunpy array
        decompressed_data = gzip.decompress(compressed_data)
        decompressed_image = cv2.imdecode(np.frombuffer(decompressed_data, dtype=np.uint8), cv2.IMREAD_COLOR)
        
        # Display compressed images
        cv2.imshow('Decompressed Image '+str(i), decompressed_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def bz2_compress():
    image_bytes = cv2.imencode('.bmp', image)[1].tobytes()

    for i in range(1, 10):
        compressed_data = bz2.compress(image_bytes,i)
        print("Compressed size: "+str(i), len(compressed_data))

        decompressed_data = bz2.decompress(compressed_data)
        decompressed_image = cv2.imdecode(np.frombuffer(decompressed_data, dtype=np.uint8), cv2.IMREAD_COLOR)

        cv2.imshow('Decompressed Image '+str(i), decompressed_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def lzma_compress():
    image_bytes = cv2.imencode('.bmp', image)[1].tobytes()

    # Compress the image bytes using LZMA
    compressed_data = lzma.compress(image_bytes)

    print("lzma compressed image: ", len(compressed_data))
    # Decompress the data if needed
    decompressed_data = lzma.decompress(compressed_data)

    # Optional: Convert the decompressed bytes back to an OpenCV image
    if decompressed_data:
        decompressed_image = cv2.imdecode(np.frombuffer(decompressed_data, dtype=np.uint8), cv2.IMREAD_COLOR)

        # Display the original and decompressed images for comparison
        cv2.imshow('Original Image', image)
        cv2.imshow('Decompressed Image', decompressed_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Decompression failed.")

def jpeg_compress():
    for i in range(0,100,10):
        # Encode and save the image with JPEG compression
        cv2.imwrite('compressed_image_' + str(i) + '.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY), i])

        # Read and display the compressed image
        # compressed_image = cv2.imread('compressed_image.jpg')
        # cv2.imshow('Compressed Image', compressed_image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

print("Uncompressed size: ", image.size)

# gzip_compress()
# bz2_compress()
# lzma_compress()
# jpeg_compress()

